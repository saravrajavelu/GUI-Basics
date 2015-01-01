#How to use a class with Tkinter

from tkinter import *

class Application(Frame):
    """A GUI application with three buttons."""

    def __init__(self,master):
        """Initialize the Frame"""
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create button, text and entry widget"""

        self.instruction = Label(self, text = "Entere the password")
        self.instruction.grid( row = 0, column = 0, columnspan = 2, sticky = W)

        self.password = Entry(self)
        self.password.grid(row = 1, column = 1, sticky = W)

        self.submit_button = Button(self, text = "Submit", command = self.reveal)
        self.submit_button.grid(row = 2, column = 0, sticky = W)

        self.text = Text(self, width = 35, height = 5, wrap = WORD)
        self.text.grid(row =3, column = 0, columnspan = 2, sticky =W)
        
    def reveal(self):
        """Display message based on the password typed in"""
        content = self.password.get()

        if content == "password":
            message = "You have entered the correct password"
        else:
            message = "Error!"
        self.text.delete(0.0,END)
        self.text.insert(0.0,message)
       

root = Tk()
root.title("Insert title")
root.geometry("200x100")

app = Application(root)

root.mainloop()
