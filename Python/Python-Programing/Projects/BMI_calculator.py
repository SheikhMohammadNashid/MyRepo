print("Welcome to BMI calculator")

weight = float(input("Enter your Weight in kg \n"))

height = float(input("Enter your Height in m \n"))

bmi = weight / height ** 2

a = round(bmi ,2)

print(f"Your BMI is: {a}")

