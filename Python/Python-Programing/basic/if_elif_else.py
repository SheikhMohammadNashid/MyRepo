'''elif means “else if”.
We use it when we want to check multiple conditions, but only ONE of them should run.'''



print("Welcome to Mad Roller Coaster")

height = float(input("What is your height in cm?\n"))
age = int(input("What is your age?\n"))
bill = 0

if height > 120:
    print("Get ready to ride!")
    
    if age < 12:
        bill = 5
        print("You have to pay $5")
    elif age < 18:
        bill = 7
        print("You need to pay $7")
    else:
        bill = 12
        print("You need to pay $12")

    photo = input("Do you want a picture? Type y for Yes and n for No: ")
    if photo == "y":
        bill += 3

    print(f"You have to pay ${bill}")
else:
    print("Sorry, you are too short to ride.")
