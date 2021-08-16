import os
import random
import time
import sys



#----------Predefined Functions----------#
# Function for clearing the screen. easier to type clear() instead of system('cls') every time you want to clear the screen
def clear(): 
    os.system('cls')

# This allows you to print centered text without having to do print("Hello World!".center(__WIDTH__)). 
# Instead you just do printC("Hello World!") and both return the same output.
def printC(text):
    print(text.center(__WIDTH__))
# same as printC but input instead
def inputC(text):
    return input(text.center(__WIDTH__))

#----------End of Predefined Functions----------#

#----------Predefined consts----------#

__WIDTH__ = os.get_terminal_size().columns # When centering strings type the string then .center(__WIDTH__) EX: "Hello World!".center(__WIDTH__)

#----------End of Predefined consts----------#
