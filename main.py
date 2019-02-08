import requests, os

filename = 'images/hubble.jpg'
url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
response = requests.get(url)

with open(filename, 'wb') as file:
    file.write(response.content)

if not os.path.exists('images'):
    os.makedirs('images')
