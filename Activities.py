#Activitiy 1 3/4/22

#print("\"Changing the values of three numbers and calculated the average\"")
#print()
#num1 = float(input("\tEnter the First Number: "))
#num2 = float(input("\tEnter the Second Number: "))
#num3 = float(input("\tEnter the Third Number: "))
#Average = (num1+num2+num3)/3
#print()
#ave = "{:.2f}".format(Average)
#print("\tFirst number is: ",num1)
#print("\tSecond number is: ",num2)
#print("\tThird number is: ",num3)

#print('\n')
#print("The average is: ",ave)
#---------------------------------------------------------------

#Activity 2 3/18/22
#  Enter 5 elements and print it 4 different times

#List = []
#Elements = int(input("Enter Number of Elements: "))

#for i in range(Elements):
 #   x = str(input())
 #   List.append(x)
#print("Elements are:",List)
#List.reverse()
#print(List)
#List.sort(key=str.lower)
#print(List)
#del List[2]
#List.sort(key=str.lower)
#print(List)
#List2 = List
#print(List + List2)

#---------------------------------------------------------------------

#Quiz 2 4/01/22
#Enter a positive number and get its factorial
#Jaspher Alcantara BSIT 1-1


#num1=int(input("Please enter a number: "))
#factorial =1

#if num1 <= 0:
   # print("Please Enter Positive Number Only!!!")
#else:
  #  for i in range(1, num1+1):
   #     factorial = factorial * i
  #  print("Positive Number - the factorial of " ,num1, "is",factorial,)

#---------------------------------------------------------------------------------
#Activity #3 4/11/22
#Create a python file that uses a Python Function


#def hello(first_name, last_name):
#    print(f"Hi {first_name} {last_name}.Good Morning!")


#hello("Jaspher", "Alcantara")

#------------------------------------------------------------------------------------
# ACTIVITY 2 4/22/22
#create a program that display  a random number from 1-100 and create a program that would shuffle a list
#must include user defined and built in functions
#import random
#def randomgame():
#    number = random.randint(1,100)
#    num1=float(input("Please guess the random number from 1 - 100: "))
#    if num1 == number:
#        print("Congratulations! You guessed the right number")
#   else:
#        print("Wrong Number,The correct number is:", number)
#    print("\n")
#    strings = input("Enter Five Elements Separated by spaces: ")
#    strings = strings.split()
#    print(strings)
#    random.shuffle(strings)
#    print(strings)
#randomgame()

#------------------------------------------------------------------------------------
#final version of activity 2 4/24/22
#import random
#def randomgame():
#  number = random.randint(1,100)
#  num1=float(input("Please guess the random number from 1 - 100: "))
#  if num1 == number:
#     print("Congratulations! You guessed the right number")
#  else:
#    print("Wrong Number,The correct number is:", number)
#
#  print("\n")
#  list = []
#  print("Enter 5 elements:")
#  for i in range (5):
#    strings=int(input())
#    list.append(strings)
#  print(list)
#  random.shuffle(list)
#  print(list)
#randomgame()

#-----------------------------------------------------------------------------------------
# ACTIVITY #3 CREATE A USER DEFINED FUNCTION THAT INCLUDES MATH OR TRIGONOMETRIC FUNCTIONS
#4/25/22
#import math
#def trigofunc():
#    print("----------Convert Numbers to its Trigonometric Values----------")
#    x = int(input("Enter the number you want to convert: "))
#    print("The value of sine of",x, " is: ",end='')
#    print(math.sin(x))
#    print("The value of cosine of",x, " is: ", end='')
#    print(math.cos(x))
#    print("The value of tangent of", x, " is: ", end='')
#    print(math.tan(x))
#    print("----------Enter Numbers from -1 to 1 to get Inverse Values----------")
#    x = int(input("Enter the number you want to convert: "))
#    print("The value of arc sine of", x, " is: ", end='')
#    print(math.asin(x))
#    print("The value of arc cosine of", x, " is: ", end='')
#    print(math.acos(x))
#    print("The value of arc tangent of", x, " is: ", end='')
#    print(math.atan(x))
#trigofunc()

#----------------------------------------------------------------------------------------
# better version of the act its linted
#import math


#def trigofunc():

