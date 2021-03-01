import sys
from antlr4 import *
from RegexLexer import RegexLexer
from RegexParser import RegexParser
from RegexVisitor import RegexVisitor
from RegexVisitorEval import RegexVisitorEval

from functools import reduce
from typing import List, Tuple, Set, Dict

import sys

State = int
Word = str
Configuration = Tuple[State, Word]
Transition = Tuple[State, Word, List[State]]
EPSILON = ""


class NFA:
	def __init__(self, numberOfStates: int, alphabet: Set[chr], finalStates: Set[State],
				 delta: Dict[Tuple[State, chr], Set[State]]):
		self.numberOfStates = numberOfStates
		self.states = set(range(self.numberOfStates))
		self.alphabet = alphabet
		self.initialState = 0
		self.finalStates = finalStates
		self.delta = delta

	def epsilonClosure(self, state: State):
		stateList = [state] # o list auxiliara in care pastrez starile pentru care trebuie sa fac inchiderile epsilon
		stateSet = {state} # contine starile care formeaza inchiderea epsilon a starii primite ca parametru
		while len(stateList) != 0:
			stateAux = stateList.pop()
			for (state, char) in self.delta:
				if state == stateAux and char == '': # am gasit o tranzitie pe epsilon
					nextStateSet = self.delta[(state, char)]
					for nextState in nextStateSet:
						if not (nextState in stateSet): #verific ca strea respectiva sa nu fie deja in set
							stateSet.add(nextState)
							stateList.append(nextState)

		return stateSet

	def convert_NFA_to_DFA(self, epsClosureStates, file4):
		stateSet = epsClosureStates[0] #inchiderile epsilon ale starii initiale
		setsList = [stateSet] #lista auxiliara de seturi
		visited = [stateSet] #pastrez toate seturile pe care deja le-am parcurs
		dfa = dict()
		finalStatesDFA = set()

		for i in stateSet: #adaug in setul de stari finale ale DFA-ului, reprezantarile seturilor 
							#care contin cel putin o stare finala din starile finale ale NFA-ului
			if i in self.finalStates:
				stateSetString = repr(stateSet)
				finalStatesDFA.add(stateSetString) 

		while setsList:
			setAux = setsList.pop()
			for char in alphabet:
				stateSetAux = set()
				for i in setAux:
					if (i, char) in self.delta:
						stateSetAux = stateSetAux.union(delta[(i, char)])
				stateSetAux2 = set()
				for i in stateSetAux:
					stateSetAux2 = stateSetAux2.union(epsClosureStates[i])
				if stateSetAux2 not in visited:
					for i in stateSetAux2:
						if i in self.finalStates:
							stateSetString = repr(stateSetAux2)
							finalStatesDFA.add(stateSetString)
							break
					setsList.append(stateSetAux2)
					visited.append(stateSetAux2)
				setString = repr(setAux)
				dfa[(setString, char)] = repr(stateSetAux2)

		self.printDFA(dfa, finalStatesDFA, file4)

	def printDFA(self, dfa, finalStatesDFA, file4):
		stateDict = dict() #cheia este reprezentarea sub forma de string a setului, 
							#iar valoarea este noua stare atribuita
		i = 0

		for (stateSet, char) in dfa:
			if stateSet not in stateDict:
				stateDict[stateSet] = i
				i = i + 1
		file4.write(str(i))
		file4.write("\n")

		for i in finalStatesDFA:
			file4.write(str(stateDict[i]))
			file4.write(" ")
		file4.write("\n")
		print(stateDict)
		for (stateSet, char) in dfa:
			file4.write(str(stateDict[stateSet]))
			file4.write(" ")
			file4.write(char)
			file4.write(" ")
			if stateDict.get(dfa[(stateSet, char)]) == None:
				file4.write("0")
			else:
				file4.write(str(stateDict.get(dfa[(stateSet, char)])))
			file4.write("\n")


if __name__ == '__main__':
	
	file1 = open(sys.argv[1], "r")
	string = file1.readline()
	lastCh = string[0] #modific stringul primit ca input astfel incat 
					   #atunci cand am de doua ori *, sa las doar una
	newString = ""
	for ch in string:
		if (ch == '*') and (ch == lastCh):
			continue
		newString = newString + ch
		lastCh = ch
	file2 = open("input.in", "w")
	file2.write(newString)
	file1.close()
	file2.close()

	input = FileStream("input.in")
	lexer = RegexLexer(input)
	stream = CommonTokenStream(lexer)
	parser = RegexParser(stream)

	tree = parser.expr()

	evalVisitor = RegexVisitorEval()
	nfa = evalVisitor.visit(tree) #nfa-ul rezultat in urma parsarii expresiei regulate
	file3 = open(sys.argv[2], "w")
	delta = evalVisitor.visit(tree).delta
	file3.write(str(nfa.numberOfStates))
	file3.write("\n")
	file3.write(str(nfa.numberOfStates - 1))
	file3.write("\n")
	for i in range(0, len(nfa.delta)):
		(currentState, ch, nextState) = nfa.delta[i]
		states = [nextState]
		ok = 0
		for j in range(i + 1, len(nfa.delta)):
			(currentStateAux, chAux, nextStateAux) = nfa.delta[j]
			if currentState == currentStateAux and ch == chAux:
				states.append(nextStateAux)
		for j in range(0, i):
			(currentStateAux, chAux, nextStateAux) = nfa.delta[j]
			if currentState == currentStateAux and ch == chAux:
				ok = 1
		if ok == 0:
			file3.write(str(currentState))
			file3.write(" ")
			file3.write(ch)
			for i in states:
				file3.write(" ")
				file3.write(str(i))
			file3.write("\n")
	file3.close()
	file4 = open(sys.argv[3], "w+")
	with open(sys.argv[2]) as file:
		numberOfStates = int(file.readline().rstrip())
		alphabet = set()
		finalStates = set(map(int, file.readline().rstrip().split(" ")))
		delta = dict()
		while True:
			transition = file.readline().rstrip().split(" ")
			if transition == ['']:
				break
			if transition[1] == "eps":
				transition[1] = EPSILON
			else:
				alphabet.add(transition[1])

			delta[(int(transition[0]), transition[1])] = set(map(int, transition[2:]))

		nfa = NFA(
			numberOfStates=numberOfStates,
			alphabet=alphabet,
			finalStates=finalStates,
			delta=delta
		)

		epsClosureStates = dict() #gasesc inchiderile epsilon ale fiecarei stari din NFA
		for i in range(0, numberOfStates):
			epsClosureStates[i] = nfa.epsilonClosure(i)
	   
		nfa.convert_NFA_to_DFA(epsClosureStates, file4)
	file1.close()
	file2.close()
	file4.close()