'''Nested if else is used when single condition is not enough'''


age = int(input("Enter your age:\n"))

if age >= 18:
    if age >= 60:
        print("You have to pay $70 (Senior discount)")
    else:
        print("You have to pay $100")
else:
    print("You have to pay $50")
