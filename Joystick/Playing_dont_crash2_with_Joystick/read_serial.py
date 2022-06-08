import serial
import threading
import keyboard as kb
from time import sleep

serialPort = serial.Serial(port="COM4", baudrate=9600, bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE)
sleep(0.5)


def get():
    try:
        result = serialPort.readline()
        result = result.decode("Ascii")
        result = (int(result.split(" ")[1]), int(result.split(" ")[3]))
    except:
        result = get()

    return result


def main():
    while True:
        if get()[0] > 600 and get()[1] > 600:
            kb.press("Up")
            kb.press("Right")
            while get()[0] > 600 and get()[1] > 600:
                None
            kb.release("Up")
            kb.release("Right")

        elif get()[0] > 600 and get()[1] < 500:
            kb.press("Down")
            kb.press("Right")
            while get()[0] > 600 and get()[1] < 500:
                None
            kb.release("Down")
            kb.release("Right")

        elif get()[0] < 500 and get()[1] < 500:
            kb.press("Down")
            kb.press("Left")
            while get()[0] < 500 and get()[1] < 500:
                None
            kb.release("Down")
            kb.release("Left")

        elif get()[0] < 500 and get()[1] > 600:
            kb.press("Up")
            kb.press("Left")
            while get()[0] < 500 and get()[1] > 600:
                None
            kb.release("Up")
            kb.release("Left")

        elif get()[0] < 500:
            kb.press("Left")
            while get()[0] < 500 and 500 < get()[1] < 600:
                None
            kb.release("Left")

        elif get()[0] > 600:
            kb.press("Right")
            while get()[0] > 600 and 500 < get()[1] < 600:
                None
            kb.release("Right")

        elif get()[1] < 500:
            kb.press("Down")
            while get()[1] < 500 and 500 < get()[0] < 600:
                None
            kb.release("Down")

        elif get()[1] > 600:
            kb.press("Up")
            while get()[1] > 600 and 500 < get()[0] < 600:
                None
            kb.release("Up")

main()



"""
def get_Y():
	try:
		result = serialPort.readline()
		result = result.decode('Ascii')
		result = int(result.split(" ")[3])
	except:
		result = get_Y()

	return result

def get_X():
	try:
		result = serialPort.readline()
		result = result.decode("Ascii")
		result = int(result.split(" ")[1])
	except:
		result = get_X()

	return result

def Y_Axis():
    while True:
        if get_Y() > 600:
            kb.press("Up")
            while get_Y() > 600:
                None
            kb.release("Up")
        elif get_Y() < 500:
            kb.press("Down")
            while get_Y() < 500:
                None
            kb.release("Down")

def X_Axis():
    while True:
        print(get_X())
        if get_X() < 500:
            kb.press("Left")
            while get_X() < 500:
                None
            kb.release("Left")
        elif get_X() > 600:
            kb.press("Right")
            while get_X() > 600:
                None
            kb.release("Right")


thread1 = threading.Thread(target=X_Axis)
thread2 = threading.Thread(target=Y_Axis)
 
thread1.start()
thread2.start()

"""