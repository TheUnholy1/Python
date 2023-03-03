# For this example, the outer for loop uses an end of range index of 
# 10. The value of index 10 will be 10-1, or 9.  
for outer_loop in range(10):

    # Using the "outer_loop" variable as the end of range for the  
    # inner loop, means the end of range index will be 9. The value 
    # of index 9 will be 9-1, or 8.
    for inner_loop in range(outer_loop):

        # The printed result is the value of "inner_loop". Since  
        # there aren’t any calculations in this loop, there is a 
        # simple shortcut for solving what the final value printed 
        # by the "inner_loop" will be. The solution is to simply use 
        # the value of the "inner_loop" index, which is 8.
        print(inner_loop)