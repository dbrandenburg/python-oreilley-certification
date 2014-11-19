#!/usr/bin/env python3

from tkinter import *

ALL = N+S+W+E
OPEN_BUTTON_LABEL = "Open"
BUTTON_LABEL = ["Red","Blue","Green","Black"]
OPEN_BUTTON_LABEL = "Open"

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(sticky=ALL)
        self.master.title("Framer")
        
        for r in range(2):
             self.master.rowconfigure(r, weight=1)

        self.master.columnconfigure(0, weight=1)
        Button(master, text="{0}".format("Red")).grid(row=2,column=0,sticky=E+W)        
        self.master.columnconfigure(1, weight=1)
        Button(master, text="{0}".format("Blue")).grid(row=2,column=1,sticky=E+W)        
        self.master.columnconfigure(2, weight=1)
        Button(master, text="{0}".format("Green")).grid(row=2,column=2,sticky=E+W)        
        self.master.columnconfigure(3, weight=1)
        Button(master, text="{0}".format("Black")).grid(row=2,column=3,sticky=E+W)        
        self.master.columnconfigure(4, weight=1)
        Button(master, text="{0}".format("Open")).grid(row=2,column=4,sticky=E+W)        
        
        top_frame = Frame(master, bg="red", height=100)
        top_frame.grid(row=0, column=0,columnspan=2,sticky=ALL)
        top_frame.bind("<Button-1>", lambda event: self.handler(event,"top_frame"))
        
        bottom_frame = Frame(master, bg="green",height=100)
        bottom_frame.grid(row=1, column=0,columnspan=2,sticky=ALL)
        bottom_frame.bind("<Button-1>", lambda event: self.handler(event,"bottom_frame"))
        
        main_frame = Frame(master, height=100)
        main_frame.grid(row=0, column=2,rowspan=2,sticky=ALL)
        
        main_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
           
        self.entry = Entry(main_frame)
        self.entry.grid(row=0, column=0,columnspan=3,sticky=W+E)
        
        #self.text = Text(main_frame)
        #self.text.grid(row=1, column=0,columnspan=3,sticky=ALL)

    def handler(self, event, framename):
        print("clicked at", event.x, event.y, "in", framename)
        filename = self.entry.get()
        print(filename)
        self.get_file_content('README')
        
    def settext(self,text_from_file):
        self.text.insert(CURRENT, text_from_file)
        
    def get_file_content(self,filename):
        print(filename)
        #f = open(filename, 'w')
        #print(f)

        

root = Tk()
app = Application(master=root)                
app.mainloop()
