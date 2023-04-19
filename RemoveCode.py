def removeTag(root, element):
    for elem in root.findall(".//*"):
        if element in elem:
            elem.remove(element)

def removeTag1(root, elementList):
    for element in elementList:
        for elem in root.findall(".//*"):
            if element in elem:
                elem.remove(element)