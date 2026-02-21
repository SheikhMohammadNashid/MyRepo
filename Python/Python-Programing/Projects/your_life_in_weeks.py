age = int(input("What is your age: "))

def your_life_in_weeks(age):
    total_weeks_lived = age * 52.1775
    print(f"Total weeks lived = {total_weeks_lived:.2f}")
    
    total_weeks_in_lifetime = 90 * 52.1775
    weeks_remaining = total_weeks_in_lifetime - total_weeks_lived
    
    print(f"You have {weeks_remaining:.2f} weeks remaining")


your_life_in_weeks(25)
