# Search user data

# import necessary modules to be used
from tkinter import *
from tkinter import messagebox
import tkinter as tk 
import csv

# class search
class Search():
    # constructor
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Contact Tracing App")  # program title
        self.window.geometry('1190x820')  # tkinter frame window

        # tkinter window
        red_frame = tk.Frame(bd=0, highlightthickness=0, background="#800000")
        white_frame = tk.Frame(bd=0, highlightthickness=0, background="white")
        red_frame.place(x=0, y=0, relwidth=0.4, relheight=1, anchor="nw")
        white_frame.place(relx=0.2, y=0, relwidth=0.8, relheight=1, anchor="nw")
        
        self.app_title = tk.Label(self.window, text = "PUP", fg = "#0818A8", bg = "white", font=("Arial",30,"bold"))
        self.app_title.place(x = 596, y = 18, width = 100, height = 90)

        self.app_title = tk.Label(self.window, text = "TRACE", fg = "red", bg = "white", font=("Arial",30,"bold"))
        self.app_title.place(x = 685, y = 18, width = 140, height = 90)

        self.app_title = tk.Label(self.window, text = "PUP CONTACT TRACING APP", fg = "gray", bg = "white", font=("Arial",11,"bold"))
        self.app_title.place(x = 488, y = 76, width = 450, height = 22)

        # text box for search
        self.search_label = tk.Label(self.window, text = "Reference No.", fg = "#494F55", bg = "white", font=("Ebrima",17,"bold"))
        self.search_label.place(x = 430, y = 175, width = 175, height = 20)
        self.search_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.search_textbox.place(x = 597 , y = 168, width = 235, height = 30)
        
        # define search function
        self.search_Button = tk.Button(self.window, text = "SEARCH", command=self.search_data, fg = "white", bg = "#008080", font=("Century Gothic",12,"bold"))
        self.search_Button.place(x = 843, y = 165, width = 71, height = 35)
    
        canvas1 = tk.Canvas(self.window, width = 720, height = 430, bg = "black")
        canvas1.place(x = 345, y = 275)

        canvas2 = tk.Canvas(self.window, width = 710, height = 420, bg = "#F2F3F5")
        canvas2.place(x = 350, y = 280)

        # Labels for searched data
        self.contact_person = tk.Label(self.window, text="RESPONDENT", fg = "#002244", bg = "#F2F3F5", font=("Franklin Gothic Demi",14))
        self.contact_person.place(x=350, y=295, width = 155, height = 35)

        self.name = tk.Label(self.window, text="NAME",  fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.name.place(x=365, y=325, width = 70, height = 35)
        self.display_name = tk.Label(self.window, fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 11), )
        self.display_name.place(x=510, y=330, width = 200, height = 25)

        self.age = tk.Label(self.window, text="AGE",  fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.age.place(x=365, y=352, width = 55, height = 30)
        self.display_age = tk.Label(self.window, fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 11), )
        self.display_age.place(x=510, y=355, width = 200, height = 25)

        self.birthday = tk.Label(self.window, text="DATE OF BIRTH",  fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.birthday.place(x=366, y=375, width = 130, height = 35)
        self.display_birthday = tk.Label(self.window, fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 11), )
        self.display_birthday.place(x=510, y=380, width = 200, height = 25)

        self.gender = tk.Label(self.window, text="GENDER", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.gender.place(x=367, y=400, width = 80, height = 35)
        self.display_gender = tk.Label(self.window, fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 11), )
        self.display_gender.place(x=510, y=405, width = 200, height = 25)

        self.email_address = tk.Label(self.window, text="EMAIL ADDRESS", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.email_address.place(x=370, y=425, width = 130, height = 35)
        self.display_email_address = tk.Label(self.window, fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 11), )
        self.display_email_address.place(x=510, y=430, width = 200, height = 25)

        self.contact_number = tk.Label(self.window, text="CONTACT NO.", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.contact_number.place(x=371, y=450, width = 105, height = 35)
        self.display_contact = tk.Label(self.window, fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 11), )
        self.display_contact.place(x=510, y=455, width = 200, height = 25)
    
        self.address = tk.Label(self.window, text="ADDRESS", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.address.place(x=370, y=475, width = 80, height = 35)
        self.display_address = tk.Label(self.window, fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 11), )
        self.display_address.place(x=510, y=480, width = 200, height = 25)


        self.contact_person = tk.Label(self.window, text="CONTACT PERSON", fg = "#002244", bg = "#F2F3F5", font=("Franklin Gothic Demi",14))
        self.contact_person.place(x=725, y=295, width = 155, height = 35)

        self.cp_name = tk.Label(self.window, text="NAME", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.cp_name.place(x=720, y=325, width = 80, height = 35)
        self.display_cp_name = tk.Label(self.window, fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 11), )
        self.display_cp_name.place(x=890, y=325, width = 100, height = 35)

        self.cp_contact = tk.Label(self.window, text="CONTACT NO.", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.cp_contact.place(x=735, y=350, width = 100, height = 35)
        self.display_cp_contact = tk.Label(self.window, fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 11), )
        self.display_cp_contact.place(x=890, y=350, width = 100, height = 35)

        self.cp_email = tk.Label(self.window, text="EMAIL ADD.", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.cp_email.place(x=735, y=375, width = 90, height = 35)
        self.display_cp_email = tk.Label(self.window, fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 11), )
        self.display_cp_email.place(x=890, y=375, width = 150, height = 35)

        self.cp_relationship = tk.Label(self.window, text="RELATIONSHIP", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.cp_relationship.place(x=735, y=400, width = 110, height = 35)
        self.display_cp_relationship = tk.Label(self.window, fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 11), )
        self.display_cp_relationship.place(x=890, y=400, width = 100, height = 35)

        # button for back entry
        self.back_Button = tk.Button(self.window, text = "BACK", command = self.go_back_main, fg = "white", bg = "#7E191B", font=("Century Gothic",12,"bold"))
        self.back_Button.place(x = 40, y = 680, width = 155, height = 45)

        # button for exit entry
        self.exit_Button = tk.Button(self.window, text = "EXIT", command = self.exit, fg = "white", bg = "#7E191B", font=("Century Gothic",12,"bold"))
        self.exit_Button.place(x = 40, y = 740, width = 155, height = 45)

    def go_back_main(self):
        from Main import ContactTracing
        self.window.destroy()
        ContactTracing()

    def exit(self):
        messagebox.askquestion("Exit Program", "Are you sure?")
        self.window.quit()


    def search_data(self):
        reference_number = self.search_textbox.get()
        
        data_list = []

        with open("data_list.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:        
                if reference_number in row:
                    data_list.append(row)
                    break

        if data_list:          
            self.display_name.configure(text = f"{row[0]}")
            self.display_age.configure(text = f"{row[1]}")
            self.display_birthday.configure(text = f"{row[2]}")
            self.display_gender.configure(text = f"{row[3]}")
            self.display_email_address.configure(text = f"{row[4]}")
            self.display_contact.configure(text = f"{row[5]}")
            self.display_address.configure(text = f"{row[6]}")
            self.display_cp_name.configure(text = f"{row[7]}")
            self.display_cp_contact.configure(text = f"{row[8]}")
            self.display_cp_email.configure(text = f"{row[9]}")
            self.display_cp_relationship.configure(text = f"{row[10]}")

    def run(self):
        self.window.mainloop()
        
if __name__ == "__main__":
    App = Search()
    App.run()