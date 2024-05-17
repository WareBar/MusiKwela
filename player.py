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


left = MD.CTkFrame(app, height=600, width=200, corner_radius=0, fg_color="#8F8F8F")
left.grid(row=0, column=0)


right = MD.CTkFrame(app, height=600, width=900, fg_color="black", corner_radius=0)
right.grid(row=0, column=1)

bottom = MD.CTkFrame(app, height=200, width=1100, fg_color="grey", corner_radius=0)
bottom.grid(row=1, column=0, columnspan=2)



#render all necessary images

logo_icon = photoRender('icons/Playerme.png',60,60)
home_icon = photoRender("icons/home.png",30,30)
genre_icon = photoRender('icons/genre.png',30,30)
search_icon = photoRender('icons/Search.png',30,30)

shuffle_icon = photoRender('icons/shuffle.png',35,35)
back_icon = photoRender('icons/back.png',35,35)
pause_icon = photoRender('icons/pause.png',35,35)
next_icon = photoRender('icons/next.png',35,35)
repeat_icon = photoRender('icons/repeat.png',35,35)
picture_logo = photoRender('icons/picture.jpg',60,60)



#putting all the landing widget into place


tag = MD.CTkLabel(left, text="MusicKwela", image=logo_icon, compound=tk.LEFT, font=(('Inter'),24))
tag.place(x=0, y=10)

home = MD.CTkButton(left, text="Home", image=home_icon, compound=tk.LEFT, font=(('Inter'),20), width=200, fg_color="#8F8F8F")
home.place(x=0, y=100)

genres = MD.CTkButton(left, text="Genres", image=genre_icon, compound=tk.LEFT, font=(('Inter'),20), width=200, fg_color="#8F8F8F")
genres.place(x=0, y=150)

search = MD.CTkButton(left, text="Search", image=search_icon, compound=tk.LEFT, font=(('Inter'),20), width=200, fg_color="#8F8F8F")
search.place(x=0, y=200)



library = MD.CTkLabel(left, text='LIBRARY', font=(('Inter'),22))
library.place(x=15, y=250)


browse = MD.CTkButton(left, text='Browse', font=(('Inter'),15), width=200, fg_color="#8F8F8F")
browse.place(x=0, y=300)

playlist = MD.CTkButton(left, text='Playlist', font=(('Inter'),15), width=200, fg_color="#8F8F8F")
playlist.place(x=0, y=350)

tracks = MD.CTkButton(left, text='Tracks', font=(('Inter'),15), width=200, fg_color="#8F8F8F")
tracks.place(x=0, y=400)

artists = MD.CTkButton(left, text='Artists', font=(('Inter'),15), width=200, fg_color="#8F8F8F")
artists.place(x=0, y=450)

albums = MD.CTkButton(left, text='Albums', font=(('Inter'),15), width=200, fg_color="#8F8F8F")
albums.place(x=0, y=500)


# album_pic = MD.CTkFrame(bottom, width=70, height=70, corner_radius=10,bg_color='white')
# album_pic.place(x=10, y=10)

currsong = MD.CTkLabel(bottom, text='  Song', image=picture_logo, compound=tk.LEFT, font=(('Inter'),20))
currsong.place(x=40, y=20)


shuffle = MD.CTkButton(bottom,image=shuffle_icon, text=None, width=50, corner_radius=200)
shuffle.place(x=550, y=35)


back = MD.CTkButton(bottom,image=back_icon, text=None, width=50, corner_radius=200)
back.place(x=650, y=35)

pause = MD.CTkButton(bottom,image=pause_icon, text=None, width=50, corner_radius=200)
pause.place(x=750, y=35)

next = MD.CTkButton(bottom,image=next_icon, text=None, width=50, corner_radius=200)
next.place(x=850, y=35)

repeat = MD.CTkButton(bottom,image=repeat_icon, text=None, width=50, corner_radius=200)
repeat.place(x=950, y=35)

current_pos = MD.CTkLabel(bottom, text="0:00", font=(('Inter'),14))
current_pos.place(x=570, y=6)

progressbar = MD.CTkSlider(bottom, width=340)
progressbar.place(x=613, y=15)

length = MD.CTkLabel(bottom, text="2:40", font=(('Inter'),14))
length.place(x=970, y=6)


app.mainloop()