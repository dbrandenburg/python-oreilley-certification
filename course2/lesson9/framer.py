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
        
        main_frame = Frame(master)
        main_frame.grid(row=0,column=2,rowspan=2,columnspan=3, sticky=ALL)
           
        self.entry = Entry(main_frame)
        self.entry.bind("<Return>", lambda e: self.get_file_content())
        self.entry.pack(side=TOP, fill=BOTH)
        
        self.text = Text(main_frame, width=0, height=0)
        self.text.pack(side=TOP, fill=BOTH, expand=True)

    def handler(self, event, framename):
        print("clicked at", event.x, event.y, "in", framename)
        filename = self.entry.get()
        
    def settext(self,text_from_file):
        self.text.insert(CURRENT, text_from_file)
        
    def get_file_content(self):
        output_text=self.entry.get()
        print(output_text)
        #f = open(filename, 'w')
        #print(f)

        

root = Tk()
app = Application(master=root)                
app.mainloop()
