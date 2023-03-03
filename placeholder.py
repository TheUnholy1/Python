print("\nformat Method\n")
def student_grade(name, grade):
	return "{name} recieved {grade}% on the exam".format(name=name,grade=grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

#easy way

def student_grade(name, grade):
	return "{} recieved {}% on the exam".format(name,grade)

print(student_grade("Mark", 75))
print(student_grade("Mia", 92))
print(student_grade("Jesse", 50))

# print 2 decimals

price = 7.5
with_tax = price * 1.09
print("Base Price: ${:.2f}. With Tax: ${:.2f}".format(price,with_tax))

def convert_distance(miles):
    km = miles * 1.6 
    result = "{} miles equals {:.2f} km".format(miles,km)
    return result


print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km


#format using placeholder 0 and 1 etc
first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

#using index slicing
def nametag(first_name, last_name):
    return("{} {}.".format(first_name,last_name[0]))


print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 

