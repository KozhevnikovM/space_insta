import requests, json
from common import download_image, get_file_extension

def get_latest_spasex_photos_urls():
    url='https://api.spacexdata.com/v3/launches/latest?pretty=true'
    response = requests.get(url)
    photos_list = json.loads(response.text)['links']['flickr_images']
    return photos_list


def download_latest_spasex_photos():
    for counter, url_photo in enumerate(get_latest_spasex_photos_urls()):
        filename = 'SpaceX_{}.{}'.format(counter, get_file_extension(url_photo))
        download_image(url_photo, filename)

if __name__ == '__main__':
    download_latest_spasex_photos()
    exit('Download complete')
