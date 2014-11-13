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
        
        top_frame = Frame(master, bg="red")
        top_frame.grid(row=0, column=0, sticky=ALL)
        l = Label(top_frame, text="Frame {0}".format(1),bg="red")
        l.grid(row=0, column=0, sticky=ALL)
   
        bottom_frame = Frame(master, bg="green")
        bottom_frame.grid(row=1, column=0, sticky=ALL)
        l = Label(bottom_frame, text="Frame {0}".format(2),bg="green")
        l.grid(row=1, column=0, sticky=ALL)
        
        main_frame = Frame(master, bg="yellow")
        main_frame.grid(row=0, column=1,rowspan=2,columnspan=4, sticky=ALL)
        l = Label(main_frame, text="Frame {0}".format(3),bg="yellow")
        l.grid(row=0, column=1, rowspan=2,columnspan=4, sticky=ALL)

root = Tk()
app = Application(master=root)                
app.mainloop()
