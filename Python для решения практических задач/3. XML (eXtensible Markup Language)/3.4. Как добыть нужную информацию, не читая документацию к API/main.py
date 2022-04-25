from bs4 import BeautifulSoup

# with open("map2.osm", encoding="utf-8") as file:
#     soup = BeautifulSoup(file, "lxml-xml")

soup = BeautifulSoup(open("map2.osm", encoding="utf-8"), "lxml-xml")
print(len(soup.select("tag[k=amenity][v=fuel]")))
