import random

def display_board():
	print('\n{:^3}|{:^3}|{:^3}'.format(board['tl'], board['tm'], board['tr']))
	print('-' * 11)
	print('{:^3}|{:^3}|{:^3}'.format(board['ml'], board['mm'], board['mr']))
	print('-' * 11)
	print('{:^3}|{:^3}|{:^3}\n'.format(board['bl'], board['bm'], board['br']))

def player_turn():
	global player_move
	valid_moves = []
	move_check = True

	while move_check == True:
		player_move = input('Make your move: ')
		#### Check if move is a valid one and if location is empty
		# First grab all current key/value pairs in the board
		for key, val in board.items():
			# If value is an empty string then it is a valid placement
			if val == '':
				# Place all valid placements (keys w/ empty strings as values) into a list
				valid_moves.append(key)
		# Check if player move is a valid move, otherwise force player to try another move
		if player_move in valid_moves:
			move_check = False
			return player_move
		else:
			print('That is not a valid move!')

def computer_turn():
	### Check board status to determine what spots are available
	global comp_move
	# Get dictionary entries and check where x and o are
	valid_moves = []
	for key, val in board.items():
		# If value is an empty string then it is a valid placement
		if val == '':
			# Place all valid placements into a list
			valid_moves.append(key)
	# Generate random number to pick random spot
	num = random.randint(0, len(valid_moves) - 1)
	comp_move = valid_moves[num]

	return comp_move

def token_placement(move, token):
	if move == 'tl' or move == 7:
		board['tl'] = token
	elif move == 'tm' or move == 8:
		board['tm'] = token
	elif move == 'tr' or move == 9:
		board['tr'] = token
	elif move == 'ml' or move == 4:
		board['ml'] = token
	elif move == 'mm' or move == 5:
		board['mm'] = token
	elif move == 'mr' or move == 6:
		board['mr'] = token
	elif move == 'bl' or move == 1:
		board['bl'] = token
	elif move == 'bm' or move == 2:
		board['bm'] = token
	elif move == 'br' or move == 3:
		board['br'] = token
	else:
		print('That is not a valid move!')

def winner_check(token):
	global game_over
	# Return all keys that have value X
	move_list = []
	# Compare keys to win conditions, if match declare winner, if no match exit
	for key, val in board.items():
		if val == token:
			move_list.append(key)

	if move_list == ['tl', 'tm', 'tr']:
		print('Hahaha, you a winner!')
		game_over = True
	elif move_list == ['ml', 'mm', 'mr']:
		print('Hahaha, you a winner!')
		game_over = True
	elif move_list == ['bl', 'bm', 'br']:
		print('Hahaha, you a winner!')
		game_over = True
	elif move_list == ['tl', 'ml', 'bl']:
		print('Hahaha, you a winner!')
		game_over = True
	elif move_list == ['tm', 'mm', 'bm']:
		print('Hahaha, you a winner!')
		game_over = True
	elif move_list == ['tr', 'mr', 'br']:
		print('Hahaha, you a winner!')
		game_over = True
	elif move_list == ['tl', 'mm', 'br']:
		print('Hahaha, you a winner!')
		game_over = True
	elif move_list == ['tr', 'mm', 'bl']:
		print('Hahaha, you a winner!')
		game_over = True
	#print('Oooooh, you a loser!')

	return game_over

# ---------- START THE PROGRAM DAWG ----------
game_over = False
player_token = ''
comp_token = ''
player_move = ''
comp_move = ''

### Create the board by using a dictionary and placing the player's letter 
### placements from move_list
board = {"tl": '', "tm": '', "tr": '',
"ml": '', "mm": '', "mr": '',
"bl": '',"bm": '', "br": ''}

### Start game loop!
while game_over != True:
	### Ask player if they want to be X or O
	# You must use AND instead of OR!
	# AND returns True if both statements are true
	# OR returns True if one of the statements is true
	# OR means if player_token equals X or O, continue the while loop. So if the player
	# picks X or O, one of the statements will always be true.
	# AND means if player_token does not equal X and it does not equal O, continue 
	# the while loop.
	while player_token != 'X' and player_token != 'O':
		player_token = input('Would you like to be X or O?: ')
		player_token = player_token.upper()
		if player_token == 'X':
			comp_token = 'O'
			print('You will go first!')
			display_board()
			player_turn()
			token_placement(player_move, player_token)
			break
		else:
			comp_token = 'X'
			print('The computer will go first!')
			computer_turn()
			token_placement(comp_move, comp_token)
			display_board()
			break

	### Player places a token
	player_turn()
	token_placement(player_move, player_token)
	### Display board
	display_board()
	### Check if three in a row, if not continue
	winner_check(player_token)
	### Check if board is full, if not continue

	### Computer places a token
	computer_turn()
	token_placement(comp_move, comp_token)
	### Display board
	display_board()
	winner_check(comp_token)

cont = input('Would you like to play again (Y/N)?: ')
cont = cont.upper()

if cont == 'Y':
	print('Figure out how to continue dummy!')
else:
	exit('Thanks for playing, goodbye!')