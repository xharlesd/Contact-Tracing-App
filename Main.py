"""
- Create a program that ask user for typical information found in covid contact tracing app
- Write the collected information in a file (use any format you like)
- The app should be able to add and search entry
- Be creative, the realistic the better.
- Please don't submit downloaded program
- Please dont follow any online contact tracing programming tutorial
"""

# import necessary modules to be used
from typing import Optional, Tuple, Union
import customtkinter as ctk
import tkinter as tk
# import classes (soon)


# App background appearance
ctk.set_appearance_mode("Light")

# App color theme
ctk.set_default_color_theme("dark-blue") 

# App Class
class ContactTracing(ctk.CTk):
    """"""
    # constructor
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.title("Contact Tracing App")  # program title
        self.geometry('900x600')  # tkinter frame window
    
    # create label for add entry 
    # button for add entry

    # create label for search entry
    # button for search entry

if __name__ == "__main__":
    ContactTracing = ContactTracing()
    ContactTracing.mainloop()