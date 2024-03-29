# Tic-Tac-Toe

import random

def drawBoard(board):
	# This function prints out the board that it was passed

	# "board" is a list of 10 strings representing the board (ignore index 0)
	print(board[7] + '|' + board[8] + '|' + board[9])
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-+-+-')
	print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
	# Lets the player type which letter they want to be
	# Retruns a list with the players letter as the first item and the computers
	# letter as the second
	letter = ''
	while not (letter == 'X' or letter == 'O'):
		print('Do you want to be X or O?')
		letter = input().upper()
	# The first element in the list is the player's letter, second is the
	# computers letter
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']

def whoGoesFirst():
	# Randomly choose which player goes first
	if random.randint(0, 1) == 0:
		return 'computer'
	else:
		return 'player'

def makeMove(board, letter, move):
	board[move] = letter

def isWinner(bo, le):
	# Given a board and a players letter, this function returns True if that
	# player has won
	# We use bo instead of board and le instead of letter so we dont have to
	# type as much
	return ((bo[7] == le and bo[8] == le and bo[9] == le) or # Across the top
	(bo[4] == le and bo[5] == le and bo[6] == le) or # Across the middle
	(bo[1] == le and bo[2] == le and bo[3] == le) or # Across the bottom
	(bo[7] == le and bo[4] == le and bo[1] == le) or # Down the left side
	(bo[8] == le and bo[5] == le and bo[2] == le) or # Down the middle
	(bo[9] == le and bo[6] == le and bo[3] == le) or # Down the right side
	(bo[7] == le and bo[5] == le and bo[3] == le) or # Diagonal
	(bo[9] == le and bo[5] == le and bo[1] == le)) # Diagonal

def getBoardCopy(board):
	# Make a copy of the board list and return it
	boardCopy = []
	for i in board:
		boardCopy.append(i)
	return boardCopy

def isSpaceFree(board, move):
	# Return True if the passed move is free on the passed board
	return board[move] == ' '

def getPlayerMove(board):
	# Let the player enter their move
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
		print('What is your next move? (1-9)')
		move = input()
	return int(move)

def chooseRandomMoveFromList(board, movesList):
	# Returns a valid move from the passed list on the passed board
	# Returns None if there is no valid move
	possibleMoves = []
	for i in movesList:
		if isSpaceFree(board, i):
			possibleMoves.append(i)

	if len(possibleMoves) != 0:
		return random.choice(possibleMoves)
	else:
		return None

def getComputerMove(board, computerLetter):
	# Given a board and the computer's letter, determine where to move and
	# return that move
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	## Here is the algorithm for our Tic-Tac-Toe AI:
	# First check if we can win in the next move
	for i in range(1, 10):
		boardCopy = getBoardCopy(board)
		if isSpaceFree(boardCopy, i):
			makeMove(boardCopy, computerLetter, i)
			if isWinner(boardCopy, computerLetter):
				return i

	# Check if the player could win on their next move and block them
	for i in range(1, 10):
		boardCopy = getBoardCopy(board)
		if isSpaceFree(boardCopy, i):
			makeMove(boardCopy, playerLetter, i)
			if isWinner(boardCopy, playerLetter):
				return i

	# Try to take a corner if it is free
	move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
	if move != None:
		return move

	# Try to take the center if it is free
	if isSpaceFree(board, 5):
		return 5

	# Move on one of the sides
	return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
	# Return True if every space on the board has been taken otherwise return False
	for i in range (1, 10):
		if isSpaceFree(board, i):
			return False
	return True

### This is the start of the actual program
print('Welcome to Tic-Tac-Toe!')

while True:
	# Reset the board
	theBoard = [' '] * 10
	## MINE: inputPlayerLetter() returns a two element array, either ['X', 'O'] or ['O', 'X']
	## MINE: These will get assigned to playerLetter and computerLetter respectively
	playerLetter, computerLetter = inputPlayerLetter()
	turn = whoGoesFirst()
	print('The ' + turn + ' will go first.')
	gameIsPlaying = True

	while gameIsPlaying:
		if turn == 'player':
			# Players turn
			## MINE: draw the current board
			drawBoard(theBoard)
			## MINE: collect the players move. as long as its a valid choice (1-9)
			## MINE: and is free by checking isSpaceFree(). this function returns
			## MINE: the players valid move
			move = getPlayerMove(theBoard)
			## MINE: this makes the actual move by feeding the function the 
			## MINE: current board, playerLetter, and the move the player just chose.
			## MINE: the function assigns theBoard[move] = playerLetter
			makeMove(theBoard, playerLetter, move)

			## MINE: check if there is a winner by feeding the function the current
			## MINE: board and the player letter. the function checks if there
			## MINE: are three of the same letters in the board array
			if isWinner(theBoard, playerLetter):
				## MINE: if there is a winner, draw the board, congrat the player and quit the game
				drawBoard(theBoard)
				print('Hooray! You have won the game!')
				gameIsPlaying = False
			else:
				## MINE: if the player did not win, check if the board is full
				## MINE: if it is, the game is a tie and break out of the while loop
				## MINE: and ask the player if they want to play again
				## MINE: if it isnt, its now the computers turn
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('The game is a tie!')
					break
				else:
					turn = 'computer'

		else:
			# Computers turn, this works similarly to the players turn
			move = getComputerMove(theBoard, computerLetter)
			makeMove(theBoard, computerLetter, move)

			if isWinner(theBoard, computerLetter):
				drawBoard(theBoard)
				print('The computer has beaten you! You lose!')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('The game is a tie!')
					break
				else:
					turn = 'player'

	print('Do you want to play again? (yes or no)')
	if not input().lower().startswith('y'):
		break