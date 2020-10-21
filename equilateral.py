"""
Program: equilateral .py
author: george 9/30/2020

Program will prompt the user to enter 3 values representing the lengths of the sides of a triangle. Program will determine based on those values if the triangle is equilateral or not(all 3 sides are not hte same)
"""

while True:
# input phase
	response = int(input("Press 1 to check a triangle, press 2 to quit: "))

	# if the user enters a '2', end the program
	if response == 2:
		print("Thank you for using hte triangle checker. Goodbye...")
		break
	side1 = int(input("Please enter the first slide: "))
	side2 = int(input("Now enter the second slide: "))
	side3 = int(input("Finally, enter the third slide: "))

	# Calculation and output phase
	if side1 == side2 and side2 == side3:
		print("Yes! The triangle IS Equilateral!\n")
	else: 
		print("Sorry, The triangle is NOT Equilateral.\n")