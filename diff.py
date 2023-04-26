# differentiation
import random


# make function to differentiate equation
def diff(first, second, third):
    first = first*2
    third=0
    return "{}x + {}".format(first, second)


# generate numbers here
num1 = random.randint(1, 9)
num2 = random.randint(1, 9)
num3= random.randint(1, 9)


# remove 1-coefficient 
if num1 == 1 or num2 == 1:
    to_show = "{}x^2 + {}x + {}".format(num1, num2, num3)
    print("Differentiate this equation")
    print(to_show.replace("1", ""))

 
else:
    print("{}x^2 + {}x + {}".format(num1, num2, num3))
    print("Differentiate this equation")
    

# get user input and compare
user_input = input("Enter equation here: ").lower()
if user_input != diff(num1, num2, num3):
    print("Incorrect")

else:
    print("Correct")



