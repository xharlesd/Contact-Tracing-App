# Input user data

# import necessary modules to be used
from tkinter import *
from tkinter import ttk
import tkinter as tk

# class add entry
class Register():
    """"""
    # constructor
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Contact Tracing App")  # program title
        self.window.geometry('1000x700')  # tkinter frame window

        # declare variables    
        app_title = tk.Label(self.window, text = "PUP CONTACT TRACING APP", fg = "gray", bg = "white", font=("Arial",20,"bold"))
        app_title.place(x = 455, y = 155, width = 450, height = 20)
    
    # tkinter window

    # get name 
    # textbox for name

    # get age
    # textbox for age

    # get gender
    # radio button for gender

    # get address
    # textbox for address

    # get contact number
    # textbox for contact number (11 digits only)

    # get email address 
    # textbox for email address

    # get contact number of contact person
    # textbox for contact number (11 digits only)

    # get name of contact person
    # textbox for name of contact person

    # get email address of contact person
    # textbox for email address of contact person

    # get relationship to contact person
    # textbox for relationship to contact person

    # ask question "Have you been vaccinated for COVID-19?"
    # radio button for choices

    # ask question "Are you experiencing any symptoms in the past 7 days such as:"
    # checkbox for choices

    # ask question "Have you had exposure to a probable or confirmed case in the last 14 days?"
    # radio button for choices

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    App = Register()
    App.run()