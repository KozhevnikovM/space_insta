import requests, os, json
from pprint import pprint


def download_image(image_url, filename):
    if not os.path.exists('images'):
        os.makedirs('images')
    response = requests.get(image_url)
    with open('images/{}'.format(filename), 'wb') as image_file:
        image_file.write(response.content)


def get_latest_spasex_photos():
    url='https://api.spacexdata.com/v3/launches/latest?pretty=true'
    response = requests.get(url)
    photos_list = json.loads(response.text)['links']['flickr_images']
    return photos_list


def download_latest_spasex_photos():
    for counter, url_photo in enumerate(get_latest_spasex_photos()):
        download_image(url_photo, 'spasex_{}.jpg'.format(counter))





if __name__ == '__main__':
    # url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    # filename = 'hubble.jpg'
    # download_image(url, filename)
    pprint(
        get_latest_spasex_photos()
    )
    download_latest_spasex_photos()
