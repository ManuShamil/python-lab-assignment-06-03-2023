import re

# 1. Extract the protocol and the hostname from the given URL
url = 'https://www.mit.edu'
protocol_hostname_regex = r'(https?|ftp)://([^\s/:]+)'
match = re.match(protocol_hostname_regex, url)
if match:
    protocol = match.group(1)
    hostname = match.group(2)
    print(f"Protocol: {protocol}")
    print(f"Hostname: {hostname}")
else:
    print("URL format not recognized.")

# 2. If the URL is of different type 'file://localhost:4040/zip_file', find the file, hostname, and port number.
url = 'file://localhost:4040/zip_file'
file_hostname_port_regex = r'file://(localhost|\w+):(\d+)/(\w+)'
match = re.match(file_hostname_port_regex, url)
if match:
    file_path = match.group(3)
    hostname = match.group(1)
    port = match.group(2)
    print(f"File: {file_path}")
    print(f"Hostname: {hostname}")
    print(f"Port: {port}")
else:
    print("URL format not recognized.")

# 3. For a general URL 'http://www.example.com/index.html', construct the path elements.
url = 'http://www.example.com/index.html'
path_elements_regex = r'(\w+):\/\/([\w.]+)\/(.*)'
match = re.match(path_elements_regex, url)
if match:
    protocol = match.group(1)
    hostname = match.group(2)
    path = match.group(3)
    path_elements = path.split('/')
    print(f"Protocol: {protocol}")
    print(f"Hostname: {hostname}")
    print(f"Path elements: {path_elements}")
else:
    print("URL format not recognized.")
