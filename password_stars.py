MINIMUM_LENGTH = 8
password = input("Enter password: ")
while len(password) < MINIMUM_LENGTH:
    print("Minimum length not met")
    password = input("Enter password: ")
print("Password:", "*" * len(password))
