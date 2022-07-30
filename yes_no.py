while True:
    
#    print()
#    print("\tDo You want to Continue? Yes or No : ")
#    print()
    
#    print("Hello Again")
#    print()
    cont = input("Another One? Yes or No: ")
    
    while cont.lower() not in ("yes", "no"):
        cont = input("Please Enter Yes or No Only: ")
    if cont == "no":
        print()
        print("Thankyou")
        break