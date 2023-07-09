import re

def validate_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[$#@]", password):
        return False
    return True

# Accept a sequence of comma-separated passwords
passwords = input("Enter comma-separated passwords: ").split(",")

# Check the validity of each password and store the valid ones
valid_passwords = [password for password in passwords if validate_password(password)]

# Print the valid passwords separated by commas
print("Valid passwords: " + ", ".join(valid_passwords))