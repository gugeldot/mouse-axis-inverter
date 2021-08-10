import mouse  #https://github.com/boppreh/mouse https://pypi.org/project/mouse/
values =[]			#Queue of values to know orientation 
border_left = 1
border_right = 1278
while True:
	x, y = str(mouse.get_position()).split(',')
	xPosition = int(x[1:]) # Removing blank space and ')' from the y division	
	yPosition = int(y[1:-1])

	if xPosition < border_left: 
		mouse.move(1,yPosition,absolute=True)  			#Gets stuck on borders of the screen 
	elif xPosition > border_right:
		mouse.move(1275,yPosition,absolute=True)

	values.append(xPosition)
	if len(values) > 1: 
		result = int(values[0]) - int (values[-1])
		if result != 0 :
			#print ("Moving difference: " + str(result))
			mouse.move(((result+1)*2),0,absolute=False)
			values=[]		
		if len(values) > 2: 
			values.pop(0)


#Mouse X inverter by GreyNom 26/07/2021 
