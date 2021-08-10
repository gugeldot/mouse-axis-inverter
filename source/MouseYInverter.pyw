import mouse 
vals =[]			#Queue of vals to know orientation 
border_left = 1
border_right = 718
while True:
	x, y = str(mouse.get_position()).split(',')
	xPosition = int(x[1:]) # Removing blank space and ')' from the y division	
	yPosition = int(y[1:-1])

	if yPosition < border_left: 
		mouse.move(xPosition,1,absolute=True)  			#Gets stuck on borders of the screen 
	elif yPosition > border_right:
		mouse.move(xPosition,716,absolute=True)

	vals.append(yPosition)
	if len(vals) > 1: 
		result = int(vals[0]) - int (vals[-1])
		if result != 0 :
			mouse.move(0,((result+1)*2),absolute=False)
			vals=[]		
		if len(vals) > 2: 
			vals.pop(0)


#Mouse Y inverter by GreyNom 26/07/2021 
############################################################3