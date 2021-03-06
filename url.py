import requests
import xml.etree.ElementTree as ET
import re
import urllib3
import tinys3
import io

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = 'https://www.bitchute.com/feeds/rss/channel/rongibson/'
ET.register_namespace('atom','http://www.w3.org/2005/Atom')
r = requests.get(url, verify=False)
r = (requests.utils.get_unicode_from_response(r))
root = ET.fromstring(r)

for chan in root:
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
        for link in item.findall('link'):
            link.text = thumb_link
        for description in item.findall('description'):
            old_description = (description.text)
            # new_description = ('<![CDATA[<img src="' + thumb_link + '"/>')
            # new_description = new_description + old_title
            # problems with the cdata encoding, figure it out
            new_description = old_title
            description.text = new_description

tree_out = io.BytesIO(b"abcdef")
tree_out.write(ET.tostring(root, encoding="utf-8"))

s3_con = tinys3.Connection('cheeky', 'bugger', tls=True)
s3_con.upload('ron3.rss', tree_out, 'secrets')
tree_out.close()
print('I am at the end now')