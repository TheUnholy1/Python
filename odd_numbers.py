def odd_numbers(maximum):
    return_string = ""

    # Set the range to start from 1 and include only odd numbers up to the maximum.
    for num in range(1, maximum+1, 2):

        # Append the odd number and a space to the return string.
        return_string += str(num) + " "

    # Check if the return string is empty, and if so, return a message saying no numbers were displayed.
    if return_string == "":
        return "No numbers displayed"
    else:
        return return_string.strip()  # Removes the final space at the end of the string


print(odd_numbers(6))  # Should be 1 3 5
print(odd_numbers(10)) # Should be 1 3 5 7 9
print(odd_numbers(1))  # Should be 1
print(odd_numbers(3))  # Should be 1 3
print(odd_numbers(0))  # No numbers displayed
