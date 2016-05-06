import xml.etree.cElementTree as ET


def write_metadata_xml(filepath):
    s = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd">
"""
    root = ET.Element("properties")

    ET.SubElement(root, "entry", key="cm:title").text = "A photo of a flower."
    ET.SubElement(root, "entry",
                  key="cm:description").text = "A photo I took of a flower while walking around Bantry Bay."
    ET.SubElement(root, "entry", key="cm:created").text = "1901-01-01T12:34:56.789+10:00"
    ET.SubElement(root, "entry", key="cm:author").text = "Peter Monks"
    ET.SubElement(root, "entry", key="cm:publisher").text = "Peter Monks"
    ET.SubElement(root, "entry", key="cm:type").text = "Photograph"

    indent(root)
    tree = ET.ElementTree(root)

    # tree.write(filename, encoding="utf-8", xml_declaration=True)
    with open(filepath, 'w') as f:
        f.write(s)
        tree.write(f, 'utf-8')


def indent(elem, level=0):
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem
