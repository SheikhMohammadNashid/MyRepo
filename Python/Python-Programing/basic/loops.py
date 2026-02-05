'''fruits = ['Apple','Peach','Mango']

for fruit in fruits:
    print(fruit)

p = 5

for a in range(p):
    print("I am Sorry")

scores = [
    78, 85, 92, 67, 74, 88, 90, 81, 69, 76,
    84, 91, 73, 68, 79, 86, 94, 72, 80, 77,
    83, 89, 66, 71, 75, 87, 93, 82, 70, 74,
    85, 90, 78, 69, 81, 88, 92, 76, 73, 84
]
sum = 0
for score in scores:
    sum += score
print(sum)


max_score = scores[0]   # assume first value is max


for score in scores:
    if score > max_score:
        max_score = score

print(max_score)

print(max(scores)) # Or we can directly use this


for number in range(1, 11):
    product = 9 * number
    print(product)

total = 0

for number in range(1, 101):
    total += number
print(total)'''

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
