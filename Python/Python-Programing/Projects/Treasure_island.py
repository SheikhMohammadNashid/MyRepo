print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

path_a = input(
    'You are at a cross road. Where do you want to go?\n'
    'Type "left" or "right":\n'
).lower()

if path_a == "left":
    path_b = input(
        'You have come to a lake. There is an island in the middle of the lake.\n'
        'Type "wait" to wait for the boat. Type "swim" to swim across:\n'
    ).lower()

    if path_b == "wait":
        path_c = input(
            'You have arrived at the island unharmed.\n'
            'There is a house with three doors: red, yellow, and blue.\n'
            'Which color do you choose?\n'
        ).lower()

        if path_c == "red" or path_c == "blue":
            print("You are safe and found the treasure! 🏆")
        else:
            print("You were killed by the dragon. Game Over 🐉")

    else:
        print("Game Over. You drowned 🌊")

else:
    print("The shark ate you 🦈 Game Over")
