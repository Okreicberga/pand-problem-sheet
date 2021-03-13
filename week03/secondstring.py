# A Programm that takes asks a user to input a string 
# Program outputs every second letter in reverse order
# Author: Olga Kreicberga 

# Create first part for input text   
inputString = input ('Please enter a sentence:')
#s = The quick brown fox jumps over the lazy dog. 
# [:: -1] - reverse text with all letters. But as we need output only every second letter, 
# I put [::-2]  
print( inputString[::-2])