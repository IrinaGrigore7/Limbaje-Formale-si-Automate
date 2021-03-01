import sys

def findNextState(nextWord, patternList):
	
	#caut un prefix al cuvantului format in lista de prefixe ale pattern-ului 
	for i in range (0, len(nextWord)):
		for j in range(0, len(patternList)):
			if patternList[j] == nextWord[i:len(nextWord)]:
				return len(patternList[j])

	return 0

def getMatrix(numberOfStates, patternList):
	deltaMatrix = []

	for i in range(0, numberOfStates):
		currentRow = [] #linia care trebuie completata in matricea delta
		currentWord = patternList[i] #linia curenta
		for j in range(0, 26): #parcurg coloanele
			nextWord = currentWord + chr(j + 65) #adaug fiecare litera pe rand 
												#pentru a gasi urmatoarea stare
			currentRow.append(findNextState(nextWord, patternList))
		deltaMatrix.append(currentRow)

	return deltaMatrix


def printSolution(deltaMatrix, pattern, word):
	q = 0
	#printez indicii la care se gaseste pattern in word
	for i in range(0, len(word)):
		q = deltaMatrix[q][ord(word[i]) - 65]
		if q == len(pattern):
			f2.write(str((i - (len(pattern) - 1))))
			f2.write(" ")

	f2.write("\n")


if __name__ == '__main__':
	filename1 = sys.argv[1]
	filename2 = sys.argv[2]
	f1 = open(filename1, "r")
	f2 = open(filename2, "w")

	stringsList = f1.readlines()

	string1 = stringsList[0]
	pattern = string1[0:len(string1) - 1] #elimin \n

	string2 = stringsList[1]
	word = string2[0:len(string2) - 1] #elimin \n

	numberOfStates = len(pattern) + 1

	patternList = []	# contine prefixele pattern-ului
	patternList.append("") 
	for i in range(1, numberOfStates):
		patternList.append(pattern[0:i])
	
	deltaMatrix = getMatrix(numberOfStates, patternList)

	printSolution(deltaMatrix, pattern, word)




