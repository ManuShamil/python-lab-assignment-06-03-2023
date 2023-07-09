import re

def extract_username_company(email):
    pattern = r'^(\w+)@(\w+)\.com$'
    match = re.match(pattern, email)
    if match:
        username = match.group(1)
        company = match.group(2)
        return username, company
    else:
        return None, None

# Accept the email address as console input
email_address = input("Enter an email address: ")

# Extract the username and company name
username, company = extract_username_company(email_address)

# Print the extracted username and company name
print("Username:", username)
print("Company:", company)