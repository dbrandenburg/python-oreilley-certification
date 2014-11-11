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
        #self.bind("<Button-1>", self.handler)
        Label(self, text="Frame {0}".format(1),bg="red").grid(row=0, column=0, sticky=ALL, columnspan=2)
        
        self.rowconfigure(1, weight=1)
        #self.bind("<Button-1>", self.handler)
        Label(self, text="Frame {0}".format(2),bg="green").grid(row=1, column=0, sticky=ALL, columnspan=2)
        
        #self.bind("<Button-1>", self.ignores)
        self.rowconfigure(5, weight=2)
        Label(self, text="Frame {0}".format(3),bg="yellow").grid(row=0, column=2, sticky=ALL, rowspan=2, columnspan=3)
        
        self.rowconfigure(5, weight=1)
        for c in range(5):
            self.columnconfigure(c, weight=1)
            Button(self, text="Col {0}".format(c)).grid(row=2, column=c, sticky=ALL)
            
    def handler(self, event):
        print("clicked at", event.x, event.y)
    
    def ignores(self,event):
        pass

root = Tk()
app = Application(master=root)   
app.pack()             
app.mainloop()



#root = Tk()
#def handler(event):
#print("clicked at", event.x, event.y)
#frame = Frame(root, width=100, height=100) frame.bind("<Button-1>", handler) frame.pack()