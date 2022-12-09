while True:
    #declare vowels in a list
    vowels = ['a','e','i','o','u']
    #take user input
    letter = input("Enter an Alphabet: ")
    #make the input in lowercase and check if it is inside the list
    if len(letter) == 1:
        if letter.lower() in vowels:
            print("the letter is vowel")
        #check if it is a digit
        elif letter.isdigit():
            print("it is a number")
        else:
            print("it is consonant")
        
        cont = input("Another One? Yes or No: ")
        
        while cont.lower() not in ("yes", "no"):
            cont = input("Please Enter Yes or No Only: ")
            
        if cont == "no":
            print()
            print("Thankyou")
            break
    else:
        print("Please Enter A single character only!")