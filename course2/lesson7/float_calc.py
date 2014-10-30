#!/usr/bin/env python3

from tkinter import *

class Application(Frame):
    """Application main window class."""
    def __init__(self, master=None):
        """Main frame initialization"""
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        """Add all the widgets to the main frame."""
        top_frame = Frame(self)
        self.input_1 = Entry(top_frame)
        self.input_2 = Entry(top_frame)
        self.label = Label(top_frame, text="Float calculation")
        self.input_1.pack()
        self.input_2.pack()
        self.label.pack()
        
        top_frame.pack(side=TOP)
        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
        
        self.QUIT = Button(bottom_frame, text="Quit", command=self.quit)
        self.QUIT.pack(side=LEFT)
        self.handleb = Button(bottom_frame, text="Convert and calculate", command=self.handle)
        self.handleb.pack(side=LEFT)

    def handle(self):
        """Convert the input to a float if possible or send Error to the label"""
        input_1 = self.input_1.get()
        input_2 = self.input_2.get()
        output = "***ERROR****"
        try:
            input_1 = float(input_1)
            input_2 = float(input_2)
            self.label.config(text=input_1 + input_2)
        except:
            self.label.config(text=output)  
root = Tk()
app = Application(master=root)
app.mainloop()