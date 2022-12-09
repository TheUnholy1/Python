num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd Number: "))
num3 = int(input("Enter 3rd Number:"))

if num1 > num2:
    
    if num1 < num3:
        print(num3," is largest")
    else:
        print(num1, " is largest")
    
elif num3 > num2:
    print(num3," is largest")
else:
    print(num2," is largest")
