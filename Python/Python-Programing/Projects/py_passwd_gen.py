import random

alphabets = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

number_s = ['0','1','2','3','4','5','6','7','8','9']

special_characters = ['!', '@', '#', '$', '%', '&', '^', '*', '(', ')']

print("Welcome to the PyPassword Generator!")

letters = int(input("How many letters would you like in your password? "))
symbols = int(input("How many symbols would you like in your password? "))
numbers = int(input("How many numbers would you like in your password? "))

password_list = []

for i in range(letters):
    password_list.append(random.choice(alphabets))

for i in range(symbols):
    password_list.append(random.choice(special_characters))

for i in range(numbers):
    password_list.append(random.choice(number_s))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print("Your password is:", password)