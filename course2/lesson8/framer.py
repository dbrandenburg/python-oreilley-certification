#!/usr/bin/env python3

from tkinter import *

ALL = N+S+W+E

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        
        self.rowconfigure(0, weight=1)
        Label(self, text="Frame {0}".format(1),bg="red").grid(row=0, column=0, sticky=ALL, columnspan=2)
        self.rowconfigure(1, weight=1)
        Label(self, text="Frame {0}".format(2),bg="green").grid(row=1, column=0, sticky=ALL, columnspan=2)
        self.rowconfigure(5, weight=2)
        Label(self, text="Frame {0}".format(3),bg="yellow").grid(row=0, column=2, sticky=ALL, rowspan=2, columnspan=3)
        self.rowconfigure(5, weight=1)
        
        for c in range(5):
            self.columnconfigure(c, weight=1)
            Button(self, text="Col {0}".format(c)).grid(row=2, column=c, sticky=ALL)
root = Tk()
app = Application(master=root)                
app.mainloop()