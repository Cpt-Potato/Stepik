from bs4 import BeautifulSoup
import requests

url = "https://stepik.org/media/attachments/lesson/209723/3.html"
r = requests.get(url).text

with open("index.html", "w") as file:
    file.write(r)

with open("index.html") as file:
    soup = BeautifulSoup(file.read(), "lxml")

result = 0
for tag in soup.find_all("td"):
    number = tag.get_text().strip()
    result += int(number)
print(result)
