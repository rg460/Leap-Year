# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# How to calculate a Leap year -on every year that is evenly divisible by 4
#    **except** every year that is evenly divisible by 100
#     **unless** the year is also evenly divisible by 400

#Write your code below this line 👇
# Checking if the given year is leap year    
if((year % 400 == 0) or  
     (year % 100 != 0) and  
     (year % 4 == 0)):   
    print(f"{year} is a leap Year");  
  # Else it is not a leap year
else:       
      print (f"{year} Year is not a leap Year")  