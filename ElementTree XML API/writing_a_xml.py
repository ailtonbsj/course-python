import xml.etree.ElementTree as ET

# parse XML from file
tree = ET.parse('country_data.xml')
root = tree.getroot()

# set elements
for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')
tree.write('output1.xml')

# remove elements
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
tree.write('output2.xml')


# append elements
country = root.findall('country')[-1]
extra = ET.SubElement(country, 'extra')
extra.set('type', 'economics')
power = ET.SubElement(extra, 'power')
power.text = '$ 3T'

print(ET.tostring(root))
