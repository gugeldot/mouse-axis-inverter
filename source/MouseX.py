from mouse import hook,move				#https://github.com/boppreh/mouse
from keyboard import wait				#https://github.com/boppreh/keyboard
queue=[]

def main(raw):
	if str(raw)[0:1] == "B": 
		pass 
	else:
		x = float(str(str(raw)[10:-1].split(",")[0]).split("=")[1])
		y = float(str(str(raw)[10:-1].split(",")[1]).split("=")[1])
		queue.append(x)
		if len(queue) > 3:
			queue.pop(0)
			print(queue)
		elif len(queue) >1:
			result = float(queue[0]) - float (queue[1])	
			print(queue, result)
			move((result*2),0,absolute=False)
			queue.clear()
		
hook(main)
wait()

#GN sign 