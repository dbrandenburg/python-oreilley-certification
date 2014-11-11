#!/usr/bin/env python3

from tkinter import *

ALL = N+S+W+E

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        #self.master.rowconfigure(0, weight=1)
        #self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        self.master.title("Framer")
        
        for r in range(6):
             self.master.rowconfigure(r, weight=1)    
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            Button(master, text="Button {0}".format(c)).grid(row=6,column=c,sticky=E+W)
            
#        Frame1 = Frame(master, bg="red")
#        Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = ALL)
#        Frame2 = Frame(master, bg="green")
#        Frame2.grid(row = 3, column = 0, rowspan = 3, columnspan = 2, sticky = ALL)
#        Frame3 = Frame(master, bg="blue")
#        Frame3.grid(row = 0, column = 2, rowspan = 6, columnspan = 3, sticky = ALL)
        
        
        top_frame = Frame(master, bg="red")
        top_frame.grid(row=0, column=0, rowspan=3, columnspan=2, sticky=ALL)
        #top_frame.rowconfigure(0, weight=1)
        l = Label(top_frame, text="Frame {0}".format(1),bg="red")
        l.grid(row=0, column=0, rowspan=3, columnspan=2, sticky=ALL)
#        
#        bottom_frame = Frame(self)
#        bottom_frame.grid(sticky=ALL)
#        bottom_frame.rowconfigure(1, weight=1)
#        Label(bottom_frame, text="Frame {0}".format(2),bg="green").grid(row=1, column=0, sticky=ALL, columnspan=2)
#        
#        main_frame = Frame(self)
#        main_frame.grid(sticky=ALL)
#        main_frame.rowconfigure(5, weight=2)
#        Label(main_frame, text="Frame {0}".format(3),bg="yellow").grid(row=0, column=2, sticky=ALL, rowspan=2, columnspan=3)
        
#        self.rowconfigure(5, weight=1)
        
#        for c in range(5):
#            self.columnconfigure(c, weight=1)
#            Button(self, text="Col {0}".format(c)).grid(row=2, column=c, sticky=ALL)

root = Tk()
app = Application(master=root)                
app.mainloop()
