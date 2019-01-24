from bs4 import BeautifulSoup as BS
import urllib.request
import requests
import ctypes
import random

url = "https://wallpapersafari.com/dark-theme-wallpaper/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

try:
    response = requests.get(url, headers=headers)
    soup = BS(response.content, 'lxml')

    links = []
    for img_block in soup.find_all("img", class_="img-fluid"):
        link = img_block['src']
        links.append(link)

    wallpaper = random.choice(links)
    ext = wallpaper.split(".")[-1]
    path = f"F:/programs/wallpaper/pictures/wallpaper.{ext}"
    image_raw = requests.get(wallpaper, headers=headers)
    with open(path, 'wb') as wr:
        wr.write(image_raw.content)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)

except:
    path = "F:/programs/wallpaper/pictures/wallpaper.jpg"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
