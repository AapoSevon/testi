#!/usr/bin/python3
import iot
import time

# Kuuntele sanaa "hello", ja vastaa "Hello, world!" 
@iot.subscribe("data_Aapo")
def testi(message):
    print(message)
    distance = float(message)
    if distance < 20.0:
        iot.say("Obstacle warning!")
        time.sleep(4)

iot.run("vastaanottaja_Aapo","aalto-shiftr-testi","aalto-shiftr-testi")

while True:
    pass

