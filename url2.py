import requests
import ffmpeg
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://seed07.bitchute.com/U8pFRoeI7dXM/6a3Iw7suM1TN.mp4'
r = requests.get(url, stream=True, verify=False)
infile = ffmpeg.input(r)
outfile = ffmpeg.output(infile, 'output.mp3')
ffmpeg.run(outfile)
r.close()