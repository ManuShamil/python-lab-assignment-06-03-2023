import re

# 1. Extract the protocol and the hostname from the given URL
url = 'https://www.mit.edu'
protocol = re.search(r'(.*?):', url).group(1)
hostname = re.search(r'//(.*?)(?:/|$)', url).group(1)
print("Protocol:", protocol)
print("Hostname:", hostname)

# 2. If the URL is of different type 'file://localhost:4040/zip_file', find the file, hostname, and port number.
url = 'file://localhost:4040/zip_file'
file = re.search(r'//.*?/(.*?)$', url).group(1)
hostname = re.search(r'//(.+?):', url).group(1)
port = re.search(r':(\d+)', url).group(1)
print("File:", file)
print("Hostname:", hostname)
print("Port:", port)

# 3. For a general URL 'http://www.example.com/index.html', construct the path elements.
url = 'http://www.example.com/index.html'
path_elements = re.findall(r'/([^/]+)', url)
print("Path elements:", path_elements)
