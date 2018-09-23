import requests
from xml.etree import ElementTree as ET
import re
import ffmpeg
import os

url = 'https://www.bitchute.com/feeds/rss/channel/rongibson/'
r = requests.get(url, verify=False)
root = ET.fromstring(r.text)
# for child in root[0]:
for chan in root:
    # print(child.tag, child.attrib, child.text)
    for item in chan.findall('item'):
        for link in item.findall('link'):
            print(link.text)
        for guid in item.findall('guid'):
            print (guid.text)
    if child.tag == 'item':
# it is kinda working like you think up to here.
        for kid in child.iter():
            print(index, kid.tag, kid.attrib, kid.text)
            # if kid.tag == 'link':
            thetest = kid[index].tag
            thelink = requests.get(kid[index].text, verify=False)
            thelinktext = thelink.text
            thelinklinks = re.findall('"(https:\/\/seed.*?)"', thelinktext)
            link = thelinklinks[0]
            # if kid.tag == 'guid':
            guid = kid[guid].text
            # if kid.tag == 'enclosure':
            thumb = kid[guid].attrib[url]
            print('The link is %s, the guid is %s, the thumb is %s' % link, guid, thumb)
            # os.system("ffmpeg -i %s %s.mp3 -y" % link, guid)                
print('I am at the end now')
