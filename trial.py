import tkinter as tk
import pyglet, os

pyglet.font.add_file('ARCADE_N.ttf')  # Your TTF file name here
pyglet.font.add_file('ARCADE_I.ttf')


root = tk.Tk()
MyLabel = tk.Label(root,text="test",font=('Arcade Interlaced',25)) 

MyLabel.pack()
root.mainloop()