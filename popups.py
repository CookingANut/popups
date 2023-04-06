import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import sys


class popup():
    def __init__(self,title, image):
        self.title = title
        self.image = image
        self.window = tk.Tk()
        self.window_setup()
        self.widget_setup()
        self.widget_deploy()
        self.window.mainloop()
    
    def widget_setup(self):
        print(self.image)
        popimage = Image.open(self.image)
        popimage.thumbnail((600,600), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(popimage)
        self.panel = tk.Label(self.window, image=img)
        self.button = tk.Button(text=f"{self.title} and Press This Button(or Press Enter)",width=110, command=self.click_button)
    
    def window_setup(self):
        self.window.title(self.title)
        self.window.geometry("600x400")
        self.window.bind('<Return>',self.click_button)
        self.window.protocol("WM_DELETE_WINDOW", func=self.click_exit)
        self.window.eval('tk::PlaceWindow . center')
        self.window.resizable(0,0)
    
    def widget_deploy(self):
        self.panel.grid(row=0,column=0)
        self.button.grid(row=1,column=0)

    def click_exit(self):
        messagebox.askokcancel("", "Please press the button!")

    def click_button(self, event=None):
        print("PASS!")
        self.window.destroy()

if __name__ == "__main__":
    try:
        title = sys.argv[1]
        image = sys.argv[2]
    except IndexError:
        title = "TEST"
        image = "./power_button.jpg"
    
    popup(title, image)