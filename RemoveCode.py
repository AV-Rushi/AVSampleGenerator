def removeTag(root, element):
    for elem in root.findall(".//*"):
        if element in elem:
            elem.remove(element)