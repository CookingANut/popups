import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import argparse


class PopupFrame(ttk.Frame):
    def __init__(self, root, title, image, image_W, button_W):
        super().__init__(root)
        self.root = root
        self.title = title
        self.image = image
        self.image_W = image_W
        self.button_W = button_W
        self.widget_setup()
        self.widget_deploy()

    def widget_setup(self):
        self.image = Image.open(self.image)
        basewidth = self.image_W
        wpercent = (basewidth/float(self.image.size[0]))
        hsize = int((float(self.image.size[1]) * float(wpercent)))
        self.image = self.image.resize((basewidth,hsize), Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(self.image)
        self.panel = ttk.Label(self, image=self.image) 
        self.button = ttk.Button(self, text=f"{self.title} and Press This Button(or Press Enter)", width=self.button_W, command=self.click_button)
    
    def widget_deploy(self):
        self.panel.grid(row=0,column=0)
        self.button.grid(row=1,column=0)

    def click_exit(self):
        messagebox.askokcancel("", "Please press the button!")

    def click_button(self, event=None):
        print("PASS!")
        self.root.destroy()


class PopupRoot():
    def __init__(self, title, image, root_WH, image_W, button_W):
        root = tk.Tk()
        frame = PopupFrame(root, title, image, image_W, button_W)
        frame.grid()
        root.title(title)
        root.geometry(root_WH)
        root.bind('<Return>',frame.click_button)
        root.protocol("WM_DELETE_WINDOW", func=frame.click_exit)
        root.eval('tk::PlaceWindow . center')
        root.resizable(0,0)
        root.mainloop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Popups Module")
    parser.add_argument('-t',   '--text',     type=str,   default="TEST",       help="modify the popup window's title")
    parser.add_argument('-i',   '--image',    type=str,   default="./test.jpg", help="the image show in popup window")
    parser.add_argument('-rwh', '--root_WH',  type=str,   default="500x260",    help='set the width and height of the popup window, default->"500x260"')
    parser.add_argument('-iw',  '--image_W',  type=int,   default=500,          help="set the width of the image, height would be automatically set to protect aspect, default->500")
    parser.add_argument('-bw',  '--button_W', type=int,   default=59,           help="set the width of the button, default->59")
    args = parser.parse_args()
    PopupRoot(args.text, args.image, args.root_WH, args.image_W, args.button_W)