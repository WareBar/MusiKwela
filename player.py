from tkinter import *
import tkinter as tk
import customtkinter as MD
import pyglet, os


# pyglet.font.add_file('Amerika.ttf')
# pyglet.font.add_file('Inika-Bold.ttf')
# pyglet.font.add_file('Inika-Regular.ttf')



app = Tk()
app.title("MusiKwela")
app.geometry("1100x700")
app.resizable(False,False)


right = MD.CTkFrame(app, height=600, width=200, corner_radius=0)
right.grid(row=0, column=0)


left = MD.CTkFrame(app, height=600, width=900, fg_color="black", corner_radius=0)
left.grid(row=0, column=1)

bottom = MD.CTkFrame(app, height=200, width=1100, fg_color="grey", corner_radius=0)
bottom.grid(row=1, column=0, columnspan=2)


app.mainloop()