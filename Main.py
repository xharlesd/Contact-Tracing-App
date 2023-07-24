"""
- Create a program that ask user for typical information found in covid contact tracing app
- Write the collected information in a file (use any format you like)
- The app should be able to add and search entry
- Be creative, the realistic the better.
- Please don't submit downloaded program
- Please dont follow any online contact tracing programming tutorial
"""

# import necessary modules to be used
from tkinter import *
from tkinter import ttk
import tkinter as tk
# import classes (soon)

# App Class
class ContactTracing():
    
    # constructor
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Contact Tracing App")  # program title
        self.window.geometry('1000x700')  # tkinter frame window
    
        red_frame = tk.Frame(bd=0, highlightthickness=0, background="#800000")
        blue_frame = tk.Frame(bd=0, highlightthickness=0, background="white")
        red_frame.place(x=0, y=0, relwidth=0.4, relheight=1, anchor="nw")
        blue_frame.place(relx=0.35, y=0, relwidth=0.7, relheight=1, anchor="nw")

        app_title = tk.Label(self.window, text = "PUP", fg = "#0818A8", bg = "white", font=("Arial",55,"bold"))
        app_title.place(x = 430, y = 80, width = 250, height = 90)

        app_title = tk.Label(self.window, text = "TRACE", fg = "red", bg = "white", font=("Arial",55,"bold"))
        app_title.place(x = 630, y = 80, width = 250, height = 90)

        app_title = tk.Label(self.window, text = "PUP CONTACT TRACING APP", fg = "gray", bg = "white", font=("Arial",20,"bold"))
        app_title.place(x = 455, y = 155, width = 450, height = 20)

        # button for add entry
        add_info_Button = tk.Button(self.window, text = "Add Info", fg = "white", bg = "#40B5AD", font=("Century Gothic",24,"bold"))
        add_info_Button.place(x = 550, y = 310, width = 250, height = 90)
        
        # button for search entry
        search_info_Button = tk.Button(self.window, text = "Search Data", fg = "white", bg = "#40B5AD", font=("Century Gothic",24,"bold"), )
        search_info_Button.place(x = 550, y = 420, width = 250, height = 90)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    App = ContactTracing()
    App.run()