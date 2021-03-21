# Program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 
# in the range [0, 4] on the one set of axes.
# Author: Olga Kreicberga 


import numpy as np 
import matplotlib.pyplot as plt 

# We must first set a grid of coordinates to construct a function chart
fig = plt.subplots()
# We have to define the areas on which we will plot the function
# Lincpace creates an array with a lower bound of 0 and an upper bound of 4, 
# creating 100 elements
x = np.linspace(0, 4, 100)


# make a functions
f= x 
g= x * x 
h= x * x * x 

# make a plots with labels for each function
plt.plot (x , f, label="f(x)=x") 
plt.plot (x , g, label="g(x)=x2") 
plt.plot (x , h, label="h(x)=x3") 
# # make a Title, LAbels for Axis, the Legend
plt.title("Plot of Functions")
plt.xlabel("X Asis")
plt.ylabel("Y Asis")
plt.legend()
# Safe a plot for image fail 
plt.savefig('plottask.png')
plt.show ()

