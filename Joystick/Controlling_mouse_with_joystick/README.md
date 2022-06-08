# Controlling_mouse_with_joystick

This project is a first electronic's test. The goal is to try to control mouve of mouse (up, down, left, right, leftclick) with a HW-504 joystick and a arduino uno card.

A joystick (for me the reference is HW-504) is connected on an arduino card (personnaly I use arduino uno). The joystick is powered in 5V and the push button in 3.3V. Both are connected to a earth. The 2 outputs of the joystick ("VRx" and "VRy") are connected on A0 and A1 inputs of the card and pin2 of the card is connected after the push button to know if we click. The little program in arduino take care of pick the joystick's values (between 0 and 1023) and push button state.

![circuit](https://raw.githubusercontent.com/KataKatis/Electronic/main/Joystick/Controlling_mouse_with_joystick/joystick_circuit2.png)

To export data's from serial port I use CoolTermWin, a free software, and I record datas in a text file (it could be coded in python but it is not the subject here). During the record an other python program is runnig on computer to pick in the text file values it needs.

The python program uses the `autopygui` and `time` modules. With `autopygui` we can control the position of the mouse, when to click... 
