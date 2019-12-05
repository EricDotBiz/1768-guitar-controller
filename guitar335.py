import pynput
import serial
import sys
from pynput.keyboard import Key, Controller

#Change this to the port where the controller is plugged in
port = "COM6"

def main():
    #Attempt to connect to serial
    s = None
    try:
        s = serial.Serial(port)
    except:
        print("Could not open serial port.")
        sys.exit(1)

    print("Serial port " + port + " opened. Listening for input...")
    keyboard = Controller()

    #Listen to input
    try:
        while 1:
            data = str(s.readline())
            data = data[4:len(data)-3]
            if data == 'a':
                keyboard.press('a')
                print("Key 'a' pressed")
            elif data == 'a!':
                keyboard.release('a')
                print("Key 'a' released")
            elif data == 's':
                keyboard.press('s')
                print("Key 's' pressed")
            elif data == 's!':
                keyboard.release('s')
                print("Key 's' released")
            elif data == 'd':
                keyboard.press('d')
                print("Key 'd' pressed")
            elif data == 'd!':
                keyboard.release('d')
                print("Key 'd' released")
            elif data == 'f':
                keyboard.press('f')
                print("Key 'f' pressed")
            elif data == 'f!':
                keyboard.release('f')
                print("Key 'f' released")
            elif data == 'g':
                keyboard.press('g')
                print("Key 'g' pressed")
            elif data == 'g!':
                keyboard.release('g')
                print("Key 'g' released")
    except:
        print("Lost connection to serial port")
    sys.exit(0)

main()