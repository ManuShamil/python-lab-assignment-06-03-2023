def validate_email(email):
    if email.count('@') == 1 and email.count('.') >= 1:
        at_index = email.index('@')
        dot_index = email.index('.')
        if at_index > 0 and dot_index > at_index + 1 and dot_index < len(email) - 1:
            if email[at_index - 1].isalnum() and email[dot_index + 1].isalnum():
                return True
    return False

# Test with VIT email addresses
emails = ['john.doe@vit.ac.in', 'jane.doe@vit.com', 'invalid.email@vit', 'john.doe@vit.']
for email in emails:
    if validate_email(email):
        print(email, "is a valid VIT email address.")
    else:
        print(email, "is not a valid VIT email address.")
