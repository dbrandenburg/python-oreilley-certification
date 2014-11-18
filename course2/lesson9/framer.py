#!/usr/bin/env python3

from tkinter import *

ALL = N+S+W+E
BUTTON_LABEL = ["Red","Blue","Green","Black","Open"]

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(sticky=ALL)
        self.master.title("Framer")
        
        for r in range(2):
             self.master.rowconfigure(r, weight=1)    
        for c, b in zip(range(5),BUTTON_LABEL):
            self.master.columnconfigure(c, weight=1)
            Button(master, text="{0}".format(b)).grid(row=2,column=c,sticky=E+W)        
        
        top_frame = Frame(master, bg="red", height=100)
        top_frame.grid(row=0, column=0,columnspan=2,sticky=ALL)
        top_frame.bind("<Button-1>", lambda event: self.handler(event,"top_frame"))
        
        bottom_frame = Frame(master, bg="green",height=100)
        bottom_frame.grid(row=1, column=0,columnspan=2,sticky=ALL)
        bottom_frame.bind("<Button-1>", lambda event: self.handler(event,"bottom_frame"))

        main_frame = Frame(master, bg="yellow",height=100)
        main_frame.grid(row=0, column=2,rowspan=2,columnspan=3,sticky=ALL)
        
        main_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        main_frame.columnconfigure(0, weight=1)
        entry = Entry(main_frame)
        entry.grid(row=0, column=0,sticky=W+N+E)
        
    def handler(self, event, framename):
        print("clicked at", event.x, event.y, "in", framename)
        

root = Tk()
app = Application(master=root)                
app.mainloop()
