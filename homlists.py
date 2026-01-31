
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

squares = [x**2 for x in range(start, end + 1)]


evens = [n for n in squares if n % 2 == 0]
odds = [n for n in squares if n % 2 != 0]


print(f"\nAll squares in range: {squares}")
print(f"Even squares: {evens}")
print(f"Odd squares: {odds}")