import xml.etree.ElementTree as ET

# parse XML from file
tree = ET.parse('country_data.xml')
root = tree.getroot()

# Or from a String
# root = ET.fromstring(country_data_as_string)

# get attributes
print(root.tag)
print(root.attrib)
print(root.text)

# get children
for child in root:
    print(child.tag, child.attrib)

# get children as array
print(root[0][1].text)

# iterating elements
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)