###############################################################
#################### user configuration #######################
interval = 600          # time interval default 600          ##
collection_id = 1465048 # siyuanxu wallpaper collection      ##
                        # you can just use mine              ##
img_width = 3000        # bigger than your screen width      ##
                        # default 2000                       ##
cache_num = 5           # how many pictures you want to keep ##
                        # default 5                          ##
#################### user configuration #######################
###############################################################

import os

os.system('pip install appscript')

# generate macosplash.py

python_path = os.popen('which python').read()
macosplash_path = os.getcwd()

usr_conf = '''
interval = {0}      
collection_id = {1} 
                    
img_width = {2}     
                    
cache_num = {3}

macosplash_path = '{4}'     
'''.format(interval,collection_id,img_width,cache_num,macosplash_path)

pyscript = '''
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
'''
with open('macosplash.py','w') as f:
    f.write('#!{}'.format(python_path))
    f.write(usr_conf)
    f.write(pyscript)


# generate plist
plistfile = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.siyuanxu.macosplash</string>
    <key>RunAtLoad</key>
    <true/>
    <key>ProgramArguments</key>
    <array> <string>{0}/macosplash.py</string>
    </array>
    <key>StartInterval</key>
    <integer>{1}</integer>
    <key>StandardErrorPath</key>
    <string>/tmp/com.siyuanxu.macosplash.err</string>
    <key>StandardOutPath</key>
    <string>/tmp/com.siyuanxu.macosplash.out</string>
</dict>
</plist>
'''.format(os.getcwd(),interval)

with open('macosplash.plist','w') as f:
    f.write(plistfile)

# give access
os.system('chmod u+x macosplash.py')

# copy plist file
os.system('''cp macosplash.plist ~/Library/LaunchAgents/macosplash.plist
cd ~/Library/LaunchAgents/
launchctl load macosplash.plist
''')

os.system('rm macosplash.plist')



