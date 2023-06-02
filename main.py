import requests
from bs4 import BeautifulSoup
import json
url = "https://pikabu.ru"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.2.928 Yowser/2.5 Safari/537.36"
}
response = requests.get(url, headers=headers)
src = response.text
# print(src)
# with open("index.html", "w") as file:
#     file.write(src)

with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
all_article = soup.find_all("article")
for item in all_article:
    _name = item.find(class_="story__user-link")
    name = _name.text.strip()
    _id = item.get("data-story-id")
    all_text = item.find("div", class_="story__content-inner")
    _txt = all_text.text.strip().replace("\n", "").replace(".", "\n")
    all_image = item.find(class_="story-image__image")
    if all_image is None:
        continue
    else:
        image = all_image.get("data-src")
    all_post = item.find(class_="story__title-link")
    item_http = all_post.get("href")
    print(f"id: {_id}\nname: {name}\nimage: {image}\npost: {item_http}\ntxt: {_txt}\n")
