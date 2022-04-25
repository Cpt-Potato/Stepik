import requests
from bs4 import BeautifulSoup

url = "https://stepik.org/media/attachments/lesson/209723/5.html"
r = requests.get(url).text
soup = BeautifulSoup(r, "lxml")

print(sum(int(td.text) for td in soup.find_all("td")))
