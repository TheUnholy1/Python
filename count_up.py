for number in range(2,12+1,2):
    print(number)

# Should print:
# 2
# 4
# 6
# 8
# 10
# 12


num1 = 2

while num1 <= 12:
    print(num1,end=" ")
    
    num1 += 2
    
    
    
def count_numbers(first, last):
  # Loop through the numbers from first to last 
  x = first
  while x <= last:
    print()
    print(x)
    x+=1


count_numbers(2, 6) 
# Should print:
# 2
# 3
# 4 
# 5
# 6