import os
import string as string

def init():
	display = []
	row = []
	i = 0
	while i< 30:
		row.append(0)
		i+=1
	i = 0
	while i < 30:
		display.append(row)
		i+=1
	return display

def chunks(l,n):
	for i in range(0, len(l), n):
		yield l[i:i+n]

def load():
	d = open("./display1.disp").read().split()
	d = list(chunks(d, 30))
	return d

def save(arr):
	fl = ""
	for line in arr:
		for digit in line:
			fl += str(digit) + " "
	f = open("./display1.disp", "w")
	f.writelines(fl)

def setdisp(x,y,val):
	display = load()
	display[y][x] = val
	save(display)

def refresh():
	os.system("clear")
	display = load()
	pcol = ""
	for row in display:
		for col in row:
			if int(col) == 0:
				col = " "
			else:
				col = string.ascii_lowercase[int(col) - 1]
			pcol += str(col)
		print(pcol)
		pcol = ""
	
def call(reg, ext):
	# print(ext)
	if ext[2] == 0:
		enabled = False
	elif ext[2] == 1:
		enabled = True
		display = init()
		save(display)
	
	x = ext[5]
	y = ext[4]
	val = ext[3]
	
	setdisp(x,y,val)
	refresh()
	
	
	