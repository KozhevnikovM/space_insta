import requests, os


def get_file_extension(file_url):
    return file_url.split('.')[-1]


def download_image(image_url, filename):
    if not os.path.exists('images'):
        os.makedirs('images')
    response = requests.get(image_url)
    if not response.ok:
        return None
    with open('images/{}'.format(filename), 'wb') as image_file:
        image_file.write(response.content)
