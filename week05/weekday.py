# A Program that outputs whether or not today is a weekday
# Author: Olga Kreicberga 

# For this challenge need to import pandas function 
import pandas as pd 
  
# Function to check which day is entered, work or day off  
def check_weekday(date): 
     # input pandas function 'pandas.bdate_range' witch Return a fixed frequency DatetimeIndex, 
     # with business day as the default frequency.  
    res=len(pd.bdate_range(date,date)) 
      
    if res == 0 : 
        print("It is the weekend, yay!") 
    else: 
        print("Yes, unfortunately today is a weekday.")  
       
# Enter date  
date =  (input("Enter the date: "))
    
check_weekday(date) 
