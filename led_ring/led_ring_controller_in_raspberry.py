import time
import io
import serial

ser = serial.Serial('/dev/ttyACM0', timeout=1, baudrate=115200)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

try:
    #ser.write(b'bong')
    while True:
        print("komennot: a-rainbow, b-rainbowcycle, c-bounce")
        command = input("Anna komento\n" )
        
        if "a" in command:
            ser.write(b"a")
            print("lähetettiin komento a")
        elif "b" in command:
            ser.write(b"b")
            print("lähetettiin komento b")
        elif command == "c":
            ser.write (b"c")
            print("lähetettiin komento c")
        else:
            print("Virheellinen komento")

except KeyboardInterrupt:
    ser.close()
    print('Ohjelman suoritus paattyy.')