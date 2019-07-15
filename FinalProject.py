print('Welcome to my game.')
print('Overview: \nYou have been captured and put in a room by kidnappers. \nYou must escape the room without alerting your abductors.\n\n')

game_running=True
round1= True
round2= True
round3= True
def End():
	exit()
def Third():
	while round3:
		print('1' ' - Run out together')
		print('2' ' - Climb out window')
		print('3' ' - Leave room and try to find other captives')
		t = int(input('Select 1-3 to Proceed '))
		if t == 1:
			print('// You escape. \nCONGRATULATIONS! \nYOU ARE FREE!')
			End()
		elif t == 2:
			print('// Window is locked. \nMake another choice.')
		elif t == 3:
			print('// The kidnappers are in the next room. \nGAME OVER')
			End()
		else:
			print('// PLEASE MAKE A VALID CHOICE')			
def Second():
	while round2:
		print('1' ' - Wake them up')
		print('2' ' - Walk back outside')
		z = int(input('Select 1-2 to Proceed '))
		if z == 1:
			print('// They are now awake and stand up')
			Third()
		elif z == 2:
			print('// Kidnappers see you. \nGAME OVER')
			End()
		else:
			print('// PLEASE MAKE A VALID CHOICE')	
def First():
	while round1:
		print('1' ' - Run to bathroom')
		print('2' ' - Run through front door')
		print('3' ' - Go to next room')
		y = int(input('Select 1-3 to Proceed '))
		if y == 1:
			print('// Theres a kidnapper there. \nGAME OVER')
			End()
		elif y == 2:
			print('// They saw you. \nGAME OVER')
			End()
		elif y == 3:
			print('// Theres another captive in the room sleeping')
			Second()
		else:
			print('// PLEASE MAKE A VALID CHOICE')
def thestart():	
	while game_running:
		input('Press Enter to Begin ')
		print('1' ' - Escape through window')
		print('2' ' - Escape through door')
		print('3' ' - Try to communicate with someone outside for help')

			
		x = int(input('Make your move ''(Select 1-3)'' '))
		if x == 1:
			print('// You alerted the kidnapper. \nGAME OVER')
			End()
		elif x == 2:
			print('// You are now in the hallway')
			First()
		elif x == 3:
			print('// Your phone made a sound when it turned on. \nGAME OVER')	
			End()
		else:
			print('// PLEASE MAKE A VALID CHOICE')
			
				

thestart()
