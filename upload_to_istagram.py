import requests, os
from dotenv import load_dotenv
import instabot


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


def upload_to_insta(username, password, photo, caption=None):
    bot = Bot()
    bot.login(username=username, password=password)
    bot.upload_photo(photo, caption)

if __name__ == '__main__':
    load_dotenv()
    bot = instabot.Bot()
    bot.login(username=os.getenv('USERNAME'), password=os.getenv('PASSWORD'))
    if bot.api.last_response != 200:
        exit(bot.api.last_response)
    photos = os.listdir('images')
    posted_photos = []
    for photo in photos:
        if photo not in posted_photos:
            bot.upload_photo('images/{}'.format(photo))
            posted_photos += photo
