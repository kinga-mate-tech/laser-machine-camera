from gpiozero import LED, Button
from time import sleep
from datetime import datetime
from signal import pause
import os

# Setup our inputs
btn = Button(6)
ledCapture = LED(13)
camera_id = 'MachineXX'
directory = '/mnt/camera'
usbcamera = '/dev/video0'
colour_code = '#00FFFFFF'
line_colour = '#00000000'
crop = '1024x768,0x0'

while True:
    # waiting for button to be pressed
    btn.wait_for_press()
    # we specify the date for the new file
    dt = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    # notify progress
    print('Taking photo %s.jpg' % dt)
    # LED turns on
    ledCapture.on()
    os.system("fswebcam -d %s -r 1024x768 -S 30 --jpeg 85 --title %s --crop '%s'  --line-colour '%s' --banner-colour '%s' -F 5 %s/%s/%s.jpg" % (usbcamera, camera_id, crop,  line_colour, colour_code, directory, camera_id, dt))
    print('Photo Captured')
    sleep (1)
    print('Organising')
    os.system("classifier -dt -d %s/%s" % (directory, camera_id))
    sleep(2)
    print('Done')
    # LED turns off
    ledCapture.off()
