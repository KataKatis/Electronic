# Playing Don't Crash 2 with Joystick

The .ino file is the program in my Arduino Uno card and just read analogic inputs of the joystick HW-504 (VRx and VRy) and then print them in the serial port. The python program "read_serial.py" read what is returned by Arduino Uno in serial port with the serial module (which can be installed with `pip install pyserial`). It tests some conditions and presses Up, Down, Left or Right key (to play). The game is entitled **Don't Crash 2** ("Astéroides" in french") and was found on internet at this adress : https://codes-sources.commentcamarche.net/source/101845-don-t-crash-2

![circuit](https://raw.githubusercontent.com/KataKatis/Electronic/main/Joystick/Playing_dont_crash2_with_joystick/joystick_dont_crash_circuit.png)
