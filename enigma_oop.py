from tkinter import *
import string
import random


class Enigma(object):
	def __init__(self):
		self.root = Tk()
		self.root.counter, self.root.counter_1, self.root.counter_2 = 0, 0, 0
		self.root.title("Enigma OOP")
		self.true_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X' ,'Y', 'Z']
		self.alphabet = ['Q', 'W', 'E', 'R', 'T', 'Z', 'U', 'I', 'O', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'P', 'Y', 'X', 'C', 'V', 'B', 'N', 'M', 'L']
		self.create_keyboard()
		self.create_cylinders()
		self.QUIT = Button(self.root, text = "QUIT", command = self.root.quit).grid(column = 5)

	### making the yellow on click and the rotate function is called here
	def onClick(self, i):
		val = self.rotate(self.labels[i]['text'])
		self.labels[self.alphabet.index(val)].configure(bg = 'YELLOW')
		self.root.after(250, lambda: self.labels[self.alphabet.index(val)].configure(bg = 'WHITE'))
		#self.rotate(self.labels[i]['text'])


	### LOGIC PART OF ENIGMA IS ADDED TO ROTATE 
	
	def rotate(self, value_sent):
		self.val = []	
		self.val_0 = value_sent
		self.val.append(self.label['text'])
		self.val.append(self.label_1['text'])
		self.val.append(self.label_2['text'])

		try: 
				self.root.counter += 1
				self.label.configure(text = self.true_alphabet[self.root.counter])
		except:
			self.root.counter = 0
			self.label.configure(text = self.true_alphabet[0])
			self.next_1(0)
			if self.label_1['text'] == self.true_alphabet[0]:
				self.next_2(0)

		value = self.enigma_brain(self.val_0, self.val)
		return value

	### making the main keyboard layout  ###
	## _________START_________##
	labels = []
	buttons = []

	def create_keyboard(self):
		for i in self.alphabet:
			self.create_label_and_buttons(i, self.alphabet.index(i))

		for i in range(26):
			if i <= 8:
				self.labels[i].grid(row = 2, column = i)
				self.buttons[i].grid(row = 5, column = i)
			elif 8 < i <= 16:
				self.labels[i].grid(row = 3, column = i-8)
				self.buttons[i].grid(row = 6, column = i-8)
			else:
				self.labels[i].grid(row = 4, column = i-17)
				self.buttons[i].grid(row = 7, column = i-17)

	def create_label_and_buttons(self, text, index):
		self.labels.append(Label(self.root, text = text, padx = 20, pady = 20, borderwidth = 3, relief = 'ridge'))
		self.buttons.append(Button(self.root, text = text, padx = 20, pady = 20, borderwidth = 3, relief = 'ridge', command = lambda: self.onClick(index)))

	## ______________END_____________ ##

	### making the rotating cylinders ###
	## ____________START______________##

	def next(self, i):
		try:
			if i == 0:
				self.root.counter += 1
				self.label.configure(text = self.true_alphabet[self.root.counter])
			else:
				self.root.counter -= 1
				self.label.configure(text = self.true_alphabet[self.root.counter])
		except:
			self.root.counter = 0
			self.label.configure(text = self.true_alphabet[self.root.counter])
	def next_1(self, i):
		try:
			if i == 0:
				self.root.counter_1 += 1
				self.label_1.configure(text = self.true_alphabet[self.root.counter_1])
			else:
				self.root.counter_1 -= 1
				self.label_1.configure(text = self.true_alphabet[self.root.counter_1])
		except:
			self.root.counter_1 = 0
			self.label_1.configure(text = self.true_alphabet[self.root.counter_1])
	def next_2(self, i):
		try:
			if i == 0:
				self.root.counter_2 += 1
				self.label_2.configure(text = self.true_alphabet[self.root.counter_2])
			else:
				self.root.counter_2 -= 1
				self.label_2.configure(text = self.true_alphabet[self.root.counter_2])
		except:
			self.root.counter_2 = 0
			self.label_2.configure(text = self.true_alphabet[self.root.counter_2])

	def create_cylinders(self):
		self.label = Label(self.root, text = self.true_alphabet[0])
		self.label.grid(row = 1, column = 2)

		self.button_right = Button(self.root, text = ">", command = lambda: self.next(0)).grid(row = 1, column = 1)
		self.button_left = Button(self.root, text = "<", command = lambda: self.next(1)).grid(row = 1, column = 3)

		self.label_1 = Label(self.root, text = self.true_alphabet[0])
		self.label_1.grid(row = 1, column = 5)

		self.button_right_1 = Button(self.root, text = ">", command = lambda: self.next_1(0)).grid(row = 1, column = 4)
		self.button_left_1 = Button(self.root, text = "<", command = lambda: self.next_1(1)).grid(row = 1, column = 6)

		self.label_2 = Label(self.root, text = self.true_alphabet[0])
		self.label_2.grid(row = 1, column = 8)

		self.button_right_2 = Button(self.root, text = ">", command = lambda: self.next_2(0)).grid(row = 1, column = 7)
		self.button_left_2 = Button(self.root, text = "<", command = lambda: self.next_2(1)).grid(row = 1, column = 9)

	## _____________END______________##
	### The LOGIC PART BEGINS NOW
	## ______________START_____________##
	random_rotors = []
	def create_random_rotors(self, i):
		random.seed(i)
		self.random_rotors.append(random.sample(self.true_alphabet, len(self.true_alphabet)))

	connect_back_rotors = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']

	def calc_value(self, var, rotor_name):
		value = self.true_alphabet.index(var)
		letter = rotor_name[value]
		return letter

	def connect_back(self, value):
		value = self.true_alphabet.index(value)
		letter = self.connect_back_rotors[value]
		return letter

	def reverse(self, value, rotor_name):
		value = self.true_alphabet[rotor_name.index(value)]
		return value

	def enigma_brain(self, val_0, val_list):
		for i in range(3):
			self.create_random_rotors(i)
		rotors = []
		for i in range(3):
			rotors.append(self.random_rotors[i][self.true_alphabet.index(self.val[i]):] + self.random_rotors[i][:self.true_alphabet.index(self.val[i])])
			#print(''.join(map(str, self.random_rotors[i][self.true_alphabet.index(self.val[i]):] + self.random_rotors[i][:self.true_alphabet.index(self.val[i])])))
		value = self.val_0

		for i in rotors:
			value = self.calc_value(value, i)
		value = self.connect_back(value)
		for i in reversed(rotors):
			value = self.reverse(value, i)

		return value
	## ___________END________________##
	
	def last_fn(self):
		self.root.mainloop()


enigma = Enigma()
enigma.last_fn()