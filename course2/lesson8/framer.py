#!/usr/bin/env python3

from tkinter import *

ALL = N+S+W+E

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(sticky=ALL)
        self.master.title("Framer")
        
        for r in range(2):
             self.master.rowconfigure(r, weight=1)    
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            Button(master, text="Button {0}".format(c+1)).grid(row=2,column=c,sticky=E+W)        
        
        top_frame = Frame(master, bg="red", height=100)
        top_frame.grid(row=0, column=0,columnspan=2, sticky=ALL)
   
        bottom_frame = Frame(master, bg="green",height=100)
        bottom_frame.grid(row=1, column=0,columnspan=2, sticky=ALL)

        main_frame = Frame(master, bg="yellow",height=100)
        main_frame.grid(row=0, column=2,rowspan=2,columnspan=3, sticky=ALL)

root = Tk()
app = Application(master=root)                
app.mainloop()
