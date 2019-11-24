import lxml.etree as ET

file = "lubuntu-rc.xml"
tree = ET.parse(file)
root = tree.getroot()

keyboard = root.findall("{http://openbox.org/3.4/rc}keyboard")[0]

# Create keybind Object
keybind = ET.SubElement(keyboard, 'keybind')
keybind.set('key','C-F5')
action = ET.SubElement(keybind, 'action')
action.set('name', 'Execute')
command = ET.SubElement(action, 'command')
command.text = 'leafpad'

tree.write('out.xml', pretty_print=True)
