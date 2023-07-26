# Input user data

# import necessary modules to be used
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk 
import sqlite3 as db

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

        self.name_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.name_textbox.place(x = 323 , y = 195, width = 230, height = 30)
        # self.name_suffix_textbox.insert(0, " Suffix (e.g. Sr., Jr., III)")   

        self.age_label = tk.Label(self.window, text = "Age", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.age_label.place(x = 320, y = 240, width = 36, height = 20)

        self.age_spinbox = tk.Spinbox(self.window, from_= 0, to = 150, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.age_spinbox.place(x = 323 , y = 260, width = 230, height = 30)

        self.birthday_label = tk.Label(self.window, text = "Birthday", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.birthday_label.place(x = 320, y = 305, width = 65, height = 20)

        self.birthday_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.birthday_textbox.place(x = 323 , y = 325, width = 230, height = 30)

        self.email_address_label = tk.Label(self.window, text = "Email Address", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.email_address_label.place(x = 567, y = 175, width = 130, height = 20)

        self.email_address_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.email_address_textbox.place(x = 580, y = 195, width = 230, height = 30)

        self.contact_number_label = tk.Label(self.window, text = "Contact Number", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.contact_number_label.place(x = 572, y = 240, width = 130, height = 20)

        self.contact_number_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.contact_number_textbox.place(x = 580, y = 260, width = 230, height = 30)

        self.gender_label = tk.Label(self.window, text = "Gender", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.gender_label.place(x = 575, y = 305, width = 60, height = 20)

        self.gender_choice = tk.IntVar()

        self.gender_choice1_radio = tk.Radiobutton(self.window, text="Male", font=("MS Sans Serif", 12), bg = "white", variable=self.gender_choice, value="1")
        self.gender_choice1_radio.place(x=600, y=325)

        self.gender_choice2_radio = tk.Radiobutton(self.window, text="Female", font=("MS Sans Serif", 12), bg = "white", variable=self.gender_choice, value="2")
        self.gender_choice2_radio.place(x=680, y=325)


        self.address_label = tk.Label(self.window, text = "Address", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.address_label.place(x = 322, y = 370, width = 65, height = 20)

        self.address_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.address_textbox.place(x = 323, y = 390, width = 488, height = 30)
        
        # contact person details
        self.contact_person_details = tk.Label(self.window, text = "Contact Person Details", fg = "#494F55", bg = "white", font=("Helvetica",15,"bold"))
        self.contact_person_details.place(x = 850, y = 143, width = 240, height = 22)
        
        self.cp_name_label = tk.Label(self.window, text = "Name", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.cp_name_label.place(x = 865, y = 175, width = 45, height = 20)

        self.cp_name_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.cp_name_textbox.place(x = 868 , y = 195, width = 230, height = 30)

        self.name_label = tk.Label(self.window, text = "Contact Number", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.name_label.place(x = 865, y = 240, width = 120, height = 20)

        self.cp_contact_number_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.cp_contact_number_textbox.place(x = 868 , y = 260, width = 230, height = 30)

        self.cp_email_address_label = tk.Label(self.window, text = "Email Address", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.cp_email_address_label.place(x = 865, y = 305, width = 110, height = 20)

        self.cp_email_address_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.cp_email_address_textbox.place(x = 868 , y = 325, width = 230, height = 30)

        self.relationship_to_cp_label = tk.Label(self.window, text = "Relationship to Contact Person", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.relationship_to_cp_label.place(x = 867, y = 370, width = 225, height = 20)

        self.relationship_to_cp_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.relationship_to_cp_textbox.place(x = 868 , y = 390, width = 230, height = 30)

        # Health Declaration 
        self.health_declaration = tk.Label(self.window, text = "Health Declaration", fg = "#494F55", bg = "white", font=("Helvetica",15,"bold"))
        self.health_declaration.place(x = 305, y = 453, width = 200, height = 22)

        # ask question "Have you been vaccinated for COVID-19?"
        self.ques1_label = tk.Label(self.window, text = "1. Have you been vaccinated for COVID-19?", fg = "black", bg = "white", font=("Segoe UI",13))
        self.ques1_label.place(x = 320, y = 485, width = 335, height = 20)
        
        self.vaccinated_choice = tk.IntVar()

        self.vaccinated_choice1_radio = tk.Radiobutton(self.window, text="Not Yet", font=("MS Sans Serif", 11), bg = "white", variable=self.vaccinated_choice, value="1")
        self.vaccinated_choice1_radio.place(x=340, y=507)

        self.vaccinated_choice2_radio = tk.Radiobutton(self.window, text="1st Dose", font=("MS Sans Serif", 11), bg = "white", variable=self.vaccinated_choice, value="2")
        self.vaccinated_choice2_radio.place(x=340, y=530)

        self.vaccinated_choice3_radio = tk.Radiobutton(self.window, text="2nd Dose (Fully Vaccinated)", font=("MS Sans Serif", 11), bg = "white", variable=self.vaccinated_choice, value="3")
        self.vaccinated_choice3_radio.place(x=340, y=553)

        self.vaccinated_choice4_radio = tk.Radiobutton(self.window, text="1st Booster Shot", font=("MS Sans Serif", 11), bg = "white", variable=self.vaccinated_choice, value="4")
        self.vaccinated_choice4_radio.place(x=490, y=507)

        self.vaccinated_choice5_radio = tk.Radiobutton(self.window, text="2nd Booster Shot", font=("MS Sans Serif", 11), bg = "white", variable=self.vaccinated_choice, value="5")
        self.vaccinated_choice5_radio.place(x=490, y=530)

        # ask question "Are you experiencing any symptoms in the past 7 days such as:"
        self.ques2_label = tk.Label(self.window, text = "2. Are you experiencing any symptoms such as:", fg = "black", bg = "white", font=("Segoe UI",13))
        self.ques2_label.place(x = 320, y = 600, width = 358, height = 20)

        self.fever_symptom = StringVar(value ="No")
        self.fever_checkbox = tk.Checkbutton(self.window, text="Fever", variable = self.fever_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = "Yes", offvalue = "No")
        self.fever_checkbox.place(x=340, y=622)

        self.cough_symptom = StringVar(value = "No")
        self.cough_checkbox = tk.Checkbutton(self.window, text="Cough", variable = self.cough_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = "Yes", offvalue = "No")
        self.cough_checkbox.place(x=340, y=642)

        self.colds_symptom = StringVar(value = "No")
        self.colds_checkbox = tk.Checkbutton(self.window, text="Colds", variable = self.colds_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = "Yes", offvalue = "No")
        self.colds_checkbox.place(x=340, y=662)

        self.sore_throat_symptom = StringVar(value = "No")
        self.sore_throat_checkbox = tk.Checkbutton(self.window, text="Sore throat", variable = self.sore_throat_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = "Yes", offvalue = "No")
        self.sore_throat_checkbox.place(x=340, y=682)

        self.muscle_pain_symptom = StringVar(value = "No")
        self.muscle_pain_checkbox = tk.Checkbutton(self.window, text="Muscle/body pains", variable = self.muscle_pain_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = "Yes", offvalue = "No")
        self.muscle_pain_checkbox.place(x=340, y=702)

        self.headache_symptom = StringVar(value = "No")
        self.headache_checkbox = tk.Checkbutton(self.window, text="Headache", variable = self.headache_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = "Yes", offvalue = "No")
        self.headache_checkbox.place(x=490, y=622)

        self.shortness_of_breath_symptom = StringVar(value = "No")
        self.shortness_of_breath_checkbox = tk.Checkbutton(self.window, text="Shortness of Breath", variable = self.shortness_of_breath_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = "Yes", offvalue = "No")
        self.shortness_of_breath_checkbox.place(x=490, y=642)

        self.fatigue_symptom = StringVar(value = "No")
        self.fatigue_checkbox = tk.Checkbutton(self.window, text="Fatigue", variable = self.fatigue_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = "Yes", offvalue = "No")
        self.fatigue_checkbox.place(x=490, y=662)

        self.loss_of_taste_symptom = StringVar(value = "No")
        self.loss_of_taste_checkbox = tk.Checkbutton(self.window, text="Lost of taste", variable = self.loss_of_taste_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = "Yes", offvalue = "No")
        self.loss_of_taste_checkbox.place(x=490, y=682)

        self.loss_of_smell_symptom = StringVar(value = "No")
        self.loss_of_smell_checkbox = tk.Checkbutton(self.window, text="Loss of smell", variable = self.loss_of_smell_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = "Yes", offvalue = "No")
        self.loss_of_smell_checkbox.place(x=490, y=702)

        # ask question "Have you had exposure to a probable or confirmed case in the last 14 days?"
        self.ques3_label = tk.Label(self.window, text = "3. Have you had exposure to a probable or", fg = "black", bg = "white", font=("Segoe UI",13))
        self.ques3_label.place(x = 680, y = 483, width = 450, height = 20)

        self.ques3_label = tk.Label(self.window, text = "confirmed case in the last 14 days?", fg = "black", bg = "white", font=("Segoe UI",13))
        self.ques3_label.place(x = 682, y = 505, width = 420, height = 20)

        self.exposure_choice = tk.IntVar()
        self.exposure_choice1_radio = tk.Radiobutton(self.window, text="Yes", font=("MS Sans Serif", 11), bg = "white", variable=self.exposure_choice, value="1")
        self.exposure_choice1_radio.place(x=765, y=530)

        self.exposure_choice2_radio = tk.Radiobutton(self.window, text="No", font=("MS Sans Serif", 11), bg = "white", variable=self.exposure_choice, value="2")
        self.exposure_choice2_radio.place(x=765, y=553)

        self.exposure_choice3_radio = tk.Radiobutton(self.window, text="Uncertain", font=("MS Sans Serif", 11), bg = "white", variable=self.exposure_choice, value="3")
        self.exposure_choice3_radio.place(x=765, y=576)

        self.data_privacy = StringVar(value = "0")
        self.data_privacy_checkbox = tk.Checkbutton(self.window, text = "I agree to Data Privacy Consent", font=("MS Sans Serif", 11), bg = "white", variable=self.data_privacy, onvalue = "1", offvalue = "0")
        self.data_privacy_checkbox.place(x=760, y=630)

        # button for submit entry
        self.submit_Button = tk.Button(self.window, text = "SUBMIT", command = self.submit_data, fg = "white", bg = "#008080", font=("Century Gothic",16,"bold"))
        self.submit_Button.place(x = 760, y = 665, width = 155, height = 55)

        # button for clear entry
        self.clear_Button = tk.Button(self.window, text = "CLEAR", command = self.clear_info, fg = "white", bg = "#008080", font=("Century Gothic",16,"bold"))
        self.clear_Button.place(x = 920, y = 665, width = 155, height = 55)

    def submit_data(self):
        data_privacy = self.data_privacy.get()

        # respondent info
        name = str(self.name_textbox.get())
        age = str(self.age_spinbox.get())
        birthday = str(self.birthday_textbox.get())
        email_address = str(self.email_address_textbox.get())
        contact_number = str(self.contact_number_textbox.get())
        gender = str(self.gender_choice.get())
        address = str(self.address_textbox.get())

        # contact person info
        cp_name = str(self.cp_name_textbox.get())
        cp_contact_number = str(self.cp_contact_number_textbox.get())
        cp_email_address = str(self.cp_email_address_textbox.get())
        relationship_to_cp = str(self.relationship_to_cp_textbox.get())

        # health declaration
        vaccinated = str(self.vaccinated_choice.get())
        symptom_fever = str(self.fever_symptom.get())
        symptom_cough = str(self.cough_symptom.get())
        symptom_colds = str(self.colds_symptom.get())
        symptom_sore_throat = str(self.sore_throat_symptom.get())
        symptom_shortness_of_breath = str(self.shortness_of_breath_symptom.get())
        symptom_fatigue = str(self.fatigue_symptom.get())
        symptom_loss_of_taste = str(self.loss_of_taste_symptom.get())
        symptom_loss_of_smell = str(self.loss_of_smell_symptom.get())
        exposure = str(self.exposure_choice.get())

        # Create table
        conn = db.connect('data.db')
        cur  = conn.cursor()
        cur.execute("INSERT INTO Data('"+name+"', '"+age+"', '"+birthday+"', '"+email_address+"', '"+contact_number+"', '"+gender+"', '"+address+"', '"+cp_name+"', '"+cp_contact_number+"', '"+cp_email_address+"', '"+relationship_to_cp+"', '"+vaccinated+"', '"+symptom_fever+"', '"+symptom_cough+"', '"+symptom_colds+"', '"+symptom_sore_throat+"', '"+symptom_shortness_of_breath+"', '"+symptom_fatigue+"', '"+symptom_loss_of_taste+"', '"+symptom_loss_of_smell+"', '"+exposure+",'"+data_privacy+"')")
        conn.commit()
        conn.close()

    def clear_info(self):
        self.name_textbox.delete(0, END)
        self.age_spinbox.delete(0, END)
        self.birthday_textbox.delete(0, END)
        self.email_address_textbox.delete(0, END)
        self.contact_number_textbox.delete(0, END)
        self.gender_choice.set(None)
        self.address_textbox.delete(0, END)
        self.cp_name_textbox.delete(0, END)
        self.cp_contact_number_textbox.delete(0, END)
        self.cp_email_address_textbox.delete(0, END)
        self.relationship_to_cp_textbox.delete(0, END)
        self.vaccinated_choice.set(None)
        self.fever_checkbox.deselect()
        self.cough_checkbox.deselect()
        self.colds_checkbox.deselect()
        self.sore_throat_checkbox.deselect()
        self.muscle_pain_checkbox.deselect()
        self.headache_checkbox.deselect()
        self.shortness_of_breath_checkbox.deselect()
        self.fatigue_checkbox.deselect()
        self.loss_of_taste_checkbox.deselect()
        self.loss_of_smell_checkbox.deselect()
        self.exposure_choice.set(None)
        self.data_privacy_checkbox.deselect()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    App = Register()
    App.run()