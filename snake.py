import tkinter as tk
from PIL import Image, ImageTk

import grid as g

class GUI:
    def __init__(self, main_frame):
        self.main_frame = main_frame

        self.grid = g.Grid(width=20, height=10)

        self.img_label = tk.Label(self.main_frame)
        self.img_label.grid(row=0, column=0)

        self.image = None

        self.image = ImageTk.PhotoImage(self.grid.draw(10, 10, 1))
        self.img_label.config(image=self.image)
    def 

root = tk.Tk()
root.title("snake")

gui = GUI(root)

root.mainloop()
