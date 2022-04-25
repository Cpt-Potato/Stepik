# from urllib.request import urlretrieve
from bs4 import BeautifulSoup

# url = "https://stepik.org/media/attachments/lesson/245678/map1.osm"
# urlretrieve(url, "map1.osm")

with open("map1.osm", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml-xml")

tags, no_tags = 0, 0

for node in soup.find_all("node"):
    if node.find("tag"):
        tags += 1
    else:
        no_tags += 1

print(tags, no_tags)
