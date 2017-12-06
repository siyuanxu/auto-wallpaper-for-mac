import sys
import os
import subprocess
import time

if sys.version_info[0] >= 3:
    from urllib.request import Request, urlopen
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib2 import Request, urlopen

import appscript

# clear cache
# at most five imgs can be stored here
img_list = [i for i in os.listdir('{}'.format(os.getcwd())) if i[-3:]=='jpg']
if len(img_list)>5:
    for i in img_list:
        os.remove(i)

# get a random img from collection 1460080
# change the collection number or you can just use mine
# also, you can view more demo on source.splash.com
# like
# pre_img_url = 'https://source.unsplash.com/random/1920x1080'
pre_img_url = 'https://source.unsplash.com/collection/1465048/random'
req = Request(pre_img_url)
response = urlopen(req)

# give the img name a time tag
# otherwise, macOS won't change the wallpaper if they have the same filename
img_name = 'unsplash{}.jpg'.format(time.time())
with open(img_name, "wb") as f:
    f.write(response.read())
# download complete, now we have a unsplash.jpg

# apple script
appscript.app('Finder').desktop_picture.set(appscript.mactypes.File(img_name))


