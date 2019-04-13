import os
import json
import ctypes
import random
from bs4 import BeautifulSoup as BS
import requests

url = "https://unsplash.com/search/photos/{0}"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def is_duplicate(link):
    home_path = os.path.expanduser('~')
    wallpaper_path = '.wallpaper_files/wallpaper.json'
    full_path = os.path.join(home_path, wallpaper_path)
    dir_path = os.path.dirname(full_name)
    duplicate = True

    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    if not os.path.exists(full_path):
        with open(full_path, 'w') as wf:
            links = {
                'wallpaper_urls': []
            }
            json.dump(links, wf)
    else:
        with open(full_path, 'r') as wf:
            try:
                data = json.load(wf)
                urls = data.get('wallpaper_urls')
                if not link in urls:
                    urls.append(link)
                    duplicate = False
            except:
                os.remove(full_path)
                is_duplicate(link)

        if not duplicate:
            with open(full_path, 'w') as wf:
                json.dump(data, wf)

def keywords(url):
    key_list = [
        "black", "shadow", "ghost", "night", "Neon",
        "space", "darkness", "dark", "Dark Background","Horror", "stars",
        "darkside", "universe", "moon", "galaxy"
     ]

    choice = random.choice(key_list)
    url = url.format(choice)
    print(url)
    return url

def random_wallpaper()
    response = requests.get(keywords(url), headers=headers)
    soup = BS(response.content, 'lxml')
    #print(soup.prettify())
    links = []

    for i in soup.find_all('img'):
        primary_img = i.get('src')

        if primary_img:
            contents = primary_img.split(".")
            if not 'adserver' in contents:
                print(primary_img)
                links.append(primary_img)

    choice = random.choice(links)
    return choice

duplicate = True
while duplicate:
    wallpaper_url = random_wallpaper()
    if not is_duplicate(wallpaper_url):
        duplicate = False

image_raw = requests.get(wallpaper_url, headers=headers)
home_path = os.path.expanduser('~')
wallpaper_path = '.wallpaper_files/wallpaper.png'
path = os.path.join(home_path, wallpaper_path)

with open(path, 'wb') as wf:
    wf.write(image_raw.content)

ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
