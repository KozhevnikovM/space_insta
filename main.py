import requests, os, json
from pprint import pprint


def get_file_extension(file_url):
    return file_url.split('.')[-1]


def download_image(image_url, filename):
    if not os.path.exists('images'):
        os.makedirs('images')
    response = requests.get(image_url)
    with open('images/{}'.format(filename), 'wb') as image_file:
        image_file.write(response.content)


def get_latest_spasex_photos_urls():
    url='https://api.spacexdata.com/v3/launches/latest?pretty=true'
    response = requests.get(url)
    photos_list = json.loads(response.text)['links']['flickr_images']
    return photos_list


def download_latest_spasex_photos():
    for counter, url_photo in enumerate(get_latest_spasex_photos_urls()):
        filename = 'SpaceX {}.{}'.format(counter, get_file_extension(url_photo))
        download_image(url_photo, filename)


def get_hubble_images_list(url):
    response = requests.get(url)
    photos_list = json.loads(response.text)['image_files']
    return [photo['file_url'] for photo in photos_list]


def download_hubble_image(image_id):
    url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
    photo_url = get_hubble_images_list(url)[-1]
    filename = 'hubble_{}.{}'.format(image_id, get_file_extension(photo_url))
    download_image(photo_url, filename)

def download_hubble_collection_images(collection):
    url = 'http://hubblesite.org/api/v3/images/{}'.format(collection)
    response = requests.get(url)
    for photo in json.loads(response.text):
        download_hubble_image(int(photo['id']))
        print('{} downloaded'.format(photo['name']))


if __name__ == '__main__':
    download_hubble_collection_images('spacecraft')
