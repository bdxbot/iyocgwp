# import random and time modules
import random, time

# create a function called displayIntro
def displayIntro():
	# print some multiline text via three '''
	print('''You are in a land full of dragons. In fron of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon 
	is greedy and hungry, and will eat you on sight.''')

print()

# create a function called chooseCave that will return the value of variable cave
def chooseCave():
	# create a variable called 'cave' and assign an empty string to it
	cave = ''
	# while cave does not equal 1 or 2 loop the following code
	while cave != '1' and cave != '2':
		# print some text
		print('Which cave will you go into (1 or 2)?: ')
		# take the players input and assign it to the variable cave
		cave = input()

	# return the value of cave
	return cave

# create a function called checkCave that takes an argument of choseCave
def checkCave(choseCave):
	print('You approach the cave...')
	time.sleep(2)
	print('It is dark and spooky...')
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	time.sleep(2)

	# create a variable called friendlyCave and assign it a random number between 1 and 2
	friendlyCave = random.randint(1, 2)

	# if the argument given when calling this function choseCave equals the 
	# number picked randomly and assigned to friendlyCave, you win else you lose
	if choseCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print('Gobbles you down in one bite!')

# create a variable called playAgain and assign it the string 'yes'
playAgain = 'yes'

# while variable playAgain equals the string yes or y loop the code
while playAgain == 'yes' or playAgain == 'y':
	# if player says yes to play again, call the displayIntro() function
	displayIntro()
	# create a variable called caveNumber, call the choseCave() function, which
	# will ask the player to chose a cave and return the players answer, which
	# will get assigned to the caveNumber variable
	caveNumber = choseCave()
	# call the checkCave function and feed it the value of caveNumber as an argument
	checkCave(caveNumber)

	# print some text
	print('Do you want to play again (yes or no)?: ')
	# ask the players input and assign it to the playAgain variable, which will
	# end the while loop and run the program again
	playAgain = input()