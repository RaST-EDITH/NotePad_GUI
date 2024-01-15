# Library and Modules used 
import os                                                    # pip install os ( In case if not present )
import numpy as np                                           # pip install numpy ( In case if not present )
import pandas as pd                                          # pip install pandas==1.4.3
import openpyxl as oxl                                       # pip install openpyxl==3.0.10
from tkinter import *                                        # pip install tkinter==8.6
import customtkinter as ctk                                  # pip install customtkinter==4.6.3
from PIL import Image ,ImageTk                               # pip install pillow==9.3.0
from tkinter.messagebox import showerror, showinfo

class NotePad :

    def __init__(self) :
        ctk.set_appearance_mode( "dark" )
        ctk.set_default_color_theme( "dark-blue" )
        self.width = 1200
        self.height = 700
        self.root = ctk.CTk()
        self.root.title( "NotePad GUI" )
        self.root.geometry( "1200x700+200+80" )
        self.root.resizable( False, False )
    
    def change( self, can, page) :

        # Switching canvas
        can.destroy()
        page()
    
    def notesPage(self) :

        # Defining Structure
        notes_page = Canvas( self.root, 
                              width = self.width, height = self.height, 
                               bg = "black", highlightcolor = "#3c5390", 
                                borderwidth = 0 )
        notes_page.pack( fill = "both", expand = True )

        # Heading
        notes_page.create_text( 700, 120, text = "Notes", 
                                font = ( "Georgia", 45, "bold" ), fill = "#1c54df" )

        box1_back = ctk.CTkTextbox( notes_page, width = 231.5, height = 231.5 )
        box1_back.place( x = 100+50-80, y = 200-50, anchor = "nw")
        
        box1 = Text( notes_page, width = 26, height = 13 )
        box1.place( x = 100+50-50, y = 200, anchor = "nw")

        box2_back = ctk.CTkTextbox( notes_page, width = 231.5, height = 231.5 )
        box2_back.place( x = 300+130-80, y = 200-50, anchor = "nw")
        
        box2 = Text( notes_page, width = 26, height = 13 )
        box2.place( x = 300+200-50, y = 200, anchor = "nw")
        
        # Return Button
        ret_bt = ctk.CTkButton( master = notes_page, 
                                 text = "Back", text_font = ( "Georgia", 20 ), 
                                  width = 100, height = 50, corner_radius = 18,
                                   bg_color = "black", fg_color = "red", 
                                    hover_color = "#ff5359", border_width = 0, 
                                     command = lambda : self.change( notes_page, self.landingPage) )
        ret_bt_win = notes_page.create_window( 30, 20, anchor = "nw", window = ret_bt )

        self.root.mainloop()

    def firstPage(self) :

        # Defining Structure
        first_page = Canvas( self.root, 
                              width = self.width, height = self.height, 
                               bg = "black", highlightcolor = "#3c5390", 
                                borderwidth = 0 )
        first_page.pack( fill = "both", expand = True )

        # Heading
        first_page.create_text( 300, 170, text = "Note", 
                                font = ( "Georgia", 60, "bold" ), fill = "#a7a8ac" )
        first_page.create_text( 390, 280, text = "Pad", 
                                font = ( "Georgia", 60, "bold" ), fill = "#e3e3e3" )
        
        # Next Page Button
        next_bt = ctk.CTkButton( master = first_page,
                                  text = "Let's  Go  ->", text_font = ( "Georgia", 23 ),
                                   width = 120, height = 50, corner_radius = 14,
                                    bg_color = "#0d0d0d", fg_color = "red",
                                     hover_color = "#ff5359", border_width = 0,
                                      text_color = "white",
                                       command = lambda : self.change( first_page, self.notesPage ) )
        next_bt_win = first_page.create_window( 190, 640, anchor = "nw", window = next_bt )

        self.root.mainloop()

if __name__ == "__main__" :

    notepad_class = NotePad()
    notepad_class.firstPage()
