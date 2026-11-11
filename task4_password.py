correct_username = "admin"
correct_password = "pass123"

MAX_ATTEMPTS = 3
attempts = 0

while attempts < MAX_ATTEMPTS:
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username == "" or password == "":
        print("Username or password cannot be empty. Try again.\n")
        continue

    attempts += 1

    if username == correct_username and password == correct_password:
        print("Login successful! Welcome to the university portal.")
        break
    else:
        remaining = MAX_ATTEMPTS - attempts
        if remaining > 0:
            print(f"Incorrect credentials. Attempts remaining: {remaining}\n")
        else:
            print("Too many failed attempts. Your account is locked.")
