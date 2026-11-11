even_count = 0
odd_count = 0
positive_count = 0
total = 0
largest = None

print("Enter integers to analyze (enter 0 to stop).")

while True:
    try:
        num = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        continue

    if num == 0:
        break

    if num < 0:
        continue

    positive_count += 1
    total += num

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if largest is None or num > largest:
        largest = num

print("\n----- Analysis Results -----")
if positive_count == 0:
    print("No positive numbers were entered. Cannot calculate average.")
else:
    print(f"Even numbers   : {even_count}")
    print(f"Odd numbers    : {odd_count}")
    print(f"Largest number : {largest}")
    print(f"Sum            : {total}")
    print(f"Average        : {total / positive_count:.2f}")
