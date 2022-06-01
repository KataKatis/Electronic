import pyautogui as ptg
from time import sleep

ptg.FAILSAFE = False
counter = 0
previous_click_state = 1

while True:
	with open("CoolTermtest1.txt", "r") as file:
		counter += 1
		reader = file.readlines()
		line = reader[-2].split(" ")
		line[-1] = line[-1][0]  # keep only 0 or 1 and not the \n
		position = list(ptg.position())
		actual_click_state = int(line[-1])


		print(str(counter) + "  :  " + "".join(line)[:-1] + "  |  " + line[1] + " " + line[3] + "    ", end="\r")
		

		if int(line[1]) < 490 and int(line[3]) < 500: 		# bas gauche
			ptg.moveTo(position[0]-30, position[1]+30, 0.1)

		elif int(line[1]) > 510 and int(line[3]) < 500:		# haut gauche
			ptg.moveTo(position[0]-30, position[1]-30, 0.1)

		elif int(line[1]) > 510 and int(line[3]) > 520:		# haut droite
			ptg.moveTo(position[0]+30, position[1]-30, 0.1)

		elif int(line[1]) < 490 and int(line[3]) > 520:		# bas droite
			ptg.moveTo(position[0]+30, position[1]+30, 0.1)

		elif int(line[1]) < 490: 							# bas
			ptg.moveTo(position[0], position[1]+30, 0.1)

		elif int(line[3]) < 500: 							# gauche
			ptg.moveTo(position[0]-30, position[1], 0.1)

		elif int(line[1]) > 510:							# haut
			ptg.moveTo(position[0], position[1]-30, 0.1)

		elif int(line[3]) > 520:							# droite
			ptg.moveTo(position[0]+30, position[1], 0.1)

		if actual_click_state == 1 and actual_click_state != previous_click_state:
			ptg.click()


		previous_click_state = int(line[-1])


		"""
		elif int(line[1]) < 490:
			ptg.moveTo(position[0], position[1]+30, 0.1)
		if int(line[3]) > 520:
			ptg.moveTo(position[0]+30, position[1], 0.1)
		elif int(line[3]) < 500:
			ptg.moveTo(position[0]-30, position[1], 0.1)
		"""

		file.close()
