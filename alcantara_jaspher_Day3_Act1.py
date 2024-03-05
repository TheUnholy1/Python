name = input("Name: ")
math = float(input("Math: "))
science = float(input("Science: "))
english = float(input("English: "))

average = (math + science + english) / 3

print("Average: ", average)

if average >= 75:
    print("Congratulations You passed the semester")
    if (average >= 75 and math < 75):
        print("But You need to Re-enroll Math subject")
    if (average >= 75 and science < 75):
        print("But You need to Re-enroll Science subject")
    if (average >= 75 and english < 75):
        print("But You need to Re-enroll English subject")
else:
    print("Sorry, You failed the semester.")
