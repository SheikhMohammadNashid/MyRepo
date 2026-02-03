import random

# random_int = random.randint(1, 6)
# print(random_int)



# random_no_0_to_1 = random.random() * 10
# print(random_no_0_to_1)

# random_float = random.uniform(1,10)

# print(random_float)


heads_tails = random.randint(1,2)

if heads_tails == 1:
    print("heads")
else:
    print("Tails")


friends =['Nashid','Ikraam','Sumaid','Faheem']

bill_payment = random.choice(friends)

print(f"Bill will be paid by: '{bill_payment}'")





