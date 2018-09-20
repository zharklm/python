import requests
from xml.etree import ElementTree as ET
url = 'https://www.bitchute.com/feeds/rss/channel/rongibson/'
r = requests.get(url, verify=False)
root = ET.fromstring(r.text)
for child in root[0]:
    print(child.tag, child.attrib, child.text)
    if child.tag == 'item':
        for kid in child:
            print(kid.tag, kid.attrib, kid.text)
