def factorial(n):
    #print(n)
    if n < 2: # factorial of 1 and 0 is 1
        #print("done")
        return n 
    #print("iterate")
    return n *  factorial(n-1)
num1 = int(input("Enter Factorial Number: "))
print(factorial(num1)) #this will call the function and print it
