import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import sys

def click_exit(event=None):
    messagebox.askokcancel("", "Please press the button!")

def click_button(event=None):
    print("PASS!")
    # window.destroy()
    sys.exit(0)


class popup():
    def __init__(self,title, image):
        window = tk.Tk()
        window.title(title)
        window.geometry("800x500")
        window.bind('<Return>',click_button)
        popimage = Image.open(image)
        popimage.thumbnail((800,800), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(popimage)
        panel = tk.Label(window, image=img)
        button = tk.Button(text=f"{title} and Press This Button(or Press Enter)",width=110, command=click_button)
        panel.grid(row=0,column=0)
        button.grid(row=1,column=0)
        window.protocol("WM_DELETE_WINDOW", func=click_exit)
        window.eval('tk::PlaceWindow . center')
        window.resizable(0,0)
        window.mainloop()

if __name__ == "__main__":
    try:
        title = sys.argv[1]
        image = sys.argv[2]
    except IndexError:
        title = "TEST"
        image = "./power_button.jpg"
    
    popup(title, image)