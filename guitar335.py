import pynput
import serial
import sys
from pynput.keyboard import Key, Controller

#Change this to the port where the controller is plugged in
port = "COM7"

#Set these to the buttons you want pressed
input_1 = 'a'
input_2 = 's'
input_3 = 'd'
input_4 = 'f'
input_5 = 'g'
input_up = Key.up
input_down = Key.down
input_pause = Key.enter
input_whammy = Key.ctrl_r
input_star = 'v'

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
                keyboard.press(input_1)
                print("Key "+ input_1 +" pressed")
            elif data == 'a!':
                keyboard.release(input_1)
                print("Key "+ input_1 +" released")
            elif data == 's':
                keyboard.press(input_2)
                print("Key "+ input_2 +" pressed")
            elif data == 's!':
                keyboard.release(input_2)
                print("Key "+ input_2 +" released")
            elif data == 'd':
                keyboard.press(input_3)
                print("Key "+ input_3 +" pressed")
            elif data == 'd!':
                keyboard.release(input_3)
                print("Key "+ input_3 +" released")
            elif data == 'f':
                keyboard.press(input_4)
                print("Key "+ input_4 +" pressed")
            elif data == 'f!':
                keyboard.release(input_4)
                print("Key "+ input_4 +" released")
            elif data == 'g':
                keyboard.press(input_5)
                print("Key "+ input_5 +" pressed")
            elif data == 'g!':
                keyboard.release(input_5)
                print("Key "+ input_5 +" released")
            elif data == 'h':
                keyboard.press(input_up)
                keyboard.release(input_up)
                print("Key UP pressed")
            elif data == 'j':
                keyboard.press(input_down)
                keyboard.release(input_down)
                print("Key DOWN pressed")
            elif data == 'p':
                keyboard.press(input_pause)
                keyboard.release(input_pause)
                print("Key PAUSE pressed")
            elif data == 'c':
                keyboard.press(input_whammy)
                keyboard.release(input_whammy)
                print("Key WHAMMY pressed")
            elif data == 'v':
                keyboard.press(input_star)
                keyboard.release(input_star)
                print("Key STAR pressed")
    except:
        print("Lost connection to serial port")
    sys.exit(0)

main()