import requests
from xml.etree import ElementTree as ET
url = 'https://www.bitchute.com/embed/pcvxneAlSGZo/'
r = requests.get(url, verify=False)
print(r.text)