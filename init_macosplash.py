import os
import shutil

plistfile = '''
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.denglibing.checkin</string>
    <key>RunAtLoad</key>
    <true/>
    <key>ProgramArguments</key>
    <array> <string>{}macosplash.sh</string>
    </array>
    <key>StartCalendarInterval</key>
    <array>
        <dict>
            <key>Minute</key>
            <string>15</string>
        </dict>
        <dict>
            <key>Minute</key>
            <string>30</string>
        </dict>
        <dict>
            <key>Minute</key>
            <string>45</string>
        </dict>
        <dict>
            <key>Minute</key>
            <string>01</string>
        </dict>
    </array>
</dict>
</plist>
'''.format(os.getcwd())

with open('macosplash.plist','w') as f:
    f.write(plistfile)