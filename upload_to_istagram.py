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


def upload_photos(username, password, photos_dir, file_with_published):
    bot = instabot.Bot()
    bot.login(username=username, password=password)
    for photo in os.listdir(photos_dir):
        if not check_is_published(photo, file_with_published):
            bot.upload_photo('{}/{}'.format(photos_dir, photo))
            add_to_published(photo, file_with_published)
        print('Skiped')


if __name__ == '__main__':
    load_dotenv()
    username, password = os.getenv('LOGIN'), os.getenv('PASSWORD')
    published_file = 'published.txt'
    photos_dir = 'images'
    upload_photos(username, password, photos_dir, published_file)

