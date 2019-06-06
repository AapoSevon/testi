#!/usr/bin/python3
import iot
import io
import serial

ser = serial.Serial('/dev/ttyACM0', timeout=1, baudrate=115200)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

# Kuuntele sanaa "hello", ja vastaa "Hello, world!" 
@iot.listen("Red led")
def red_led():
    ser.write(b"a")
    print("lähetettiin komento a")
    iot.say("Deploying red LED")
    #iot.publish("messages","blue")
    
@iot.listen("rainbow cycle")
def rainbow_cycle():
    print("lähetettiin komento b")
    iot.say("Deploying rainbow cycle")
    ser.write(b"b")
    #iot.say("OK, sparkle")

@iot.listen("bounce")
def bounce():
    print("lähetettiin komento c")
    iot.say("Deploying bounce")
    ser.write(b"c")
    iot.publish("messages","green")
    #iot.say("Asking the car to move backward")
    
@iot.listen("cycle")
def cycle():
    print("lähetettiin komento d")
    iot.say("Deploying cycle")
    ser.write(b"d")
    iot.publish("messages","green")

@iot.listen("color wipe")
def cycle():
    print("lähetettiin komento e")
    iot.say("Deploying wipe")
    ser.write(b"e")
    iot.publish("messages","green")
    
@iot.listen("blue star")
def said_left():
    iot.publish("messages","blue")
    
@iot.listen("red star")
def said_left():
    iot.publish("messages","red")
    

@iot.listen("green glitter")
def said_back():
    iot.publish("messages","green glitter")

@iot.listen("red glitter")
def said_back():
    iot.publish("messages","red glitter")

@iot.listen("blue glitter")
def said_back():
    iot.publish("messages","green glitter")

@iot.listen("rainbow")
def said_back():
    iot.publish("messages","rainbow")
    
    
@iot.listen("no light")
def said_right():
    iot.publish("messages","nolight")
    #iot.say("Asking the car to move right")


@iot.listen("no light")
def said_nolight():
    iot.publish("messages","nolight")

@iot.listen("How are you")
def said_How_are_you():
    iot.say("I'm good. Thank you for asking ")

iot.run("voice1","shiftr-key","shiftr-secret")


