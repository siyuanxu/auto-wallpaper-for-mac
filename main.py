import sys
import os
import subprocess

if sys.version_info[0] >= 3:
    from urllib.request import Request, urlopen
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib2 import Request, urlopen

import appscript

# get a random img from collection 1460080
# change the collection number or you can just use mine
# also, you can view more demo on source.splash.com
pre_img_url = 'https://source.unsplash.com/collection/1460080/1920x1080'
req = Request(pre_img_url)
response = urlopen(req)
with open('unsplash.jpg', "wb") as f:
    f.write(response.read())
# download complete, now we have a unsplash.jpg

# apple script
appscript.app('Finder').desktop_picture.set(appscript.mactypes.File('unsplash.jpg'))