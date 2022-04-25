from bs4 import BeautifulSoup

with open("map2.osm", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "lxml-xml")

# counter = 0
#
# for node in soup.find_all("node"):
#     if node.find("tag", attrs={"k": "amenity", "v": "fuel"}):
#         counter += 1
#
# print(counter)

print(len(soup.select("node tag[k=amenity][v=fuel]")))
