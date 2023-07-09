import re

def validate_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[$#@]', password):
        return False
    return True

# Test with comma-separated passwords
passwords = "ABd1234@1,aF1#,2w3E*,2We3345"
valid_passwords = []
for password in passwords.split(','):
    if validate_password(password.strip()):
        valid_passwords.append(password.strip())
print(','.join(valid_passwords))
