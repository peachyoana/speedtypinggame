#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gw15kolevaioana
#
# Created:     17/11/2020
# Copyright:   (c) gw15kolevaioana 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        # master = root
        self.master.title("A simple GUI") # set title of window
        self.master.geometry("800x550+300+200") # create window and center it on screen
        self.master['background']='#80ff00'

        self.label = Label(master, text="Choose your character: ")
        self.label.grid(row=1, columnspan=2, column=2)

        self.start_button = Button(master, text="Browse", command=self.start)
        self.start_button.grid(row=3, column=2)

        self.close_button = Button(master, text="Choose", command=master.quit)
        self.close_button.grid(row=3, column=3)

    def start(self):
        self.master = Tk()


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()