from gpiozero import LED, Button
from time import sleep
from datetime import datetime
from signal import pause
import os

# Setup our inputs
dt = datetime.now().strftime('%H-%M-%S')
      
def print_menu():       ## Your menu design here
    print 30 * "-" , "TESTS" , 30 * "-"
    print "1. Standard Photo"
    print "2. Resizing Photo"
    print "3. Exit"
    print 67 * "-"
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-3]: ")
     
    if choice==1:     
        print "Taking a standard test photo..."
        os.system("fswebcam -d /dev/video0 -r 1024x768 -S 30 --jpeg 85 --title 'Standard Test' --line-colour '#00000000' --banner-colour '#002CA3FE' -F 5 '/mnt/camera/Tests/Standard %s.jpg'" % (dt))
        print "Complete"
        print "."
        print ".."
        print "..."
        ## You can add your code or functions here
    elif choice==2:
        resize_1 = raw_input('Resize to: ')
        resize_2 = raw_input('Crop at: ')
        resize = ("%s,%s") % (resize_1, resize_2) 
        fswebcam_resize = ("Resizing Test: %s") % (resize)
        print "Taking photo at: %s" % (resize)
        os.system("fswebcam -d /dev/video0 -r 1024x768 -S 30 --jpeg 85 --title '%s' --crop '%s' --line-colour '#00000000' --banner-colour '#002CA3FE' -F 5 '/mnt/camera/Tests/Resize %s %s.jpg'" % (fswebcam_resize, resize, resize, dt))
        print "Complete"
        print "."
        print ".."
        print "..."
        ## You can add your code or functions here
    elif choice==3:
        print "Exiting"
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")