# Recursion using factorial
# def factorial(x):


#    if x == 1:
#        return 1
#    else:
#        return (x*factorial(x-1))
#
# to take input from the user
# num = int(input("Enter a number: "))
# num = 7
# print("The factorial of", num, "is", factorial(num))
# ---------------------------------------------------------
# Multiplication table
#number = int(input("Enter the number of which the user wants to print the Multiplication table: "))
# We are using "for loop" to iterate the multiplication 10 times
#print("The Multiplication Table of: ", number)
#for count in range(1, 11):
#    print(number, 'x', count, '=', number * count)
#-----------------------------------------------------------------
# create a program that converts minutes to days and years
#minutes = int(input("Please Enter the number of Minutes: "))
#year = minutes // 525600
#remaining_Minutes = minutes % 525600
#day = remaining_Minutes / 1440
#day = round(day)
#print(minutes, " minutes is approximately", year, "years &", day, "days")
#------------------------------------------------------------------------
#factorial not recursion
#def fact(n):

#    f = 1

#    for i in range(1, n+1):
#        f = f * i

#    return f


#x = 7

#result = fact(x)

#print(result)
#------------------------------------------------------------------------------
#def recur_factorial(n):  
#   if n == 1:  
#       return n  
#   else:  
#       return n*recur_factorial(n-1)  
# take input from the user  
#num = int(input("Enter a number: "))  
# check is the number is negative  
#if num < 0:  
#   print("Sorry, factorial does not exist for negative numbers")  
#elif num == 0:  
#   print("The factorial of 0 is 1")  
#else:  
#   print("The factorial of",num,"is",recur_factorial(num))  
#----------------------------------------------------------------------------------
# Python 3 program to find  
# factorial of given number 
#def factorial(n): 
      
    # Checking the number
    # is 1 or 0 then
    # return 1
    # other wise return
    # factorial
#    if (n==1 or n==0):
          
#        return 1
      
#    else:
          
#        return (n * factorial(n - 1)) 
  
# Driver Code 
#num = 5; 
#print("number : ",num)
#print("Factorial : ",factorial(num))
#------------------------------------------------------------------------------
#def factorial(x):
    

#    if x == 1:
#        return 1
#    else:
#        return (x * factorial(x-1))

#num = int(input("ENTER THE NUMBER: "))
#num = 7
#print("The factorial of", num, "is", factorial(num))
#--------------------------------------------------------------------------------
#check if letter is vowel or consonant and check if number is odd or even
#num = int(input("Please Enter a number: "))
#char = input("Please Enter a Character: ")

#if num % 2 == 0:
#    print("Even")
#else:
#    print("Odd")

#if char == 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U':
#    print("Vowel")
#else:
#    print("Consonant")
#------------------------------------------------------------------------------------
#continue yer or no
#while True:
#    print()
#    print("\tDo You want to Continue? Yes or No : ")
#    print()
    
#    print("Hello Again")
#    print()
#    cont = input("Another One? Yes or No: ")
    
#    while cont.lower() not in ("yes", "no"):
#        cont = input("Please Enter Yes or No Only: ")
#    if cont == "no":
#        print()
#        print("Thankyou")
#        break
#----------------------------------------------------------------------------------------------------
