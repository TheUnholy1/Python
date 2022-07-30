# to take input from the user
# num = int(input("Enter a number: "))
num = 7


def juju(x):

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return x * juju(x - 1)

# change the value for a different result


# call the factorial function
result = juju(num)


print("The factorial of", num, "is", result)
#nice