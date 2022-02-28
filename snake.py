import tkinter as tk

import grid as g

class GUI:
    def __init__(self, main_frame):
        self.main_frame = main_frame

        self.grid = g.Grid(width=20, height=10)

root = tk.Tk()
root.title("snake")

gui = GUI(root)

root.mainloop()
