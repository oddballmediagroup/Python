"""
program: randomGuess.py
autyhor anthoiny graffeo
exercise on 90-91

program promts the user to enter in two values for a numeric range. program randomly picks a number in that range. user enters their own guess.program will let the user know if the guess is too high, too low or a match. program will also keep track of hte # of attempts.

"""

#import the random module so we can use randit()
import random

# constants and variables
attempts = 0

# input phase
smallNum = int(input("Please enter the smallest value for the range>>"))
largeNum = int(input("Please enter the largest value for the range >>"))

# calculation phase
# Program will randomly generate a number in that range
magicNum = random.randint(smallNum, largeNum)

#Loop which contains the game mechanics 
while True:
	userNum = int(input("Enter your guess >>"))
	attempts += 1
	if userNum < magicNum:
		print ("Too low, try again!")
	elif userNum > magicNum:
		print("Too high,Try again!")
	else:
		print("Congratulations! You got in " + str(attempts) + "tries")
		break