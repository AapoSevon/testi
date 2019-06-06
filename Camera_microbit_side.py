#ping_pong in microbit
from microbit import *
uart.init(baudrate = 115200)



while True:
    if button_a.is_pressed():
        uart.write(b"a")
        sleep(1500)
    if button_b.is_pressed():
        uart.write(b"b")
        sleep(1500)
       