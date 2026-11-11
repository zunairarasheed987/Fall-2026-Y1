stock = 100
total_sold = 0

print(f"Starting stock: {stock} units")

while stock > 0:
    try:
        qty = int(input("\nEnter quantity sold (-1 to stop): "))
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        continue

    if qty == -1:
        break

    if qty <= 0:
        print("Error: Quantity must be greater than zero.")
        continue

    if qty > stock:
        print(f"Error: Only {stock} units available. Transaction rejected.")
        continue

    stock -= qty
    total_sold += qty
    print(f"Sale successful. Remaining stock: {stock}")

    if stock == 0:
        print("Stock is finished. No more sales possible.")

print("\n----- Inventory Summary -----")
print(f"Total units sold : {total_sold}")
print(f"Remaining stock  : {stock}")
