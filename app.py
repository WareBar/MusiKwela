from tkinter import *
import tkinter as tk
import customtkinter as MD
from player_utility import photoRender
from tinytag import TinyTag
import os
#for selecting path





class App(MD.CTk):
    def __init__(self, title, size) -> None:
        super().__init__()

        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.resizable(False, False)

        self.navigation = Navigation(self, 600, 200, "#8F8F8F")
        self.navigation.create_items()

        self.control = Control(self, 200, 1100, 'grey')
        self.control.create_buttons()

        self.main = Main(self, 600, 900, 'black')
        self.main.DisplaySong()


        self.mainloop()



class Navigation(MD.CTkFrame):
    def __init__(self, parent, length, span, color):
        super().__init__(parent)

        self.configure(height=length, width=span, fg_color=color, corner_radius=0)

    def create_items(self):

        logo_icon = photoRender('icons/Playerme.png',60,60)
        home_icon = photoRender("icons/home.png",30,30)
        genre_icon = photoRender('icons/genre.png',30,30)
        search_icon = photoRender('icons/Search.png',30,30)

        tag = MD.CTkLabel(self, text="MusicKwela", image=logo_icon, compound=tk.LEFT, font=(('Inter'),24))
        tag.place(x=0, y=10)

        home = MD.CTkButton(self, text="Home", image=home_icon, compound=tk.LEFT, font=(('Inter'),20), width=200, fg_color="#8F8F8F")
        home.place(x=0, y=100)

        genres = MD.CTkButton(self, text="Genres", image=genre_icon, compound=tk.LEFT, font=(('Inter'),20), width=200, fg_color="#8F8F8F")
        genres.place(x=0, y=150)

        search = MD.CTkButton(self, text="Search", image=search_icon, compound=tk.LEFT, font=(('Inter'),20), width=200, fg_color="#8F8F8F")
        search.place(x=0, y=200)



        library = MD.CTkLabel(self, text='LIBRARY', font=(('Inter'),22))
        library.place(x=15, y=250)


        browse = MD.CTkButton(self, text='Browse', font=(('Inter'),15), width=200, fg_color="#8F8F8F")
        browse.place(x=0, y=300)

        playlist = MD.CTkButton(self, text='Playlist', font=(('Inter'),15), width=200, fg_color="#8F8F8F")
        playlist.place(x=0, y=350)

        tracks = MD.CTkButton(self, text='Tracks', font=(('Inter'),15), width=200, fg_color="#8F8F8F")
        tracks.place(x=0, y=400)

        artists = MD.CTkButton(self, text='Artists', font=(('Inter'),15), width=200, fg_color="#8F8F8F")
        artists.place(x=0, y=450)

        albums = MD.CTkButton(self, text='Albums', font=(('Inter'),15), width=200, fg_color="#8F8F8F")
        albums.place(x=0, y=500)


        self.grid(row=0, column=0)

class Control(MD.CTkFrame):
    def __init__(self, parent, length, span, color):
        super().__init__(parent)
        self.configure(height=length, width=span, fg_color=color, corner_radius=0)


    def create_buttons(self):
        shuffle_icon = photoRender('icons/shuffle.png',35,35)
        back_icon = photoRender('icons/back.png',35,35)
        pause_icon = photoRender('icons/pause.png',35,35)
        next_icon = photoRender('icons/next.png',35,35)
        repeat_icon = photoRender('icons/repeat.png',35,35)
        global picture_logo
        picture_logo = photoRender('icons/picture.jpg',60,60)
        currsong = MD.CTkLabel(self, text='  Song', image=picture_logo, compound=tk.LEFT, font=(('Inter'),20))
        currsong.place(x=40, y=20)


        shuffle = MD.CTkButton(self,image=shuffle_icon, text=None, width=50, corner_radius=200)
        shuffle.place(x=550, y=35)


        back = MD.CTkButton(self,image=back_icon, text=None, width=50, corner_radius=200)
        back.place(x=650, y=35)

        pause = MD.CTkButton(self,image=pause_icon, text=None, width=50, corner_radius=200)
        pause.place(x=750, y=35)

        next = MD.CTkButton(self,image=next_icon, text=None, width=50, corner_radius=200)
        next.place(x=850, y=35)

        repeat = MD.CTkButton(self,image=repeat_icon, text=None, width=50, corner_radius=200)
        repeat.place(x=950, y=35)

        current_pos = MD.CTkLabel(self, text="0:00", font=(('Inter'),14))
        current_pos.place(x=570, y=6)

        progressbar = MD.CTkSlider(self, width=340)
        progressbar.place(x=613, y=15)

        length = MD.CTkLabel(self, text="2:40", font=(('Inter'),14))
        length.place(x=970, y=6)

        self.grid(row=1, column=0, columnspan=2)

class Main(MD.CTkFrame):
    def __init__(self, parent, length, span, color):
        super().__init__(parent)
        self.grid_propagate(False)
        self.configure(height=length, width=span, fg_color=color, corner_radius=0)

        self.grid(row=0, column=1)

    def DisplaySong(self):

        holder = MD.CTkScrollableFrame(self, height=550, width=870,fg_color='black',scrollbar_fg_color='white')
        holder.place(x=10, y=10)


        for box_column in range(2):
            for box_row in range(4):

                box = MD.CTkButton(holder, image=picture_logo, text=f'', compound=tk.LEFT,fg_color='green', width=350, height=45, anchor="w")
                box.grid(row=box_row, column=box_column,padx=10, pady=10)








App('MusiKwela',(1100,700))