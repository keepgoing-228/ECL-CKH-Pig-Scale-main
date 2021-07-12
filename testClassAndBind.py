# import tkinter #need tkinter.Tk()
from tkinter import * 
from tkinter.ttk import *

class App(Tk):
    def __init__(self):
        super().__init__()
        # Entry widget 
        e1 = Entry(self) 
        e1.pack(expand = 1, fill = BOTH) 
  
        # Button Widget 
        e2 = Button(self, text ="Button") 
        e2.pack(pady = 5) 
        
        # Radiobutton widget 
        e3 = Radiobutton(self, text ="Hello") 
        e3.pack(pady = 5) 
        self.bind("<Button-1>", lambda e: self.on_click(e))

    def on_click(self, event):
        widget = self.focus_get() 
        print(widget, "has focus") 
        # self.entry.delete(5, 'end')



win = App()
win.mainloop()


'''

from tkinter import * 
from tkinter.ttk import *
  
# creating master window 
master = Tk() 
  
# This method is used to get 
# the name of the widget 
# which currently has the focus 
# by clicking Mouse Button-1 
def focus(event):
    widget = master.focus_get() 
    print(widget, "has focus") 
  
# Entry widget 
e1 = Entry(master) 
e1.pack(expand = 1, fill = BOTH) 
  
# Button Widget 
e2 = Button(master, text ="Button") 
e2.pack(pady = 5) 
  
# Radiobutton widget 
e3 = Radiobutton(master, text ="Hello") 
e3.pack(pady = 5) 
  
# Here function focus() is binded with Mouse Button-1 
# so every time you click mouse, it will call the 
# focus method, defined above 
master.bind_all("<Button-1>", lambda e:focus(e)) 
  
# infinite loop 
mainloop()
'''



'''
from tkinter import * 

class GUI: 
    def __init__(self,root): 
     Window = Frame(root) 
     self.DrawArea = Canvas(Window) 
     self.DrawArea.pack() 
     Window.pack() 

     self.DrawArea.bind("<Button 1>",self.starttracking) 

    def updatetracking(self,event): 
     print (event.x,event.y )

    def finishtracking(self,event): 
     self.DrawArea.bind("<Button 1>",self.starttracking) 
     self.DrawArea.unbind("<Motion>") 

    def starttracking(self,event): 
     print (event.x,event.y) 
     self.DrawArea.bind("<Motion>",self.updatetracking) 
     self.DrawArea.bind("<Button 1>",self.finishtracking) 



if __name__ == '__main__': 
    root = Tk() 
    App = GUI(root) 
    root.mainloop() 
'''