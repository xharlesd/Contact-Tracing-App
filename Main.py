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
import tkinter as tk
from PIL import ImageTk, Image

# App Class
class ContactTracing():

    # constructor
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Contact Tracing App")  # program title
        self.window.geometry('1190x820')  # tkinter frame window
       
        # insert background image
        original_image = Image.open("Puppic.png")
        resized_image = original_image.resize((420, 950))  
        background_image = ImageTk.PhotoImage(resized_image)
        self.canvas = tk.Canvas(self.window, width=400, height=900)
        self.canvas.pack(side=LEFT)
        self.canvas.create_image(0, 0, image=background_image, anchor="nw")

        # insert background image
        self.window.config(bg = "#FFFFFF")
        
        self.app_title1 = tk.Label(self.window, text = "PUP", fg = "#0818A8", bg = "white", font=("Arial",55,"bold"))
        self.app_title2 = tk.Label(self.window, text = "TRACE", fg = "red", bg = "white", font=("Arial",55,"bold"))
        self.app_title3 = tk.Label(self.window, text = "PUP CONTACT TRACING APP", fg = "gray", bg = "white", font=("Arial",20,"bold"))
        self.app_title1.place(x = 560, y = 120, width = 250, height = 90)
        self.app_title2.place(x = 760, y = 120, width = 250, height = 90)
        self.app_title3.place(x = 585, y = 195, width = 450, height = 22)

        # Buttons
        self.register_Button = tk.Button(self.window, text = "REGISTER", command = self.register_window, fg = "white", bg = "#40B5AD", font=("Century Gothic",24,"bold"))
        self.search_Button = tk.Button(self.window, text = "SEARCH", command = self.search_window, fg = "white", bg = "#40B5AD", font=("Century Gothic",24,"bold"), )
        self.exit_Button = tk.Button(self.window, text = "EXIT", command = self.exit, fg = "white", bg = "#40B5AD", font=("Century Gothic",24,"bold"), )
        self.register_Button.place(x = 670, y = 340, width = 250, height = 90)
        self.search_Button.place(x = 670, y = 450, width = 250, height = 90)
        self.exit_Button.place(x = 670, y = 560, width = 250, height = 90)

        self.window.mainloop()

    def register_window(self):
        from Obtain import Register
        self.window.destroy()
        Register()

    def search_window(self):
        from Search import Search
        self.window.destroy()
        Search()

    def exit(self):
        self.window.destroy()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    App = ContactTracing()
    App.run()