from yattag import Doc, indent

doc, tag, text = Doc().tagtext()

with tag("html"):
    with tag("body"):
        with tag("table"):
            for table_row in range(1, 11):
                with tag("tr"):
                    for table_cell in range(1, 11):
                        with tag("td"):
                            number = str(table_row * table_cell)
                            with tag("a", href=f"http://{number}.ru"):
                                text(number)

with open("3.html", "w") as file:
    file.write(indent(doc.getvalue()))
