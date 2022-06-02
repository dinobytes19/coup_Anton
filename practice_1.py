# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:45:33 2022

@author: Anton Mournstone
"""

"""
Objectives:
    - Understand what the terminal is and how to run a written python program
    - Understand basic usage of random numbers
    - Understand basic string parsing
    - Understand basic file input and out with open() and .close()
    - Understand how to build a class
    - Understand how to build and parse a text file
    - Programming philosophy: Understand defensive programming
"""

"""
Instructions:
    - Copy this whole file into your own directory
    - Remove the instructor's name from the top and place your name
        - do the same with creation date
    - Follow the problem specifications that follow and make a python
      document that can run without any errors
    - If you want some extra practice, proceed to the extra practice document
"""

# Problem 1
# Print a random whole number in the range of [1,10] (inclusive)
import random
print (random.randint(1,10))

# Problem 2
# Print all of the perfect squares in the range of [1,10000]
# Note: you should use a loop (100 print statements will get you 0 points),
#       but you don't have to use 'for i in range(10000)' as your statement
a = 0
while(a< 100):
    a = a + 1
    print(a, "squared is", a*a)
# Problem 3
# Open the file `abab.txt` and print the total number of times the character
# 'b' appears in the file
# This shouldn't be hard-coded. You should be printing from a variable!
# Don't forget to close the file when you're done!
# Note: you're allowed to look at how the file was generated if you want
abab_file = open("abab.txt", 'r')
print(abab_file.read())
b_count = 0
for character in "abab_file":
    if (character == "b"):
        print ("B count is", b_count)
        b_count = b_count + 1
    
abab_file.close()
# Problem 4
# Open the file `abab.txt` and print the following:
    # the longest sequence of 'a's in the file
    # the longest sequence of 'b's in the file


