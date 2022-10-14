# Quiz game July 11 2022

def testing():

    print("\nWelcome to My Special Quiz\n")
    score = 0
    quest = 0
    ans = input("1.What is the color of blood? : ")
    quest += 1
    if ans.lower() == "red":
        print("Correct")
        score += 1
    else:
        print("incorrect")
    ans = input("2.Is moon bigger than earth? : ")
    quest += 1
    if ans.lower() == "no":
        print("Correct")
        score += 1
    else:
        print("Incorrect")
    ans = input("3.What does RAM stand for? : ")
    quest += 1
    if ans.lower() == "random access memory":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    print("Your score is " + str(score) + " over " + str(quest))
    

# continue yes or no
while True:
    testing()
    cont = input("Play Again? Yes or No: ")
    while cont.lower() not in ("yes", "no"):
        cont = input("Please Enter Yes or No Only!: ")
    if cont == "no":
        print()
        print("-----Thank you-----")
        break
