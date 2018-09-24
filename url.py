import requests
import xml.etree.ElementTree as ET
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = 'https://www.bitchute.com/feeds/rss/channel/rongibson/'
r = requests.get(url, verify=False)
root = ET.fromstring(r.content)

for chan in root[0]:
    for item in chan.findall('item'):
        for title in item.findall('title'):
            old_title = (title.text)
        for link in item.findall('link'):
            old_link = (link.text)
        for guid in item.findall('guid'):
            old_guid = (guid.text)
        for enclosure in item.findall('enclosure'):
            thumb_link = (enclosure.attrib['url'])
            new_link = re.findall('"(https:\/\/seed.*?)"', ((requests.get(old_link, verify=False)).text))
            enclosure.set('url', new_link[0])

tree = ET.ElementTree(root)
tree.write("output.rss")
print('I am at the end now')