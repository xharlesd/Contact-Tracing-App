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
        self.window.geometry('1200x800')  # tkinter frame window

        # tkinter window
        red_frame = tk.Frame(bd=0, highlightthickness=0, background="#800000")
        white_frame = tk.Frame(bd=0, highlightthickness=0, background="white")
        red_frame.place(x=0, y=0, relwidth=0.4, relheight=1, anchor="nw")
        white_frame.place(relx=0.2, y=0, relwidth=0.8, relheight=1, anchor="nw")
        
        self.app_title = tk.Label(self.window, text = "Sign Up", fg = "black", bg = "white", font=("Helvetica",24,"bold"))
        self.app_title.place(x = 265, y = 17, width = 120, height = 40)

        self.app_title = tk.Label(self.window, text = "Respondent Details", fg = "#494F55", bg = "white", font=("Helvetica",15,"bold"))
        self.app_title.place(x = 240, y = 87, width = 240, height = 22)

        # get name Name
        self.name_label = tk.Label(self.window, text = "Name", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.name_label.place(x = 270, y = 125, width = 45, height = 20)

        # textbox for Name
        self.name_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.name_textbox.place(x = 273 , y = 145, width = 230, height = 30)
        # self.name_suffix_textbox.insert(0, " Suffix (e.g. Sr., Jr., III)")   

        # get Age 
        self.age_label = tk.Label(self.window, text = "Age", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.age_label.place(x = 270, y = 190, width = 36, height = 20)

        # textbox for Age
        self.age_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.age_textbox.place(x = 273 , y = 210, width = 230, height = 30)

        # get Birthday 
        self.birthday_label = tk.Label(self.window, text = "Birthday", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.birthday_label.place(x = 270, y = 255, width = 65, height = 20)

        # textbox for Birthday
        self.birthday_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.birthday_textbox.place(x = 273 , y = 275, width = 230, height = 30)

        # get email address 
        self.email_address_label = tk.Label(self.window, text = "Email Address", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.email_address_label.place(x = 517, y = 125, width = 130, height = 20)

        # textbox for email address
        self.email_address_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.email_address_textbox .place(x = 530, y = 145, width = 230, height = 30)

        # get contact number
        self.contact_number_label = tk.Label(self.window, text = "Contact Number", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.contact_number_label.place(x = 522, y = 190, width = 130, height = 20)

        # textbox for contact number
        self.contact_number_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.contact_number_textbox .place(x = 530, y = 210, width = 230, height = 30)
        
        # get Gender 
        self.gender_label = tk.Label(self.window, text = "Gender", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.gender_label.place(x = 525, y = 255, width = 60, height = 20)

        # textbox for Gender
        self.gender_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.gender_textbox.place(x = 530 , y = 275, width = 230, height = 30)

        # get address
        self.address_label = tk.Label(self.window, text = "Address", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.address_label.place(x = 272, y = 320, width = 65, height = 20)

        # textbox for address
        self.address_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.address_textbox .place(x = 273, y = 340  , width = 488, height = 30)

        

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