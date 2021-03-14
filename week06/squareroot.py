# program that takes a positive floating-point number as input and outputs an 
# approximation of its square root.
# Author: Olga Kreicberga 

# I use float to Values are specified with a decimal point.
# Function Input -  it will ask the user to Enter a possitive number
num = float(input("Enter a positive number: "))
a = 1.0
# use an infinite loop which will run till a break statement is issued explicitly.
while(1):
	b = a*a
	if  num-0.1 < b < num+0.1 :
		break
	else:
		pass
	a = a + 0.01

#Format a for print one decimilar {:.1f} 
print("\n The Square root of {} is approx. {:.1f}. ".format(num,a))