import random

word_list = ["Python","DevOps","Ansible","FastAPI","Docker","Jenkins"]
word_to_guess = random.choice(word_list).lower()

tries = 6
guessed_word = []
word_completion = "_" * len(word_to_guess)

print("Welcome to Hangman Game")

while tries > 0 and "_" in word_completion:

    print("\nWord:", word_completion)
    print("Guessed letters:", guessed_word)
    print("Tries:", tries)

    guess = input("Guess a letter: ").lower()

    # Check if already guessed
    if guess in guessed_word:
        print("You already guessed that letter")
        continue

    guessed_word.append(guess)

    if guess in word_to_guess:
        print("Good guess!")

        new_word = ""
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                new_word += guess
            else:
                new_word += word_completion[i]

        word_completion = new_word

    else:
        print("Wrong guess!")
        tries -= 1

if "_" not in word_completion:
    print("\n🎉 You won! The word was:", word_to_guess)
else:
    print("\n💀 You lost! The word was:", word_to_guess)