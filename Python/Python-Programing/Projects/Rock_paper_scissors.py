import random

choice = ['rock', 'paper', 'scissors']

user_choice = int(input("Type 0 for rock, 1 for paper, 2 for scissors: "))

if user_choice < 0 or user_choice > 2:
    print("You entered the wrong input")
else:
    cpu_choice = random.choice(choice)
    print("Computer chose:", cpu_choice)

    if user_choice == 0 and cpu_choice == 'rock':
        print("Draw")
    elif user_choice == 0 and cpu_choice == "paper":
        print("Paper! You lose")
    elif user_choice == 0 and cpu_choice == "scissors":
        print("Scissors! You win")
    elif user_choice == 1 and cpu_choice == "rock":
        print("Rock! You win")
    elif user_choice == 1 and cpu_choice == 'paper':
        print("Draw")
    elif user_choice == 1 and cpu_choice == 'scissors':
        print("Scissors! You lose")
    elif user_choice == 2 and cpu_choice == 'rock':
        print("Rock! You lose")
    elif user_choice == 2 and cpu_choice == 'paper':
        print("Paper! You win")
    elif user_choice == 2 and cpu_choice == 'scissors':
        print("Draw")
