import RPi.GPIO as GPIO
from subprocess import call
import time
import datetime
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def write_to_file(name, data):
    f = open(name,'w')
    for d in data:
        f.write(d+'\n')
data = []
motion_sleep = 0.5
display_time = 30
counter = 0
call(["./webcam.sh"])
print ('motion detector is running')
while True:
    counter = counter +1
    if GPIO.input(4):
        data.append('MOTION DETECTED!! at '+str(datetime.datetime.now())[:-7])
        call(["./webcam.sh"])
        time.sleep(10)
    else:
        if counter*motion_sleep > display_time:
            data.append('no motion detected at '+str(datetime.datetime.now())[:-7])
            counter = 0

    if len(data) > 10:
        del data[0]
    write_to_file('motion.txt', data)
    time.sleep(0.5)




