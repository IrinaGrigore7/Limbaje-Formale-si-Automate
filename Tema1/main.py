import sys


def findNextState(nextWord, patternList):
	for i in range(0, len(patternList)):
		if patternList[i] == nextWord:
			return len(patternList[i])

	for i in range (0, len(nextWord)):
		for j in range(0, len(patternList)):
			if patternList[j] == nextWord[i:len(nextWord)]:
				return len(patternList[j])

	return 0


if __name__ == '__main__':
	filename = sys.argv[1]
	f = open(filename, "r")
	stringsList = f.readlines()
	string2 = stringsList[0]
	pattern = string2[0:len(string2)]
	print(pattern)
	string1 = stringsList[1] # are inclus si \n
	word = string1[0:len(string1)]
	print(word)

	numberOfStates = len(pattern) #sirul vid + lungimea pattern-ului
	finalState = numberOfStates
	
	deltaMatrix = []

	patternList = []	
	patternList.append("") 
	for i in range(1, len(pattern)):
		patternList.append(pattern[0:i])
	

	for i in range(0, numberOfStates):
		currentRow = [] #linia care trebuie completata in matricea delta
		currentWord = patternList[i]
		for j in range(0, 26):
			nextWord = currentWord + chr(j + 65)
			currentRow.append(findNextState(nextWord, patternList))
		deltaMatrix.append(currentRow)


	q = 0
	
	for i in range(0, len(word)):
		q = deltaMatrix[q][ord(word[i]) - 65]
		if q == (len(pattern) - 1):
			print(i - (len(pattern) - 2))

	
		







	# currentState = 0
	# nextState = currentState + 1
	# a  = []
	# for i in range(0, 26):
	# 	if pattern[0] == chr(i + 65):
	# 		a.append(nextState)
	# 	else:
	# 		a.append(currentState)
	# deltaMatrix.append(a)
	

	# currentPos = 1
	# previousPos = currentPos - 1
	
	# firstRow = deltaMatrix[previousPos]
	
	# for j in range(1, numberOfStates - 1):
	# 	currentRow = []
	# 	for i in range(0, 26):
	# 		currentState = firstRow[i]
	# 		if pattern[j] == chr(i + 65):
	# 			nextState = j + 1
	# 			currentRow.append(nextState)
	# 		else:
	# 			currentRow.append(currentState)
	# 	deltaMatrix.append(currentRow)

	# a  = []
	# for i in range(0, 26):
	# 	if pattern[0] == chr(i + 65):
	# 		a.append(1)
	# 	else:
	# 		a.append(0)
	# deltaMatrix.append(a)

	# print(ord(word[0]) - 65)
	




	

		#else:
		#	deltaMatrix[0][i] = 0

	#for ch in pattern
#	a = 97
#	print(chr(a))