import requests
import re
from collections import Counter

url = "https://stepik.org/media/attachments/lesson/209719/2.html"
content = requests.get(url=url).text

with open("content.html", "w", encoding="UTF-8") as file:
    file.write(content)

with open("content.html", encoding="UTF-8") as file:
    finder = re.findall(r"<code>(.*?)</code>", file.read())

counter = Counter(finder).most_common(3)
for word, count in counter:
    print(word, end=" ")
