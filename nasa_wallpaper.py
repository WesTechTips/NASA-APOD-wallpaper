from pathlib import Path
import requests
import shutil
import ctypes
import sys

api_key="DEMO_KEY"
api_url="https://api.nasa.gov/planetary/apod"

destination_path = Path().absolute() / 'images' / 'apod.jpg'

def get_today_apod_url():
    return requests.get(f'{api_url}?api_key={api_key}').json()['hdurl']

def get_random_apod_url():
    return requests.get(f'{api_url}?api_key={api_key}&count=1').json()[0]['hdurl']

def download_image(url):
    image_file = requests.get(url, stream=True)
    with open(destination_path, 'wb') as f:
        image_file.raw.decode_content = True
        shutil.copyfileobj(image_file.raw, f)

def set_wallpaper(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(path), 1)

if len(sys.argv) == 2:
    image_url = get_random_apod_url()
else:
    image_url = get_today_apod_url()

download_image(image_url)
set_wallpaper(destination_path)














