data = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 10
}

value = int(input("Enter the value to check frequency: "))

frequency = 0
for v in data.values():
    if v == value:
        frequency += 1

print("Frequency of", value, "is:", frequency)
