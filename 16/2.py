def validate_vit_email(email):
    at_symbol_index = email.find('@')
    dot_symbol_index = email.rfind('.')
    space_symbol_index = email.find(' ')

    if at_symbol_index > 0 and dot_symbol_index > at_symbol_index and space_symbol_index == -1:
        return True
    else:
        return False

# Example usage
email_address = input("Enter your VIT email address: ")

if validate_vit_email(email_address):
    print("Valid VIT email address")
else:
    print("Invalid VIT email address")
