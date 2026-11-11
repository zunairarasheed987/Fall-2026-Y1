while True:
    try:
        n = int(input("Enter a positive integer: "))
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        continue

    if n > 0:
        break
    print("Number must be positive. Try again.")

print("\n--- Pattern ---")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\n--- Inverted Pattern ---")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\n--- Multiplication Table (1 to {}) ---".format(n))
for i in range(1, n + 1):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()
