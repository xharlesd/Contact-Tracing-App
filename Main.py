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
# import classes (soon)


# App Class
class ContactTracing():

    # constructor
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Contact Tracing App")  # program title
        self.window.geometry('1190x820')  # tkinter frame window
       
        original_image = Image.open("Puppic.png")
        resized_image = original_image.resize((420, 950))  
        background_image = ImageTk.PhotoImage(resized_image)

        # Create a canvas to display the background image
        self.canvas = tk.Canvas(self.window, width=400, height=900)
        self.canvas.pack(side=LEFT)
        self.canvas.create_image(0, 0, image=background_image, anchor="nw")

        self.window.config(bg = "#FFFFFF")
        
        self.app_title = tk.Label(self.window, text = "PUP", fg = "#0818A8", bg = "white", font=("Arial",55,"bold"))
        self.app_title.place(x = 560, y = 120, width = 250, height = 90)

        self.app_title = tk.Label(self.window, text = "TRACE", fg = "red", bg = "white", font=("Arial",55,"bold"))
        self.app_title.place(x = 760, y = 120, width = 250, height = 90)

        self.app_title = tk.Label(self.window, text = "PUP CONTACT TRACING APP", fg = "gray", bg = "white", font=("Arial",20,"bold"))
        self.app_title.place(x = 585, y = 195, width = 450, height = 22)

        # button for add entry
        self.register_Button = tk.Button(self.window, text = "REGISTER", command = self.register_window, fg = "white", bg = "#40B5AD", font=("Century Gothic",24,"bold"))
        self.register_Button.place(x = 670, y = 340, width = 250, height = 90)
        
        # button for search entry
        self.search_Button = tk.Button(self.window, text = "SEARCH", command = self.search_window, fg = "white", bg = "#40B5AD", font=("Century Gothic",24,"bold"), )
        self.search_Button.place(x = 670, y = 450, width = 250, height = 90)

        self.window.mainloop()

    def register_window(self):
        from Obtain import Register
        self.window.destroy()
        Register()

    def search_window(self):
        from Search import Search
        self.window.destroy()
        Search()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    App = ContactTracing()
    App.run()