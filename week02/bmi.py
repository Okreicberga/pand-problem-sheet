# Calculate body max index by a weihgt devide height
# Author: Olga Kreicberga 

# Program will calculate the BMI in KG and Meters 
# Need to convert the input string to float for calculations 

height = float(input("Input your height in cm: "))
weight = float(input("Input your weight in kilogram: "))

# Made changes to calculate BMI in KG and Centimeters 
BMI = weight /(height/100)**2
# Format BMI for print two decimilars {:.2f} 
print("BMI is {:.2f}".format(BMI)) 