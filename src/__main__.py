import os
import string as string

letters_numbers = {
	" ":0,
	"a":1,
	"b":2,
	"c":3,
	"d":4,
	"e":5,
	"f":6,
	"g":7,
	"h":8,
	"i":9,
	"j":10,
	"k":11,
	"l":12,
	"m":13,
	"n":14,
	"o":15,
	"p":16,
	"q":17,
	"r":18,
	"s":19,
	"t":20,
	"u":21,
	"v":22,
	"w":23,
	"x":24,
	"y":25,
	"z":26,
	":":27,
	"1":28,
	".":29,
	"0":30
}

numbers_letters = {
	0:" ",
	1:"a",
	2:"b",
	3:"c",
	4:"d",
	5:"e",
	6:"f",
	7:"g",
	8:"h",
	9:"i",
	10:"j",
	11:"k",
	12:"l",
	13:"m",
	14:"n",
	15:"o",
	16:"p",
	17:"q",
	18:"r",
	19:"s",
	20:"t",
	21:"u",
	22:"v",
	23:"w",
	24:"x",
	25:"y",
	26:"z",
	27:":",
	28:"1",
	29:".",
	30:"0"
}

def init():
	display = []
	row = []
	i = 0
	while i< 80:
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
	d = list(chunks(d, 80))
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
	# print(string.ascii_lowercase[int(val - 1)])
	# print(val)
	if type(val) == type("hi"):
		for char in val:
			display[y][x] = letters_numbers[char]
			x += 1
	else:
		display[y][x] = val
	save(display)

def refresh():
	os.system("clear")
	display = load()
	pcol = ""
	rown = 0
	coln = 0
	
	for row in display:
		for col in row:
			if int(col) == 0:
				col = " "
			else:
				col = numbers_letters[int(col)]
			pcol += str(col)
			# print("\033["+ str(rown) +";"+ str(coln) +"H" + str(col))
			coln +=1
		# print( "\u001b[0m" + pcol + "\u001b[30m\u001b[47m")
		print(pcol)
		pcol = ""
		rown += 1
	
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
	
	if ext[2] != 0:
		setdisp(x,y,val)
		refresh()
	
	
	