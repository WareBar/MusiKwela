from tkinter import *
import tkinter as tk
import customtkinter as MD
import pyglet, os
from photo_rendering import photoRender


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



#render all necessary images

logo_icon = photoRender('icons/Playerme.png',60,60)
home_icon = photoRender("icons/home.png",30,30)
genre_icon = photoRender('icons/genre.png',20,20)
search_icon = photoRender('icons/Search.png',20,20)

shuffle_icon = photoRender('icons/shuffle.png',20,20)
back_icon = photoRender('icons/back.png',20,20)
pause_icon = photoRender('icons/pause.png',20,20)
next_icon = photoRender('icons/next.png',20,20)
repeat_icon = photoRender('icons/repeat.png',20,20)



#putting all the landing widget into place


tag_pic = MD.CTkLabel(right, text="", image=logo_icon)
tag_pic.place(x=10, y=10)

tag = MD.CTkLabel(right, text='MusiKwela', font=(('Inter'),24))
tag.place(x=70, y=25)


home_pic = MD.CTkLabel(right, text="Home", image=home_icon)
home_pic.place(x=40, y=100)

# home = MD.CTkLabel(right, text="HOME", font=(('Inter'),20))
# home.grid(row=1, column=1)




app.mainloop()