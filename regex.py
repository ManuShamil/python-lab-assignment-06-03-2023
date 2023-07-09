import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')

result = phoneNumRegex.sub('***-***-****', 'My number is 415-555-4242.')
print(result)


print(phoneNumRegex.match('415-555-4242'))

emailRegex = re.compile(r"\w+@\w+.\w+")
emil = emailRegex.match('finin@cs.umbc.edu')

print(emil)
