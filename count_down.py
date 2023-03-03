# This function should count down by -2 from 11 to 1, so that it only
# prints odd numbers. 

# This range(11, -2) tells the for loop to start at 11 and end at index
# position -2 (which corresponds to the numeric value of -1). Since the
# third incremental or decremental value is missing, the loop will 
# increment by the default of +1 instead of the intended -2 decrement.
# Starting at index position 11 and incrementing by +1 will end the loop 
# automatically, because the index is not counting down towards -2 as 
# the end of the range. 

# To fix this problem, the range() needs three parameters:
# First parameter should be the starting index position of 11.
# Second parameter should be the ending index position of 0 (value 1).
# Third parameter should be decrementing by -2.
# So, the range should be configured as range(11, 0, -2).

# Fix this loop with the corrected range parameters and click Run.
for n in range(11,0,-2):
    if n % 2 != 0:
        print(n, end=" ")
        

# Should print: 11, 9, 7, 5, 3, 1 once the problem is fixed.

print()


number = 15 # Initialize the variable
while number >= 5: # Complete the while loop condition
    print(number, end=" ")
    number -= 5 # Increment the variable

# Should print 15 10 5 