import os
from dotenv import load_dotenv
import instabot


def add_to_published(image_filename, log_file):
    with open(log_file, 'a') as file:
        file.write(image_filename)
        file.write('\n')


def check_is_published(image_filename, log_file):
    with open(log_file, 'r') as file:
        return image_filename in file.read().splitlines()


if __name__ == '__main__':
    load_dotenv()
    bot = instabot.Bot()
    bot.login(username=os.getenv('LOGIN'), password=os.getenv('PASSWORD'))
    published = 'published.txt'
    photos = os.listdir('images')

    for photo in photos:
        if not check_is_published(photo, published):
            bot.upload_photo('images/{}'.format(photo))
            add_to_published(photo, published)
        print('File already published')
