import requests, json, re, argparse
from common import download_image, get_file_extension

def get_hubble_images_list(url):
    response = requests.get(url)
    photos_list = json.loads(response.text)['image_files']
    photo_name = json.loads(response.text)['name']
    return [photo['file_url'] for photo in photos_list], photo_name


def download_hubble_image(image_id):
    url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
    photo_url = get_hubble_images_list(url)[0][-1]
    file_name = re.sub(r'[\\/\?<>:]', '', get_hubble_images_list(url)[1])
    file_ext = get_file_extension(photo_url)
    filename = file_name + '.' + file_ext
    download_image(photo_url, filename)


def download_hubble_collection_images(collection):
    url = 'http://hubblesite.org/api/v3/images/{}'.format(collection)
    response = requests.get(url)
    for photo in json.loads(response.text):
        download_hubble_image(int(photo['id']))
        print('{} downloaded'.format(photo['name']))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('collection', default='wallpaper', nargs='?')
    collection = parser.parse_args().collection
    download_hubble_collection_images(collection)

