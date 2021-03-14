# Program that reads in a text file and outputs the number of e's it contains.
# Author: Olga Kreicberga 


# We create a variable 'y' and  function input - it will ask the user to input any letter
# this function also makes it possible not to rewrite the code if a different value will set
# 

x = 0
y=input("Enter a letter:") 
# Here we open txt file in read mode (I put only first Chapter of Moby Dick in txt file)
with open("moby-dick.txt", 'r') as f:
    for line in f: # to read each line in the file
        words = line.split() # to spleat 
        for i in words: # the loop searches for words
            for letter in i: # the loop searches for letters
                # if the letter that was requested from the user 
                # is fixed during the search, then the value is increased
                if(letter==y): 
                    x=x+1
# The total is printed 
print(x)