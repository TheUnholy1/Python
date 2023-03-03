#def factorial(n):
#    print(n)
#    if n < 2: # factorial of 1 and 0 is 1
#        return 1 
#    return n *  factorial(n-1)
#print(factorial(5)) #this will call the function and print it

def factorial(n):
    
    print("Factorial Called with "+str(n))
    
    if n < 2:
        print("Returning 1")
        return 1
    
    result = n * factorial(n-1)
    print("Returning "+str(result)+" for factorial of "+str(n))
    return result

factorial(6)