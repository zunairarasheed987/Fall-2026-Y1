start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count = 0
total_sum = 0
primes = []

for num in range(start, end + 1):
    if num < 2:
        continue

    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)
        count += 1
        total_sum += num

print("\n----- Prime Number Results -----")
if count > 0:
    print("Prime numbers:", primes)
else:
    print("No prime numbers found in this range.")
print("Total prime numbers found:", count)
print("Sum of all prime numbers:", total_sum)
