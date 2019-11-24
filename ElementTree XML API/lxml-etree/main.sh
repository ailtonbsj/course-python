#!/bin/bash

python3 enable-keybind.py
echo '<?xml version="1.0" encoding="UTF-8"?>' > new.xml
cat out.xml >> new.xml
rm out.xml
# Fix xml
sed -i "s/><action/>\n      <action/g" new.xml
sed -i "s/><command/>\n        <command/g" new.xml
sed -i "s/command></command>\n      </g" new.xml
sed -i "s/action></action>\n    </g" new.xml
sed -i "s/keybind></keybind>\n  </g" new.xml
sed -i "s/<keybind key=\"C-F5/  <keybind key=\"C-F5/g" new.xml