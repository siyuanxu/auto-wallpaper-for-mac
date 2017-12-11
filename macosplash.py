#!/Users/siyuan/miniconda2/bin/python

interval = 600      
collection_id = 1465048 
                    
img_width = 3000     
                    
cache_num = 5

macosplash_path = '/Users/siyuan/Dropbox/github/macosplash'     

import sys
import os
import re
import time

if sys.version_info[0] >= 3:
    from urllib.request import Request, urlopen
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib2 import Request, urlopen

# clear the oldest picture to save space
path = str(macosplash_path)+r'/wallpaper_cache/'
img_list = [i for i in os.listdir(path) if i[-3:]=='jpg']
if len(img_list)>cache_num-1:
    os.remove('{0}/{1}'.format(path,img_list[0]))

# url treatment
pre_img_url = 'https://source.unsplash.com/collection/{}'.format(collection_id)
req = Request(pre_img_url)
response = urlopen(req)
real_url = response.geturl()


# set a bigger resolution
pattern = re.compile(r'w=\d+')
split_url = pattern.split(real_url)
larger_size = ''.join([split_url[0],'w={}'.format(img_width),split_url[1]])
response = urlopen(larger_size)

# give the img name a time tag
# otherwise, macOS won't change the wallpaper if they have the same filename
img_name = '{0}/wallpaper_cache/unsplash{1}.jpg'.format(macosplash_path, time.time())

# generally, urlretrieve was used to download files 
# but it has some issues when we have an unstable network condition
with open(img_name, "wb") as f:
    f.write(response.read())

# use apple script to set wallpaper
import appscript
appscript.app('Finder').desktop_picture.set(appscript.mactypes.File(img_name))
