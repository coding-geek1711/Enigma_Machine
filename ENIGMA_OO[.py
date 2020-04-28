import tkinter as tk


class myGUI(object):

    alphabet = ['Q', 'W', 'E', 'R', 'T', 'Z', 'U', 'I', 'O', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'P', 'Y', 'X', 'C', 'V', 'B', 'N', 'M', 'L']

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ENIGMA")
        self.window.geometry('800x600')

    def create_label(self, text):
        return Label(self.window, text = self.text, padx = 20, pady = 20, borderwidth = 3, relief = 'ridge')
    def create_button(self, text, i):
        self.Button(self.window, text = self.text, padx = 20, pady = 20, command = lambda: onClick(self.i))

    labels = []
    buttons = []


    for i in alphabet:
        labels.append(create_label(i))
        buttons.append(create_button(i, alphabet.index(i)))

    for i in range(26):
        if i < 9:
            buttons[i].grid(row=5, column=i)
            labels[i].grid(row=1, column=i)
        elif i >= 9 and i <= 16:
            buttons[i].grid(row=6, column=i - 8)
            labels[i].grid(row=2, column=i - 8)
        elif i > 16 and i < 26:
            buttons[i].grid(row=7, column=i - 17)
            labels[i].grid(row=3, column=i - 17)


root = myGUI()