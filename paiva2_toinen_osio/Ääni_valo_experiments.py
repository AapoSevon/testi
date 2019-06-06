from microbit import *
import neopixel
import time

num_pixels = 24
pixels = neopixel.NeoPixel(pin0, num_pixels)

uart.init(baudrate = 115200)

def update_pixels(r, g, b): #red green blue        range: 0-255
    global pixels
    for i in range(24):
        pixels[i+(i % 2)] = (r, g, b)
        sleep(100)  #10 ms
        pixels.show()
        
# wheel function
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b)

# rainbow animation
def rainbow_cycle(wait):
    global num_pixels
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep_ms(wait)

# bounce animation
def bounce(r, g, b, wait):
    global pixels
    global num_pixels
    for i in range(2 * num_pixels):
        for j in range(num_pixels):
            pixels[j] = (r, g, b)
        if (i // num_pixels) % 2 == 0:
            pixels[i % num_pixels] = (0, 0, 0)
        else:
            pixels[num_pixels - 1 - (i % num_pixels)] = (0, 0, 0)
        pixels.show()
        time.sleep_ms(wait)

#cycle animation
def cycle(r, g, b, wait):
    global pixels
    global num_pixels
    for i in range(num_pixels):
        for j in range(num_pixels):
            pixels[j] = (0, 0, 0)
        pixels[i % num_pixels] = (r, g, b)
        pixels.show()
        time.sleep_ms(wait)

# Almost same as update pixels
def colorWipe(r, g, b, wait):
    global pixels
    global pixes
    for j in range(num_pixels):
        pixels[j] = (r, g, b)
        pixels.show()
        time.sleep_ms(wait)

# rainbow function goes through colors
def rainbow(wait):
    global num_pixels
    global pixels
    for j in range(255):
        for i in range(num_pixels):
            idx = int(i + j)
            pixels[i] = wheel(idx & 255)
            pixels.show()
        time.sleep_ms(wait)


while True:

    """update_leds(255, 0, 0)
    time.sleep(2000)
    
    update_leds(0, 255, 0)
    time.sleep(2000)"""
    
    
    """update_pixels(32,32,32) # white
    time.sleep(2)
    update_pixels(255, 0, 0) # red
    time.sleep(2)

    update_pixels(0, 255, 0) # green
    time.sleep(2)

    update_pixels(0, 0, 255) # blue
    time.sleep(2)


    rainbow(50)
    colorWipe(0, 255,0, 100) # r,g,b-values and wait 100 ms

    rainbow_cycle(10)    # rainbow cycle with 10 ms delay. scan all colors

    bounce(255, 0, 0, 200) # r, g, b values and wait 200 ms.

    cycle(0, 0, 255, 200)""" # r, g, b values and wait 200 ms
    
    message_bytes = uart.read()
    message = str(message_bytes)[2:-1]
    
    if  "a" in message:
        update_pixels(255, 0, 0)
    
    elif "b" in message:
        rainbow_cycle(5)
    
    elif "c" in message:
        bounce(255, 0, 0, 5)
    
    elif "d" in message:
        cycle(50, 200, 100, 200)
        
    elif "e" in message:
        colorWipe(0, 255,0, 100)
    
    update_pixels(0, 0, 0)

