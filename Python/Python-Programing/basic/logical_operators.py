'''In Python, logical operators are used to combine or modify Boolean expressions (True / False)'''

#1. and
#Returns True if both conditions are True

#Example

age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed entry")


#2. or
#Example

is_student = False
has_coupon = True

if is_student or has_coupon:
    print("Discount applied")


#3. not

is_raining = False

if not is_raining:
    print("Go outside")
