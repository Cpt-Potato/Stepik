from urllib.request import urlretrieve
import xmltodict

urlretrieve("https://stepik.org/media/attachments/lesson/245571/map1.osm", "map1.osm")  # download file
fin = open("map1.osm", "r", encoding="utf8")
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
print(parsedxml["osm"]["node"][100]["@id"])
