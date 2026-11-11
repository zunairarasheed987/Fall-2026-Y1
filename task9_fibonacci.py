while True:
    try:
        n = int(input("How many terms to generate? "))
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        continue

    if n < 1:
        print("Number of terms must be at least 1. Try again.")
    else:
        break

a, b = 0, 1
total = 0
even_count = 0
odd_count = 0

print("\nFibonacci sequence:")

for i in range(n):
    print(a, end=" ")

    total += a

    if a % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    a, b = b, a + b

print(f"\nSum: {total}")
print(f"Even terms: {even_count}")
print(f"Odd terms: {odd_count}")
