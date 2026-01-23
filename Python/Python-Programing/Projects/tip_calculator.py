print("Welcome to tip calculator")

total_bill = float(input("What was the total bill? $\n"))

percentage_tip = float(input("How much tip would you like to give? 10, 12, or 15?\n"))

split_bill = float(input("How many people are splitting the bill?\n"))

tip = total_bill * (percentage_tip / 100)

cost = (total_bill + tip) / split_bill

final_cost = round(cost, 2)

print(f"Each person should pay: ${final_cost}")
