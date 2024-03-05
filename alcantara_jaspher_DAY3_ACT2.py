years_in_service = int(input("Years in Service: "))
office = input("Office (it/acct/hr): ")

if years_in_service >= 10:
    if office == "it":
        bonus = 10000
    elif office == "acct":
        bonus = 12000
    elif office == "hr":
        bonus = 15000
    else:
        bonus = 0
    print("Bonus ", bonus)
else:
    if office == "it":
        bonus = 5000
    elif office == "acct":
        bonus = 6000
    elif office == "hr":
        bonus = 7500
    else:
        bonus = 0
    print("Bonus ", bonus)
