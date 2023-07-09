import re

def extract_username_company(email):
    match = re.match(r'(\w+)@(\w+\.com)', email)
    if match:
        username = match.group(1)
        company = match.group(2)
        return username, company
    return None

# Test with email addresses
emails = ['john@google.com', 'jane@facebook.com', 'invalid.email']
for email in emails:
    result = extract_username_company(email)
    if result:
        username, company = result
        print("Email:", email)
        print("Username:", username)
        print("Company:", company)
    else:
        print("Invalid email:", email)
