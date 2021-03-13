# A program that asks the user to input any positive integer and outputs the successive values 
# of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, 
# divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

# Firs part - input data. 
# Int- for whole numbers; \n - new line 
number=int(input('Enter number:\n'))

# Add function collatz - program at each step calculate  the next value by taking a current value
def collatz(number):
# Enter loop
    while number !=1: 
        # program end if the value is one
        if number % 2==0:
            # if number is even divide it by two 
            number= number//2
            print(number)
        # If the next value is odd, than multiply it by three and add one
        else: 
            number= 3 * number + 1
            print (number)

collatz(number)