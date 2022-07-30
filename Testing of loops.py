# While Loop Experiments
#prints all elements inside the string
#a = ["ass","poop","shit"];

#for i in a:
   # print(i)
#-------------------------------------------------------------------------------
# print total of a string
#a = [20,10,5]
#total = 0 

#for num in a:
   # total = total + num
#print(total)

#--------------------------------------------------------------------------------
#print total of a string using range
#Total = 0
#for i in range(1,5):
 #   Total += i
#print(Total)
#-----------------------------------------------------------------------------------

#add all odd numbers in a list

#total = 0

#for i in range(1,15):
 #   if i%2==1:
  #      total += i
#print(total)

#----------------------------------------------------------------------------------
# add multiples of 3 and 5 that are under 100
#total = 0
#for i in range (1,100):
    #if i%3 == 0 and i % 5 == 0:
       # total += i
#print(total)

#-----------------------------------------------------------------------------------

# While loops experiments
# print all numbers from 1 to 4
#total = 0
#j = 1

#while j < 5:
#    total += j
#    j += 1

#print(total)

#------------------------------------------------------------------------------------

#print the total positive numbers in an ordered list

#list = [5,4,4,3,1,-2,-3,-5]

#total = 0
#i = 0

#while list[i] > 0:
   # total += list[i]
   # i += 1
#print(total)

#-------------------------------------------------------------------------------------
# add all multiples of both 3 or 5

#total = 0
#for i in range(1,100):
 #   if i %3 == 0 or i %5 == 0:
  #      total += i
#print(total)

#--------------------------------------------------------------------------------------
# print the total of all positive numbers from a tuple

#tuple = (5,-1,-3,-5,6,7,9,3,2)
#total = 0
#i = 0
#a = list(tuple)
#a.sort(reverse= True)

#while a[i] > 0:
 #   total += a[i]
 #   i += 1
#print(total)

#--------------------------------------------------------------------------------------

#print the total of all numbers in a list

#1.) Using for loop
#total = 0


#list= [5,4,3,4,1]

#for i in list:
 #   total += i
#print(total)

#2.) using while loop

#list = [5,4,4,3]

#total = 0
#i = 0

#while i < len(list) and list[i] > 0:
 #   total += list[i]
 #   i += 1
#print(total)

#---------------------------------------------------------------------------------------
# print all positive elements using for loop

#list = [1,2,4,5,3,-1,-2,-3]
#total = 0 

#for i in list:
#   if i <=0:
#      break
#   total += i

#print(total)

#---------------------------------------------------------------------------------------

#print all positive elements using while loop
#list = [1,2,4,5,3,-1,-2,-3]

#total =0
#i =0

#while True:
   #total +=list[i]
   #i +=1
   #if list[i] <0:
   #   break
#print(total)

#-----------------------------------------------------------------------------------------
# adding all negative numbers in a list
#list = [7,5,-3,4,3,1,-2,-3,-5,-7]

#total =0

#for i in list:
#   if i < 0:
#      total += i
#print(total)

#-----------------------------------------------------------------------------------------
#print numbers using while loop                
#j = 1
#while j<=10:
#   print(j)
#   j +=1

#-------------------------------------------------------------------------------------
#print numbers using for loop
#for i in range (1,11):
#   print(i)

#--------------------------------------------------------------------------------------
#input elements with restrictions using for loop and turn it into a list
#list=[]
#print("Enter 5 elements: ",end='')
#for i in range(0,5):
#    ele=int(input())
#
#    list.append(ele)
#print(list)

#--------------------------------------------------------------------------------------
#create multiplication table using for loop
#def print_table():
#    n = int(input("Enter number: "))
#    for i in range(1,11):
#        print(n,'x''=',n*i)

#print_table()

#---------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------------------------


