import random

guessesTaken = 0
number = random.randint(1, 20)

print('Hello, what is your name?')
playerName = input()

print('Well, ' + playerName + ', I am thinking of a number between 1 and 20.')

for i in range(6):
	print('Take a guess.')
	guess = input()
	guess = int(guess)
	guessesTaken = guessesTaken + 1

	if guess < number:
		print('Your guess is too low.')
	if guess > number:
		print('Your guess is too high.')
	if guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken)
	print('Good job, ' + playerName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
	number = str(number)
	print('Nope, the number I was thinking of was ' + number + '.')
