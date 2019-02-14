import requests, re, argparse
from common import download_image, get_file_extension


def get_hubble_images_list(url):
    response = requests.get(url)
    photos_list = response.json()['image_files']
    photo_name = response.json()['name']
    return [photo['file_url'] for photo in photos_list], photo_name


def download_hubble_image(image_id):
    url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
    hubble_images_list = get_hubble_images_list(url)
    photo_url = hubble_images_list[0][-1]
    file_name = re.sub(r'[\\/\?<>:]', '', hubble_images_list[1])
    file_ext = get_file_extension(photo_url)
    filename = file_name + '.' + file_ext
    download_image(photo_url, filename)


def fetch_hubble_collection(collection):
    url = 'http://hubblesite.org/api/v3/images/{}'.format(collection)
    return requests.get(url).json()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('collection', default='wallpaper', nargs='?')
    collection = parser.parse_args().collection
    for photo in fetch_hubble_collection(collection):
        download_hubble_image(int(photo['id']))
        print('{} downloaded'.format(photo['name']))

