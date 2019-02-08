import requests, os


def download_image(image_url, filename):
    if not os.path.exists('images'):
        os.makedirs('images')
    response = requests.get(image_url)
    with open('images/{}'.format(filename), 'wb') as image_file:
        image_file.write(response.content)


if __name__ == '__main__':
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    filename = 'hubble.jpg'
    download_image(url, filename)
