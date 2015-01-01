#Simple GUI

from tkinter import *

#Create the window
root = Tk()

#Modify root window
root.title("Simple GUI")
root.geometry("800x400")

app = Frame(root)
app.grid()
label = Label(app,text = "This is a label")
button1 = Button(app,text = "This is a button" )
button2 = Button(app,text = "This is a button" )
button3 = Button(app)
button3["text"] = "Button 3"


button1.grid()
button2.grid()
button3.grid()

label.grid()


#Kick off the event loop
root.mainloop()


