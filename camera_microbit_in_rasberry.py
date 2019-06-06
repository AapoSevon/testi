#tuodaan kirjastoja käyttöön
from picamera import PiCamera 
from time import sleep

import time
import io
import serial

ser = serial.Serial('/dev/ttyACM0', timeout=1, baudrate=115200)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))


# Luodaan camera-niminen ilmentymä eli olio PiCamera() funktiolla
my_camera=PiCamera()
my_camera.hflip = True
my_camera.vflip = True

def take_photo():
    global my_camera
    my_camera.start_preview()
    sleep(4)
    my_camera.capture('image.jpg') # nyt otetaan valokuva
    my_camera.stop_preview()

def take_video (duration=5):
    global my_camera
    with open("video.h264","wb") as capture_file:
        #my_camera.resolution = (1296, 972)
        my_camera.framerate = 24
        my_camera.start_recording(capture_file)
        my_camera.wait_recording(duration)
        my_camera.stop_recording()

def main():
    try:
    #ser.write(b'bong')
        while True:
            serial_in = str(sio.readline())
            print('Found in serial: ' + serial_in)
            if 'a' in serial_in:
                take_photo()
            elif "b" in serial_in:
                take_video()

    except KeyboardInterrupt:
        ser.close()
        print('Ohjelman suoritus paattyy.')


main()

