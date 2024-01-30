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
        self.root.iconbitmap( os.path.join( os.getcwd(), r"Design\notepad.ico" ))
        self.root.title( "NotePad GUI" )
        self.root.geometry( "1200x700+200+80" )
        self.root.resizable( False, False )
    
    def Imgo( self, file, w, h) :

        # Image processing
        img = Image.open( file )
        pht = ImageTk.PhotoImage( img.resize( (w,h), Image.Resampling.LANCZOS))
        return pht

    def change( self, can, page) :

        # Switching canvas
        can.destroy()
        page()

    def saveNotes( self, boxes, sheet_pd, path ) :

        # saving notes
        wb = oxl.load_workbook( path )
        sheet_xl = wb['Sheet1']

        for i in range( len(boxes) ) :
            data = boxes[i].get("0.0", END )
            sheet_xl[f"B{i+2}"].value = data

        try :
            wb.save( path )
            showinfo( title = "Done", message = "Changes Saved" )
        
        except :
            showerror( title = "Open File", message = "Close File in Background")

    def notesPage(self) :

        back_color = "#f6f6f8"
        frame_color = "#2b346d"
        inner_color = "#b0bee5"
        font = ( "Book Antiqua", 15, "bold")

        # Defining Structure
        notes_page = Canvas( self.root, 
                              width = self.width, height = self.height, 
                               bg = back_color, highlightcolor = "#3c5390", 
                                borderwidth = 0 )
        notes_page.pack( fill = "both", expand = True )

        path = os.path.join( os.getcwd(), r"Data_File\note_file.xlsx")
        notes_sheet = pd.read_excel( path )
        column = notes_sheet.columns
        row, col = notes_sheet.shape

         # Background Image
        back_image = self.Imgo( os.path.join( os.getcwd(), r"Design\secondPage.png" ), 80, 80)
        notes_page.create_image( 1350, 20, image = back_image , anchor = "nw")

        # Heading
        notes_page.create_text( 760, 120, text = "Notes", 
                                font = ( "Georgia", 45, "bold" ), fill = "#5871b4" )

        box1_back = ctk.CTkTextbox( notes_page, width = 231.5, height = 231.5, 
                                     bg_color = back_color, fg_color = frame_color )
        box1_back.place( x = 70, y = 150, anchor = "nw")
        
        box1 = Text( notes_page, width = 20, height = 9, font = font,
                        background = inner_color, foreground = "white" )
        box1.place( x = 100, y = 200, anchor = "nw")

        box2_back = ctk.CTkTextbox( notes_page, width = 231.5, height = 231.5, 
                                     bg_color = back_color, fg_color = frame_color )
        box2_back.place( x = 350, y = 150, anchor = "nw")
        
        box2 = Text( notes_page, width = 20, height = 9, font = font,
                        background = "white", foreground = "black"  )
        box2.place( x = 450, y = 200, anchor = "nw")

        box3_back = ctk.CTkTextbox( notes_page, width = 231.5, height = 231.5, 
                                     bg_color = back_color, fg_color = frame_color )
        box3_back.place( x = 630, y = 150, anchor = "nw")
        
        box3 = Text( notes_page, width = 20, height = 9, font = font,
                        background = inner_color, foreground = "white" )
        box3.place( x = 800, y = 200, anchor = "nw")

        box4_back = ctk.CTkTextbox( notes_page, width = 231.5, height = 231.5, 
                                     bg_color = back_color, fg_color = frame_color )
        box4_back.place( x = 910, y = 150, anchor = "nw")

        box4 = Text( notes_page, width = 20, height = 9, font = font,
                        background = "white", foreground = "black"  )
        box4.place( x = 1150, y = 200, anchor = "nw")

        box5_back = ctk.CTkTextbox( notes_page, width = 231.5, height = 231.5 )
        box5_back.place( x = 100+50-80, y = 400+100-86, anchor = "nw")

        box5 = Text( notes_page, width = 26, height = 13 )
        box5.place( x = 100+50-50, y = 400+150-20, anchor = "nw")

        box6_back = ctk.CTkTextbox( notes_page, width = 231.5, height = 231.5 )
        box6_back.place( x = 300+130-80, y = 400+100-86, anchor = "nw")

        box6 = Text( notes_page, width = 26, height = 13 )
        box6.place( x = 300+200-50, y = 400+150-20, anchor = "nw")

        box7_back = ctk.CTkTextbox( notes_page, width = 231.5, height = 231.5 )
        box7_back.place( x = 500+150-20, y = 400+100-86, anchor = "nw")

        box7 = Text( notes_page, width = 26, height = 13 )
        box7.place( x = 500+350-50, y = 400+150-20, anchor = "nw")

        box8_back = ctk.CTkTextbox( notes_page, width = 231.5, height = 231.5 )
        box8_back.place( x = 700+200+10, y = 400+100-86, anchor = "nw")

        box8 = Text( notes_page, width = 26, height = 13 )
        box8.place( x = 700+500-50, y = 400+150-20, anchor = "nw")
        
        boxes = [ box1, box2, box3, box4, box5, box6, box7, box8]

        for i in range( row ) :
            boxes[i].insert( "0.0", notes_sheet[column[1]][i] )

        # Save Button
        save_bt = ctk.CTkButton( master = notes_page, 
                                  text = "Save", text_font = ( "Georgia", 20 ), 
                                   width = 100, height = 30, corner_radius = 18,
                                    bg_color = "black", fg_color = "green", 
                                     hover_color = "#ff5359", border_width = 0, 
                                      command = lambda : self.saveNotes( boxes, notes_sheet, path ) )
        save_bt_win = notes_page.create_window( 730, 820, anchor = "nw", window = save_bt )

        # Return Button
        ret_bt = ctk.CTkButton( master = notes_page, 
                                 text = "Back", text_font = ( "Georgia", 20 ), 
                                  width = 100, height = 50, corner_radius = 18,
                                   bg_color = "black", fg_color = "red", 
                                    hover_color = "#ff5359", border_width = 0, 
                                     command = lambda : self.change( notes_page, self.firstPage) )
        ret_bt_win = notes_page.create_window( 30, 20, anchor = "nw", window = ret_bt )

        self.root.mainloop()

    def firstPage(self) :

        # Defining Structure
        first_page = Canvas( self.root, 
                              width = self.width, height = self.height, 
                               bg = "black", highlightcolor = "#3c5390", 
                                borderwidth = 0 )
        first_page.pack( fill = "both", expand = True )

        # Background Image
        back_image = self.Imgo( os.path.join( os.getcwd(), r"Design\firstPage.jpg" ), 1498, 875)
        first_page.create_image( 0, 0, image = back_image , anchor = "nw")

        # Heading
        first_page.create_text( 1140, 290, text = "Note", 
                                font = ( "Georgia", 60, "bold" ), fill = "#5871b4" )
        first_page.create_text( 1260, 400, text = "Pad", 
                                font = ( "Georgia", 60, "bold" ), fill = "#232e66" )
        
        # Next Page Button
        next_bt = ctk.CTkButton( master = first_page,
                                  text = "Let's  Note ➡", text_font = ( "Georgia", 20 ),
                                   width = 80, height = 40, corner_radius = 14,
                                    bg_color = "#f7f7f9", fg_color = "red",
                                     hover_color = "#ff5359", border_width = 0,
                                      text_color = "white",
                                       command = lambda : self.change( first_page, self.notesPage ) )
        next_bt_win = first_page.create_window( 1070, 600, anchor = "nw", window = next_bt )

        self.root.mainloop()

if __name__ == "__main__" :

    notepad_class = NotePad()
    notepad_class.firstPage()
