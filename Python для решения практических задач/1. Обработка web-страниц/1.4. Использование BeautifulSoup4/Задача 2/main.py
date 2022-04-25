import requests
from bs4 import BeautifulSoup

url = "https://stepik.org/media/attachments/lesson/209723/4.html"
r = requests.get(url).text

with open("index.html", "w") as file:
    file.write(r)

with open("index.html") as file:
    soup = BeautifulSoup(file.read(), "lxml")

print(sum(int(tag.get_text()) for tag in soup.find_all("td")))
