#Tuodaan kirjastoja käyttöön
from picamera import PiCamera
from time import sleep


#Luodaan camera-niminen ilmentymä eli olio PiCamera() funktiolla
my_camera=PiCamera()
my_camera.hflip=True
my_camera.vflip=True
my_camera.start_preview()
sleep(4)
my_camera.capture("image.jpg")
my_camera.stop_preview()