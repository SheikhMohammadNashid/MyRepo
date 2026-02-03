'''A list is a collection of items stored in a single variable.'''

# Example:
details = ["Nashid", 25, "Buchpora"]

print(details)

# Operations on lists

print(details[0])  # This prints the first element of the list i.e Nashid

details[1] = 7  # This changes the value to 7
print(details)

details.append("Legend")  # Adds "Legend" at the end of the list
print(details)

details.extend(["Green Valley", "Football"])  # Adds multiple items
print(details)
