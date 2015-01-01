#How to use a class with Tkinter

from tkinter import *

class Application(Frame):
    """A GUI application with three buttons."""

    def __init__(self,master):
        """Initialize the Frame"""
        Frame.__init__(self,master)
        self.grid()
        self.button_clicks = 0 #count the number of button clicks
        self.create_widgets()

    def create_widgets(self):
        """Create button which displays number of clicks """
        """Create 3 buttons that do nothing. """

        self.button = Button(self)
        self.button["text"] = "Total Clicks : 0"
        self.button["command"] = self.update_count
        self.button.grid()

    def update_count(self):
        """Increase the click count and display the new total"""
        self.button_clicks += 1
        self.button["text"] = "Total Clicks :" + str(self.button_clicks)
       

root = Tk()
root.title("Insert title")
root.geometry("200x100")

app = Application(root)

root.mainloop()
