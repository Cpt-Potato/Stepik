# with open("2.html", "w") as file:
#     file.write("<html>\n<body>\n<table>\n")
#     for table_row in range(1, 11):
#         file.write("\t<tr>\n")
#         for table_cell in range(1, 11):
#             file.write(f"\t\t<td>{table_row * table_cell}")
#             file.write("</td>\n")
#         file.write("\t</tr>\n")
#     file.write("</table>\n</body>\n</html>")

from yattag import Doc, indent

doc, tag, text = Doc().tagtext()

with tag("html"):
    with tag("body"):
        with tag("table"):
            for table_row in range(1, 11):
                with tag("tr"):
                    for table_cell in range(1, 11):
                        with tag("td"):
                            text(f"{table_row * table_cell}")

with open("2.html", "w") as file:
    file.write(indent(doc.getvalue()))

# from lxml import etree
#
# html = etree.Element("html")
# body = etree.SubElement(html, "body")
# table = etree.SubElement(body, "table")
#
# for i in range(1, 11):
#     row = etree.SubElement(table, "tr")
#     for j in range(1, 11):
#         td = etree.SubElement(row, "td")
#         td.text = str(i * j)
#
# with open("2.html", "wb") as file:
#     file.write(etree.tostring(html, pretty_print=True))
