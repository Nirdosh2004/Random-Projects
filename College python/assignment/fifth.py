
print("Enter dictionary items :")
dictionary = {}
while True:
    try:
        key = input("Enter key : ")
        if not key:
            break
        value = float(input("Enter value: "))
        dictionary[key] = value
    except ValueError:
        print("Please enter a valid number.")


totals = sum(dictionary.values())

print("Sum of values:", totals)
