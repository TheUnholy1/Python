def factorial(n):
    
    if n < 2: # factorial of 1 and 0 is 1
        return 1 
    return n *  factorial(n-1)


print(factorial(5)) #this will call the function and print it