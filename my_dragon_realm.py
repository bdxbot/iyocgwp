import random, time, sys

gold = 0

while True:
	print('You are in a land full of dragorgons. In front of you,you see')
	print('two caves. In one cave, the dragorgon is friendly and will share his')
	print('treasure with you. The other dragorgon is greedy and hungry, and will')
	print('eat you on sight.\n')
	print('You have %s gold pieces.\n' % gold)
	print('Your options are NORTH, WEST, or QUIT.')

	caveAlignment = random.randint(1, 2)

	print('Which cave will you enter?: ')
	caveChoice = input()
	caveChoice = caveChoice.lower()
	print(caveChoice)

	if caveChoice == 'q' or caveChoice == 'quit':
		print('You can test your luck some other day...')
		sys.exit()

	print('You approach the cave...')
	time.sleep(1.5)
	print('It is dark and spooky...')

	if caveAlignment == 1:
		print('The dragorgon is greedy. He roasts you with his fire breath.')
		print('You have died.')
		print('The dragorgon adds your %s gold pieces to his treasure.' % gold)
		gold -= gold
	elif caveAlignment == 2:
		print('The dragorgon is friendly and shares his treasure with you.')
		print('You recieve 100 gold pieces.')
		gold += 100

	playAgain = input('Would you like to continue? (YES or NO): ')
	playAgain = playAgain.lower()

	if playAgain == 'n' or 'no':
		print('You retreat to your home with %s' % gold)
		print('You can test your luck some other day...')
		sys.exit()
	elif playAgain == 'y':
		continue
