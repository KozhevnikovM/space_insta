# Space Instagram
Download photos from SpaceX and Hubble sites. Publish photos on Instagram.

## System requirements:
python3.5+

## How to install:
### Install requirements:

```bash
$ pip install -r requierments.txt

``` 
### Setup your instagram credentials:
Rename dotenv.sample to .env and specify LOGIN and PASSWORD with your credentials:
```text
LOGIN=your_instagram_username
PASSWORD=your_instagram_password
```

## How to run

If you want to fetch latest SpaceX photos, run fetch_spacex.py
Your photos will be saved in folder named 'images'
```bash
$ python fetch_spacex.py
Download complete

```


If you want to fetch hubble collections, run fetch_hubble.py.
Script download wallpapers collection, by default. 
But you can specify collection with command line "fetch_hubble.py
collection_name"

```bash
$ python fetch_hubble.py news
Uranus and Neptune downloaded
Compass Image of Uranus and Neptune downloaded
Uranus downloaded
```

To upload your photos on instagram, run "upload_to_instagram.py".
All photos in images folder will be uploaded.

```bash
$ python upload_to_instagram.py
Analizing `images/Uranus.png`
No exif info found (ERR: 'PngImageFile' object has no attribute '_getexif')
FOUND w:514, h:514, ratio=1.0
Square image
Saving new image w:514 h:514 to `images/Uranus.png.CONVERTED.jpg`
FOUND: w:514 h:514 r:1.0

```

# Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.