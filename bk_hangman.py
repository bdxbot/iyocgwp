import random

# create a list with all images for reaper
REAPER = ['''
	=====''', '''
	  O
	=====''', '''
	  O
	  |
	=====''', '''
	  O
	 /|
	=====''', '''
	  O
	 /|\\
	=====''', '''
	  O
	 /|\\
	 /
	=====''', '''
	  O
	 /|\\
	 / \\
	=====''', '''
	  O - GAME OVER
	 (|)
	 / \\
	====='''
]

# create a variable 'words', assign a long string to it BUT using the .split()
# function turns 'words' from a variable to a list. each space between words
# creates a new element in the list.
words = 'ant baboon badger bat bear beaver camel cat calm cobra cougar coyote \
crow deer dog donkey dragon duck dwarf eagle elf ferret fox frog goat goose \
hawk lion lizard llama mole monkey moose mouse mule newt orc otter owl panda \
parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk \
sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf \
wombat zebra'.split()

#!print(words)

def getRandomWord(wordList):
	# this function returns a random string from the list that is passed to it
	#!print(wordList)
	#!print(len(wordList))
	#!print(len(wordList) - 1)
	
	# this creates a variable 'wordIndex' and assigns it a random integer between
	# 0 and the length of wordList which is fed to the function when called, -1.
	# len(list) returns how many elements are in a list.
	wordIndex = random.randint(0, len(wordList) - 1)
	#!print(wordIndex)

	# the function then returns a random element from the list it was fed by taking
	# the random number assigned to wordIndex and using that to specify what element
	# from the list we want. ie wordList[24].
	return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
	# this function displays the current state of the game and takes three arguments
	# this prints the current REAPER image by taking the length of missedLetters
	# and using that integer to call the matching REAPER list element.
	print(REAPER[len(missedLetters)])
	print()

	# this takes the len of the secretWord argument fed to the function, multiplies
	# the _ by that and assigns it to the variable 'blanks'
	# ie secretWord = kitten, len(secretWord) = 6, _ * 6 = _ _ _ _ _ _ (w/ no spaces)
	blanks = '_' * len(secretWord)

	for i in range(len(secretWord)): # replaces blanks with correctly guessed letters
		if secretWord[i] in correctLetters:
			blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

	for letter in blanks: # show the secret word with spaces in between each letter
		print(letter, end = ' ')
	print()

	print('Missed letters:', end = ' ')
	for letters in missedLetters:
		print(letters, end = ' ')
	print()

def getGuess(alreadyGuessed):
	# returns the letter the player entered. this function makes sure the player
	# entered a single letter and not something else.
	while True:
		print('Guess a letter.')
		guess = input()
		guess = guess.lower()
		if len(guess) != 1:
			print('Please enter a single letter only.')
		elif guess in alreadyGuessed:
			print('You have already guessed that letter. Choose a different letter')
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print('Please enter a LETTER.')
		else:
			return guess

def playAgain():
	# this function returns True if the player wants to play again, otherwise
	# it returns False
	print('Do you want to play again (yes or no)?')
	return input().lower().startswith('y')

#==================== PROGRAM STARTS HERE YO ====================#
print('R E A P E R')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
#!secretWord = 'apple'
gameIsDone = False

#!print(secretWord)

while True:
	displayBoard(missedLetters, correctLetters, secretWord)

	# let the player enter a letter
	guess = getGuess(missedLetters + correctLetters)

	if guess in secretWord:
		correctLetters = correctLetters + guess

		# check if the player has won
		foundAllLetters = True
		for i in range(len(secretWord)):
			if secretWord[i] not in correctLetters:
				foundAllLetters = False
				break
		if foundAllLetters:
			print('You guessed it! The secret word is "' + secretWord + '"! '
				'You have won!')
			gameIsDone = True
	else:
		missedLetters = missedLetters + guess

		# check if player has guessed too many times and lost
		if len(missedLetters) == len(REAPER) - 1:
			displayBoard(missedLetters, correctLetters, secretWord)
			print('You have run out of guesses!\nAfter ' +
				str(len(missedLetters)) + ' missed guesses and ' +
				str(len(correctLetters)) + ' correct guesses, '
				'the word was "' + secretWord + '."')
			gameIsDone = True

	# ask the player if they want to play again (but only if the game is done)
	if gameIsDone:
		if playAgain():
			missedLetters = ''
			correctLetters = ''
			gameIsDone = False
			secretWord = (getRandomWord(words))
		else:
			break