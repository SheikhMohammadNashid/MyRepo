'''Modulo(%) operator give ud the remainder after division'''

10 % 2 #output:0

print("Even no verifier")

number = int(input("Enter the no:"))

checked_no = number % 2

if checked_no == 0:
    print("The number is even.")
else:
    print("The number is odd.")
    