#    print("----------Convert Numbers to its Trigonometric Values----------")
#    x = int(input("Enter the number you want to convert: "))
#    print("The value of sine of", x, " is: ", end='')
#    print(math.sin(x))
#    print("The value of cosine of", x, " is: ", end='')
#    print(math.cos(x))
#    print("The value of tangent of", x, " is: ", end='')
#    print(math.tan(x))
#    print("----------Enter Numbers from -1 to 1 to get Inverse Values--------")
#    x = int(input("Enter the number you want to convert: "))
#    print("The value of arc sine of", x, " is: ", end='')
#    print(math.asin(x))
#    print("The value of arc cosine of", x, " is: ", end='')
#    print(math.acos(x))
#    print("The value of arc tangent of", x, " is: ", end='')
#    print(math.atan(x))


#trigofunc()

#---------------------------------------------------------------------------------------
# Create a program using recursion that prints countdown then count up
#print("------------Activity 4------------")
#num = int(input("Enter Number: "))
#def part1(num):
#    print(num, end=' ')
#
#    ber = num - 1
#    if 0 < ber:
#        part1(ber)
#
#part1 (num)
#
#
#def part2(x):
#    print(x, end=' ')
#    y = x + 1
#    if y <= num:
#        part2(y)
#part2(1)

#-----------------------------------------------------------------------------------------
# Better version of Activity #4
#n = int(input("Please Enter A Number: "))


#def part1(n):
#    if 0 < n:
#        print(n, end=' ')
#        part1(n - 1)


#part1(n)


#def part2(x):
#    print(x, end=' ')
#    y = x + 1
#    if y <= n:
#        part2(y)
#
#
#part2(1)
#------------------------------------------------------------------------------------------
# Activity 4 version 3
#n = int(input("Please Enter A Number: "))


#def part1(number):
#    if 0 < number:
#        print(number, end=' ')
#        part1(number - 1)


#part1(n)


#def part2(x):
#    if x <= n:
#        print(x, end=' ')
#        part2(x + 1)

#part2(1)
#--------------------------------------------------------------------------------------
# Activity 4 version 3
#n = int(input("Please Enter A Number: "))


#def part1(number):
#    if 0 < number:
#        print(number, end=' ')
#        part1(number - 1)


#part1(n)


#def part2(x):
#    if x <= n:
#        print(x, end=' ')
#        part2(x + 1)

#part2(1)
#---------------------------------------------------------------------------------------
# Jaspher Alcantara BSIT 1-1 Practical Exam

#def reversal(string1):
#   if len(string1) == 1:
#        return string1
#    else:
#        return reversal(string1[1:]) + string1[0]
    
    
#string1 = input("Enter a String: ")
#string2 = reversal(string1)
#print("Reversed String: "+string2)
#answer = input("Do you want to print again? y/n: ")
#if answer == 'y':
#    def reversal(string1):
#        if len(string1) == 1:
#            return string1
#        else:
#            return reversal(string1[1:]) + string1[0]


#    string1 = input("Enter a String: ")
#    string2 = reversal(string1)
#    print("Reversed String: " + string2)
#    answer = input("Do you want to print again? y/n: ")
#    if answer == 'n':
#        print("Thankyou!")
#    else:
#        print("Please Enter y/n: ")
#else:
#    print("Thankyou!")
#--------------------------------------------------------------------------------
# EXAM 5/16/22
#BMI CALCULATOR
#patients = [[88,1.5], [55,1.9], [73,1.8], [65,1.8], [160,1.7]]
#def bmi_calculator (weight, height):
#    return (weight / (height**2))

#for patients in patients:
#    weight, height = patients
#    BMI = bmi_calculator(weight, height)
#    print("Patient's BMI is:", BMI)

#--------------------------------------------------------------------------------------------
#quiz debug
#create a program that prints the largest number and the total number of a list
#height = [100, 2, 300, 10, 11, 1000]


#def sum_of_numbers(number):
#    total = 0
#    for x in number:
#        total += x
#    return total


#largest_number = height
#for number in height:
#    if number < number:
#        number = number

#print("The largest number is", number)
#print("The sum of the given numbers is", sum_of_numbers(largest_number))
#----------------------------------------------------------------------------------------------------------
