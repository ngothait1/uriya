# This is final project which concludes the first part in the course.
import time

flag = True #for not print the resuly if division by zero

print("Hello, This is my final project")
user_name = input("What is your name? ")

print("Hi " + user_name + ", nice to meet you")
print("This is a special calculator, I would need two numbers from you")

num_1 = int(input("First number >>> "))
num_2 = int(input("Second number >>> "))

#check if even or odd
if_even_1 = "odd"
if num_1 % 2 == 0:
    if_even_1 = "even"

if_even_2 = "odd"
if num_2 % 2 == 0:
    if_even_2 = "even"

print("Thank you for putting in your numbers, " + str(num_1) +" and " + str(num_2))
print("I can see that the first number is " + if_even_1)
print("And the second is " + if_even_2)

if if_even_1 == if_even_2:
    if if_even_1 == "even":
        print("So both of them are even")
    else:
        print("So both are odd")
else:
    print("So one of them is even, and one is odd")

#-------
operator = input("Operator (+, -, *, /): ")

exrice = str(num_1) + " " + operator + " " + str(num_2) + " = "

#--------

if operator == "+":
    result = str(num_1 + num_2)

elif operator == "-":
    result = str(num_1 - num_2)
    
elif operator == "*":
    result = str(num_1 * num_2)

elif operator == "/": 
    intORfloat =  input("You chose division, should the result be integer? (y/n) ")
    
    # check if divesion by zero
    if num_2 == 0:
        print("Error: num_2 is zero")
        print("An error had occured, please try again")
        flag = False

    elif intORfloat == "y":
        result = str(int(num_1 / num_2))
    elif intORfloat == "n":
        result = str(num_1 / num_2) 
 
if flag:
    print(exrice + result)

print("Thank you " + user_name + " for using the calculator on " + time.ctime())

# The end