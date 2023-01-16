import re

phone1 = input("Enter phone number 1: ")
phone2 = input("Enter phone number 2: ")

def check_phone_number(phone_number):
  # The regular expression pattern to match / make the first numbers as 123
  pattern = r"123-\d{3}-\d{4}"
  
  # Use the re.fullmatch() function to check if the phone number
  # matches the pattern
  if re.fullmatch(pattern, phone_number):
    print("Phone number is valid")
  else:
    print("Phone number is not valid")

# Test the function with some phone numbers
check_phone_number(phone1)  # should print "Phone number is valid" if 3-3-4
check_phone_number(phone2)     # should print "Phone number is not valid" 3-3
