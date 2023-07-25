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

        self.respondent_details = tk.Label(self.window, text = "Respondent Details", fg = "#494F55", bg = "white", font=("Helvetica",15,"bold"))
        self.respondent_details.place(x = 290, y = 143, width = 240, height = 22)

        # get name Name
        self.name_label = tk.Label(self.window, text = "Name", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.name_label.place(x = 320, y = 175, width = 45, height = 20)

        # textbox for Name
        self.name_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.name_textbox.place(x = 323 , y = 195, width = 230, height = 30)
        # self.name_suffix_textbox.insert(0, " Suffix (e.g. Sr., Jr., III)")   

        # get Age 
        self.age_label = tk.Label(self.window, text = "Age", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.age_label.place(x = 320, y = 240, width = 36, height = 20)

        # textbox for Age
        self.age_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.age_textbox.place(x = 323 , y = 260, width = 230, height = 30)

        # get Birthday 
        self.birthday_label = tk.Label(self.window, text = "Birthday", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.birthday_label.place(x = 320, y = 305, width = 65, height = 20)

        # textbox for Birthday
        self.birthday_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.birthday_textbox.place(x = 323 , y = 325, width = 230, height = 30)

        # get email address 
        self.email_address_label = tk.Label(self.window, text = "Email Address", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.email_address_label.place(x = 567, y = 175, width = 130, height = 20)

        # textbox for email address
        self.email_address_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.email_address_textbox .place(x = 580, y = 195, width = 230, height = 30)

        # get contact number
        self.contact_number_label = tk.Label(self.window, text = "Contact Number", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.contact_number_label.place(x = 572, y = 240, width = 130, height = 20)

        # textbox for contact number
        self.contact_number_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.contact_number_textbox .place(x = 580, y = 260, width = 230, height = 30)
        
        # get Gender 
        self.gender_label = tk.Label(self.window, text = "Gender", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.gender_label.place(x = 575, y = 305, width = 60, height = 20)

        # textbox for Gender
        self.gender_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.gender_textbox.place(x = 580 , y = 325, width = 230, height = 30)

        # get address
        self.address_label = tk.Label(self.window, text = "Address", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.address_label.place(x = 322, y = 370, width = 65, height = 20)

        # textbox for address
        self.address_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.address_textbox .place(x = 323, y = 390, width = 488, height = 30)
        
        # contact person 
        self.contact_person_details = tk.Label(self.window, text = "Contact Person Details", fg = "#494F55", bg = "white", font=("Helvetica",15,"bold"))
        self.contact_person_details.place(x = 850, y = 143, width = 240, height = 22)
        
        # get name of contact person
        self.name_label = tk.Label(self.window, text = "Name", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.name_label.place(x = 865, y = 175, width = 45, height = 20)
        
        # textbox for name of contact person
        self.cp_name_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.cp_name_textbox.place(x = 868 , y = 195, width = 230, height = 30)

        # get name of contact person
        self.name_label = tk.Label(self.window, text = "Contact Number", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.name_label.place(x = 865, y = 240, width = 120, height = 20)
        
        # textbox for name of contact person
        self.cp_contact_number_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.cp_contact_number_textbox.place(x = 868 , y = 260, width = 230, height = 30)

        # get email address of contact person
        self.cp_email_address_label = tk.Label(self.window, text = "Email Address", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.cp_email_address_label.place(x = 865, y = 305, width = 110, height = 20)

        # textbox for email address of contact person
        self.cp_email_address_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.cp_email_address_textbox.place(x = 868 , y = 325, width = 230, height = 30)

        # get relationship to contact person
        self.relationship_to_cp_label = tk.Label(self.window, text = "Relationship to Contact Person", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.relationship_to_cp_label.place(x = 867, y = 370, width = 225, height = 20)

        # textbox for relationship to contact person
        self.relationship_to_cp_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.relationship_to_cp_textbox.place(x = 868 , y = 390, width = 230, height = 30)

        # Health Declaration 
        self.health_declaration = tk.Label(self.window, text = "Health Declaration", fg = "#494F55", bg = "white", font=("Helvetica",15,"bold"))
        self.health_declaration.place(x = 305, y = 453, width = 200, height = 22)

        # ask question "Have you been vaccinated for COVID-19?"
        self.ques1_label = tk.Label(self.window, text = "1. Have you been vaccinated for COVID-19?", fg = "black", bg = "white", font=("Segoe UI",13))
        self.ques1_label.place(x = 320, y = 485, width = 335, height = 20)
        
        # radio buttons for choices
        self.vaccinated_choice = IntVar()
        self.vaccinated_choice1_radio = Radiobutton(self.window, text="Not Yet", font=("MS Sans Serif", 11), bg = "white", variable=self.vaccinated_choice, value="1")
        self.vaccinated_choice1_radio.place(x=340, y=507)

        self.vaccinated_choice2_radio = Radiobutton(self.window, text="1st Dose", font=("MS Sans Serif", 11), bg = "white", variable=self.vaccinated_choice, value="2")
        self.vaccinated_choice2_radio.place(x=340, y=530)

        self.vaccinated_choice3_radio = Radiobutton(self.window, text="2nd Dose (Fully Vaccinated)", font=("MS Sans Serif", 11), bg = "white", variable=self.vaccinated_choice, value="3")
        self.vaccinated_choice3_radio.place(x=340, y=553)

        self.vaccinated_choice4_radio = Radiobutton(self.window, text="1st Booster Shot", font=("MS Sans Serif", 11), bg = "white", variable=self.vaccinated_choice, value="4")
        self.vaccinated_choice4_radio.place(x=490, y=507)

        self.vaccinated_choice5_radio = Radiobutton(self.window, text="2nd Booster Shot", font=("MS Sans Serif", 11), bg = "white", variable=self.vaccinated_choice, value="5")
        self.vaccinated_choice5_radio.place(x=490, y=530)

        # ask question "Are you experiencing any symptoms in the past 7 days such as:"
        self.ques2_label = tk.Label(self.window, text = "2. Are you experiencing any symptoms such as:", fg = "black", bg = "white", font=("Segoe UI",13))
        self.ques2_label.place(x = 320, y = 600, width = 358, height = 20)
        
        # check buttons for choices
        self.fever_checkbox = tk.Checkbutton(self.window, text="Fever", font=("MS Sans Serif", 11), bg = "white")
        self.fever_checkbox.place(x=340, y=622)

        self.cough_checkbox = tk.Checkbutton(self.window, text="Cough", font=("MS Sans Serif", 11), bg = "white")
        self.cough_checkbox.place(x=340, y=642)

        self.colds_checkbox = tk.Checkbutton(self.window, text="Colds", font=("MS Sans Serif", 11), bg = "white")
        self.colds_checkbox.place(x=340, y=662)

        self.sore_threat_checkbox = tk.Checkbutton(self.window, text="Sore throat", font=("MS Sans Serif", 11), bg = "white")
        self.sore_threat_checkbox.place(x=340, y=682)

        self.muscle_pain_checkbox = tk.Checkbutton(self.window, text="Muscle/body pains", font=("MS Sans Serif", 11), bg = "white")
        self.muscle_pain_checkbox.place(x=340, y=702)

        self.headache_checkbox = tk.Checkbutton(self.window, text="Headache", font=("MS Sans Serif", 11), bg = "white")
        self.headache_checkbox.place(x=490, y=622)

        self.shortness_of_breath_checkbox = tk.Checkbutton(self.window, text="Shortness of Breath", font=("MS Sans Serif", 11), bg = "white")
        self.shortness_of_breath_checkbox.place(x=490, y=642)

        self.fatigue_checkbox = tk.Checkbutton(self.window, text="Fatigue", font=("MS Sans Serif", 11), bg = "white")
        self.fatigue_checkbox.place(x=490, y=662)

        self.loss_of_taste_checkbox = tk.Checkbutton(self.window, text="Lost of taste", font=("MS Sans Serif", 11), bg = "white")
        self.loss_of_taste_checkbox.place(x=490, y=682)

        self.loss_of_smell_checkbox = tk.Checkbutton(self.window, text="Loss of smell", font=("MS Sans Serif", 11), bg = "white")
        self.loss_of_smell_checkbox.place(x=490, y=702)

        # ask question "Have you had exposure to a probable or confirmed case in the last 14 days?"
        self.ques3_label = tk.Label(self.window, text = "3. Have you had exposure to a probable or", fg = "black", bg = "white", font=("Segoe UI",13))
        self.ques3_label.place(x = 680, y = 483, width = 450, height = 20)

        self.ques3_label = tk.Label(self.window, text = "confirmed case in the last 14 days?", fg = "black", bg = "white", font=("Segoe UI",13))
        self.ques3_label.place(x = 682, y = 505, width = 420, height = 20)
        
        # radio buttons for choices
        self.exposure_choice = IntVar()
        self.exposure_choice1_radio = Radiobutton(self.window, text="Yes", font=("MS Sans Serif", 11), bg = "white", variable=self.exposure_choice, value="1")
        self.exposure_choice1_radio.place(x=765, y=530)

        self.exposure_choice2_radio = Radiobutton(self.window, text="No", font=("MS Sans Serif", 11), bg = "white", variable=self.exposure_choice, value="2")
        self.exposure_choice2_radio.place(x=765, y=553)

        self.exposure_choice3_radio = Radiobutton(self.window, text="Uncertain", font=("MS Sans Serif", 11), bg = "white", variable=self.exposure_choice, value="3")
        self.exposure_choice3_radio.place(x=765, y=576)

        # button for submit entry
        self.add_info_Button = tk.Button(self.window, text = "SUBMIT", fg = "white", bg = "#008080", font=("Century Gothic",16,"bold"))
        self.add_info_Button.place(x = 760, y = 645, width = 155, height = 55)

        # button for clear entry
        self.add_info_Button = tk.Button(self.window, text = "CLEAR", fg = "white", bg = "#008080", font=("Century Gothic",16,"bold"))
        self.add_info_Button.place(x = 920, y = 645, width = 155, height = 55)
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    App = Register()
    App.run()