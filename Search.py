# Search for user data

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

        # tkinter window
        self.window.title("Contact Tracing App")  # program title
        self.window.geometry('1190x820')  # tkinter frame window
        red_frame = tk.Frame(bd=0, highlightthickness=0, background="#800000")
        white_frame = tk.Frame(bd=0, highlightthickness=0, background="white")

        red_frame.place(x=0, y=0, relwidth=0.4, relheight=1, anchor="nw")
        white_frame.place(relx=0.2, y=0, relwidth=0.8, relheight=1, anchor="nw")
        
        self.app_title1 = tk.Label(self.window, text = "PUP", fg = "#0818A8", bg = "white", font=("Arial",30,"bold"))
        self.app_title2 = tk.Label(self.window, text = "TRACE", fg = "red", bg = "white", font=("Arial",30,"bold"))
        self.app_title3 = tk.Label(self.window, text = "PUP CONTACT TRACING APP", fg = "gray", bg = "white", font=("Arial",11,"bold"))

        self.app_title1.place(x = 596, y = 18, width = 100, height = 90)
        self.app_title2.place(x = 685, y = 18, width = 140, height = 90)
        self.app_title3.place(x = 488, y = 76, width = 450, height = 22)

        # Label, text box, and button for search
        self.search_label = tk.Label(self.window, text = "Reference No.", fg = "#494F55", bg = "white", font=("Ebrima",17,"bold"))
        self.search_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.search_Button = tk.Button(self.window, text = "SEARCH", command=self.search_data, fg = "white", bg = "#008080", font=("Century Gothic",12,"bold"))
        self.search_label.place(x = 430, y = 175, width = 175, height = 20)
        self.search_textbox.place(x = 597 , y = 168, width = 235, height = 30)
        self.search_Button.place(x = 843, y = 165, width = 71, height = 35)

        # Canvas frame for results
        canvas1 = tk.Canvas(self.window, width = 720, height = 400, bg = "black")
        canvas2 = tk.Canvas(self.window, width = 710, height = 390, bg = "#F2F3F5")
        canvas1.place(x = 345, y = 275)
        canvas2.place(x = 350, y = 280)

        # Labels for searched data
        self.respondent = tk.Label(self.window, text="RESPONDENT", fg = "#002244", bg = "#F5F5F5", font=("Franklin Gothic Demi",14))
        self.contact_person = tk.Label(self.window, text="CONTACT PERSON", fg = "#002244", bg = "#F2F3F5", font=("Franklin Gothic Demi",14))
        self.health_decla = tk.Label(self.window, text="HEALTH DECLARATION", fg = "#002244", bg = "#F2F3F5", font=("Franklin Gothic Demi",14))
        self.respondent.place(x=350, y=295, width = 155, height = 35)
        self.contact_person.place(x=725, y=295, width = 155, height = 35)
        self.health_decla.place(x=370, y=515, width = 190, height = 35)

        # Respondent
        self.name = tk.Label(self.window, text="NAME",  fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.age = tk.Label(self.window, text="AGE",  fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.birthday = tk.Label(self.window, text="DATE OF BIRTH",  fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.gender = tk.Label(self.window, text="GENDER", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.email_address = tk.Label(self.window, text="EMAIL ADDRESS", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.contact_number = tk.Label(self.window, text="CONTACT NO.", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.address = tk.Label(self.window, text="ADDRESS", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))

        self.name.place(x=365, y=325, width = 70, height = 35)  
        self.age.place(x=365, y=352, width = 55, height = 30)
        self.birthday.place(x=366, y=375, width = 130, height = 35)
        self.gender.place(x=367, y=400, width = 80, height = 35)
        self.email_address.place(x=370, y=425, width = 130, height = 35)
        self.contact_number.place(x=371, y=450, width = 105, height = 35)
        self.address.place(x=370, y=475, width = 80, height = 35)

        self.display_name = tk.Label(self.window, anchor="w", justify="left", fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 12), )
        self.display_age = tk.Label(self.window, anchor="w", justify="left", fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 12), )
        self.display_birthday = tk.Label(self.window, anchor="w", justify="left", fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 12), )
        self.display_gender = tk.Label(self.window, anchor="w", justify="left", fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 12), )
        self.display_email_address = tk.Label(self.window, anchor="w", justify="left", fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 12), )
        self.display_contact = tk.Label(self.window, anchor="w", justify="left", fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 12), )
        self.display_address = tk.Label(self.window, anchor="w", justify="left", fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 12), )

        self.display_name.place(x=520, y=330, width = 200, height = 25)
        self.display_age.place(x=520, y=355, width = 200, height = 25)
        self.display_birthday.place(x=520, y=380, width = 200, height = 25)
        self.display_gender.place(x=520, y=405, width = 200, height = 25)
        self.display_email_address.place(x=520, y=430, width = 200, height = 25)
        self.display_contact.place(x=520, y=455, width = 200, height = 25)
        self.display_address.place(x=520, y=480, width = 200, height = 25)

        # Contact Person
        self.cp_name = tk.Label(self.window, text="NAME", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.cp_contact = tk.Label(self.window, text="CONTACT NO.", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.cp_email = tk.Label(self.window, text="EMAIL ADD.", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.cp_relationship = tk.Label(self.window, text="RELATIONSHIP", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))

        self.cp_name.place(x=720, y=325, width = 80, height = 35)
        self.cp_contact.place(x=735, y=350, width = 100, height = 35)
        self.cp_email.place(x=735, y=375, width = 90, height = 35)
        self.cp_relationship.place(x=735, y=400, width = 110, height = 35)

        self.display_cp_name = tk.Label(self.window, anchor="w", justify="left", fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 12), )
        self.display_cp_contact = tk.Label(self.window, anchor="w", justify="left", fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 12), )
        self.display_cp_email = tk.Label(self.window, anchor="w", justify="left", fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 12), )
        self.display_cp_relationship = tk.Label(self.window, anchor="w", justify="left", fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 12), )

        self.display_cp_name.place(x=875, y=325, width = 130, height = 35)
        self.display_cp_contact.place(x=875, y=350, width = 130, height = 35)
        self.display_cp_email.place(x=875, y=375, width = 130, height = 35)
        self.display_cp_relationship.place(x=875, y=400, width = 130, height = 35)

        # Health Declaration
        self.ques1 = tk.Label(self.window, text="1. Have you been vaccinated for COVID-19?", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.ques2 = tk.Label(self.window, text="2. Are you experiencing any symptoms such as:", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))
        self.ques3 = tk.Label(self.window, text="3. Have you had exposure to a probable or confirmed case in the last 14 days?", fg = "#1F2022", bg = "#F2F3F5", font=("Franklin Gothic Demi",12))

        self.ques1.place(x=365, y=550, width = 330, height = 20)
        self.ques2.place(x=370, y=580, width = 350, height = 20)
        self.ques3.place(x=355, y=633, width = 600, height = 20)

        self.display_ques1 = tk.Label(self.window, anchor="w", justify="left", fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 12), )
        self.display_ques2 = tk.Label(self.window, anchor="w", justify="left", fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 12), )
        self.display_ques3 = tk.Label(self.window, anchor="w", justify="left", fg = "#1F2022", bg = "#F2F3F5", font=("MS Sans Serif", 12), )

        self.display_ques1.place(x=720, y=550, width = 270, height = 20)
        self.display_ques2.place(x=390, y=605, width = 630, height = 20)
        self.display_ques3.place(x=942, y=634, width = 105, height = 20)


        # Buttons
        self.back_Button = tk.Button(self.window, text = "BACK", command = self.go_back_main, fg = "white", bg = "#7E191B", font=("Century Gothic",12,"bold"))
        self.exit_Button = tk.Button(self.window, text = "EXIT", command = self.exit, fg = "white", bg = "#7E191B", font=("Century Gothic",12,"bold"))
        self.clear_Button = tk.Button(self.window, text = "CLEAR", command = self.clear_info, fg = "white", bg = "#008080", font=("Century Gothic",14,"bold"))

        self.back_Button.place(x = 40, y = 680, width = 155, height = 45)
        self.exit_Button.place(x = 40, y = 740, width = 155, height = 45)
        self.clear_Button.place(x = 950, y = 725, width = 140, height = 45)

    def go_back_main(self):
        from Main import ContactTracing
        self.window.destroy()
        ContactTracing()

    def exit(self):
        messagebox.askquestion("EXIT PROGRAM", "Are you sure?")
        self.window.destroy()

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
            self.display_ques1.configure(text = f"{row[11]}")
            self.display_ques2.configure(text = f"{row[12]}")
            self.display_ques3.configure(text = f"{row[13]}")

        else: 
            messagebox.showerror("ERROR", "Reference Number not found. If you forgot, try to enter your full name.")

    def clear_info(self):
            self.search_textbox.delete(0, END)
            self.display_name.configure(text = "")
            self.display_age.configure(text = "")
            self.display_birthday.configure(text = "")
            self.display_gender.configure(text = "")
            self.display_email_address.configure(text = "")
            self.display_contact.configure(text = "")
            self.display_address.configure(text = "")
            self.display_cp_name.configure(text = "")
            self.display_cp_contact.configure(text = "")
            self.display_cp_email.configure(text = "")
            self.display_cp_relationship.configure(text = "")
            self.display_ques1.configure(text = "")
            self.display_ques2.configure(text = "")
            self.display_ques3.configure(text = "")

    def run(self):
        self.window.mainloop()
        
if __name__ == "__main__":
    App = Search()
    App.run()

# END OF PROGRAM