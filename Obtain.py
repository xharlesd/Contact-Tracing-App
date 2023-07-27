# Input user data

# import necessary modules to be used
from tkinter import *
from tkinter import messagebox
import tkinter as tk 
import csv
import random

# class add entry
class Register():
    
    """"""
    # constructor
    def __init__(self):        
        self.window = tk.Tk()

        # Tkinter window
        self.window.title("Contact Tracing App")  
        self.window.geometry('1190x820')  
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

        # Respondent Details
        self.respondent_details = tk.Label(self.window, text = "Respondent Details", fg = "#494F55", bg = "white", font=("Helvetica",15,"bold"))
        self.respondent_details.place(x = 290, y = 143, width = 240, height = 22)

        self.name_label = tk.Label(self.window, text = "Name", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.age_label = tk.Label(self.window, text = "Age", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.birthday_label = tk.Label(self.window, text = "Birthday", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.email_address_label = tk.Label(self.window, text = "Email Address", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.contact_number_label = tk.Label(self.window, text = "Contact Number", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.gender_label = tk.Label(self.window, text = "Gender", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.address_label = tk.Label(self.window, text = "Address", fg = "black", bg = "white", font=("Trajan Pro",13))

        self.name_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.age_spinbox = tk.Spinbox(self.window, from_= 0, to = 150, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.birthday_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.email_address_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.contact_number_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.address_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")

        self.name_label.place(x = 320, y = 175, width = 45, height = 20)
        self.age_label.place(x = 320, y = 240, width = 36, height = 20)
        self.birthday_label.place(x = 320, y = 305, width = 65, height = 20)
        self.email_address_label.place(x = 567, y = 175, width = 130, height = 20)
        self.contact_number_label.place(x = 572, y = 240, width = 130, height = 20)
        self.gender_label.place(x = 575, y = 305, width = 60, height = 20)
        self.address_label.place(x = 322, y = 370, width = 65, height = 20)

        self.name_textbox.place(x = 323 , y = 195, width = 230, height = 30)
        self.age_spinbox.place(x = 323 , y = 260, width = 230, height = 30)
        self.birthday_textbox.place(x = 323 , y = 325, width = 230, height = 30)
        self.email_address_textbox.place(x = 580, y = 195, width = 230, height = 30)
        self.contact_number_textbox.place(x = 580, y = 260, width = 230, height = 30)
        self.address_textbox.place(x = 323, y = 390, width = 488, height = 30)

        self.gender_choice = tk.StringVar(value = '0')
        self.gender_choice1_radio = tk.Radiobutton(self.window, text="Male", font=("MS Sans Serif", 12), bg = "white", variable=self.gender_choice, value="Male")
        self.gender_choice2_radio = tk.Radiobutton(self.window, text="Female", font=("MS Sans Serif", 12), bg = "white", variable=self.gender_choice, value="Female")
        self.gender_choice1_radio.place(x=600, y=325)
        self.gender_choice2_radio.place(x=680, y=325)

        
        # Contact person details
        self.contact_person_details = tk.Label(self.window, text = "Contact Person Details", fg = "#494F55", bg = "white", font=("Helvetica",15,"bold"))
        self.contact_person_details.place(x = 850, y = 143, width = 240, height = 22)
        
        self.cp_name_label = tk.Label(self.window, text = "Name", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.cp_contact_number_label = tk.Label(self.window, text = "Contact Number", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.cp_email_address_label = tk.Label(self.window, text = "Email Address", fg = "black", bg = "white", font=("Trajan Pro",13))
        self.relationship_to_cp_label = tk.Label(self.window, text = "Relationship to Contact Person", fg = "black", bg = "white", font=("Trajan Pro",13))

        self.cp_name_label.place(x = 865, y = 175, width = 45, height = 20)
        self.cp_contact_number_label.place(x = 865, y = 240, width = 120, height = 20)
        self.cp_email_address_label.place(x = 865, y = 305, width = 110, height = 20)
        self.relationship_to_cp_label.place(x = 867, y = 370, width = 225, height = 20)

        self.cp_name_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.cp_contact_number_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.cp_email_address_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.relationship_to_cp_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")

        self.cp_name_textbox.place(x = 868 , y = 195, width = 230, height = 30)
        self.cp_contact_number_textbox.place(x = 868 , y = 260, width = 230, height = 30)
        self.cp_email_address_textbox.place(x = 868 , y = 325, width = 230, height = 30)
        self.relationship_to_cp_textbox.place(x = 868 , y = 390, width = 230, height = 30)


        # Health Declaration 
        self.health_declaration = tk.Label(self.window, text = "Health Declaration", fg = "#494F55", bg = "white", font=("Helvetica",15,"bold"))
        self.health_declaration.place(x = 305, y = 453, width = 200, height = 22)

        # Vaccination Status
        self.ques1_label = tk.Label(self.window, text = "1. Have you been vaccinated for COVID-19?", fg = "black", bg = "white", font=("Segoe UI",13))
        self.ques1_label.place(x = 320, y = 485, width = 335, height = 20)
        
        self.vaccinated_choice = tk.StringVar(value = '0')
        self.vaccinated_choice1_radio = tk.Radiobutton(self.window, text="Not Yet", font=("MS Sans Serif", 11), bg = "white", variable=self.vaccinated_choice, value="Not yet vaccinated")
        self.vaccinated_choice2_radio = tk.Radiobutton(self.window, text="1st Dose", font=("MS Sans Serif", 11), bg = "white", variable=self.vaccinated_choice, value="1st dose")
        self.vaccinated_choice3_radio = tk.Radiobutton(self.window, text="2nd Dose (Fully Vaccinated)", font=("MS Sans Serif", 11), bg = "white", variable=self.vaccinated_choice, value="2nd dose (Fully Vaccinated)")
        self.vaccinated_choice4_radio = tk.Radiobutton(self.window, text="1st Booster Shot", font=("MS Sans Serif", 11), bg = "white", variable=self.vaccinated_choice, value="1st booster shot")
        self.vaccinated_choice5_radio = tk.Radiobutton(self.window, text="2nd Booster Shot", font=("MS Sans Serif", 11), bg = "white", variable=self.vaccinated_choice, value="2nd booster shot")

        self.vaccinated_choice1_radio.place(x=340, y=507)
        self.vaccinated_choice2_radio.place(x=340, y=530)
        self.vaccinated_choice3_radio.place(x=340, y=553)
        self.vaccinated_choice4_radio.place(x=490, y=507)
        self.vaccinated_choice5_radio.place(x=490, y=530)

        # COVID-19 Symptoms
        self.ques2_label = tk.Label(self.window, text = "2. Are you experiencing any symptoms such as:", fg = "black", bg = "white", font=("Segoe UI",13))
        self.ques2_label.place(x = 320, y = 600, width = 358, height = 20)

        self.fever_symptom = BooleanVar()
        self.cough_symptom = BooleanVar()
        self.colds_symptom = BooleanVar()
        self.sore_throat_symptom = BooleanVar()
        self.muscle_pain_symptom = BooleanVar()
        self.headache_symptom = BooleanVar()
        self.shortness_of_breath_symptom = BooleanVar()
        self.fatigue_symptom = BooleanVar()
        self.loss_of_taste_symptom = BooleanVar()
        self.loss_of_smell_symptom = BooleanVar()
        self.None_of_the_above = BooleanVar()

        self.fever_checkbox = tk.Checkbutton(self.window, text="Fever", variable = self.fever_symptom, font=("MS Sans Serif", 11), bg = "white",onvalue = True, offvalue = False)
        self.cough_checkbox = tk.Checkbutton(self.window, text="Cough", variable = self.cough_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = True, offvalue = False)
        self.colds_checkbox = tk.Checkbutton(self.window, text="Colds", variable = self.colds_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = True, offvalue = False)
        self.sore_throat_checkbox = tk.Checkbutton(self.window, text="Sore throat", variable = self.sore_throat_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = True, offvalue = False)
        self.muscle_pain_checkbox = tk.Checkbutton(self.window, text="Muscle/body pains", variable = self.muscle_pain_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = True, offvalue = False)
        self.headache_checkbox = tk.Checkbutton(self.window, text="Headache", variable = self.headache_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = True, offvalue = False)
        self.shortness_of_breath_checkbox = tk.Checkbutton(self.window, text="Shortness of Breath", variable = self.shortness_of_breath_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = True, offvalue = False)
        self.fatigue_checkbox = tk.Checkbutton(self.window, text="Fatigue", variable = self.fatigue_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = True, offvalue = False)
        self.loss_of_taste_checkbox = tk.Checkbutton(self.window, text="Lost of taste", variable = self.loss_of_taste_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = True, offvalue = False)
        self.loss_of_smell_checkbox = tk.Checkbutton(self.window, text="Loss of smell", variable = self.loss_of_smell_symptom, font=("MS Sans Serif", 11), bg = "white", onvalue = True, offvalue = False)
        self.nota_checkbox = tk.Checkbutton(self.window, text="None of the Above", variable = self.None_of_the_above, font=("MS Sans Serif", 11), bg = "white", onvalue = True, offvalue = False)

        self.fever_checkbox.place(x=340, y=622)
        self.cough_checkbox.place(x=340, y=642)
        self.colds_checkbox.place(x=340, y=662)  
        self.sore_throat_checkbox.place(x=340, y=682) 
        self.muscle_pain_checkbox.place(x=340, y=702)  
        self.headache_checkbox.place(x=490, y=622)
        self.shortness_of_breath_checkbox.place(x=490, y=642) 
        self.fatigue_checkbox.place(x=490, y=662)
        self.loss_of_taste_checkbox.place(x=490, y=682)
        self.loss_of_smell_checkbox.place(x=490, y=702)
        self.nota_checkbox.place(x=340, y=722)

        # Exposure to probable patient
        self.ques3_label = tk.Label(self.window, text = "3. Have you had exposure to a probable or", fg = "black", bg = "white", font=("Segoe UI",13))
        self.ques3_label = tk.Label(self.window, text = "confirmed case in the last 14 days?", fg = "black", bg = "white", font=("Segoe UI",13))
        self.ques3_label.place(x = 680, y = 483, width = 450, height = 20)
        self.ques3_label.place(x = 682, y = 505, width = 420, height = 20)

        self.exposure_choice = tk.StringVar(value = '0')
        self.exposure_choice1_radio = tk.Radiobutton(self.window, text="Yes", font=("MS Sans Serif", 11), bg = "white", variable=self.exposure_choice, value="Yes")
        self.exposure_choice1_radio.place(x=765, y=530)
        self.exposure_choice2_radio = tk.Radiobutton(self.window, text="No", font=("MS Sans Serif", 11), bg = "white", variable=self.exposure_choice, value="No")
        self.exposure_choice2_radio.place(x=765, y=553)
        self.exposure_choice3_radio = tk.Radiobutton(self.window, text="Uncertain", font=("MS Sans Serif", 11), bg = "white", variable=self.exposure_choice, value="Uncertain")
        self.exposure_choice3_radio.place(x=765, y=576)

        self.data_privacy = BooleanVar()
        self.data_privacy_checkbox = tk.Checkbutton(self.window, text = "I agree to Data Privacy Consent", font=("MS Sans Serif", 11), bg = "white", variable=self.data_privacy, onvalue = True, offvalue = False)
        self.data_privacy_checkbox.place(x=760, y=630)

        # Buttons
        self.submit_Button = tk.Button(self.window, text = "SUBMIT", command = self.submit_data, fg = "white", bg = "#008080", font=("Century Gothic",16,"bold"))
        self.clear_Button = tk.Button(self.window, text = "CLEAR", command = self.clear_info, fg = "white", bg = "#008080", font=("Century Gothic",16,"bold"))
        self.back_Button = tk.Button(self.window, text = "BACK", command = self.go_back_main, fg = "white", bg = "#7E191B", font=("Century Gothic",12,"bold"))
        self.exit_Button = tk.Button(self.window, text = "EXIT", command = self.exit, fg = "white", bg = "#7E191B", font=("Century Gothic",12,"bold"))

        self.submit_Button.place(x = 760, y = 665, width = 155, height = 55)
        self.clear_Button.place(x = 920, y = 665, width = 155, height = 55)
        self.back_Button.place(x = 40, y = 680, width = 155, height = 45)
        self.exit_Button.place(x = 40, y = 740, width = 155, height = 45)

    def go_back_main(self):
        from Main import ContactTracing
        self.window.destroy()
        ContactTracing()

    def exit(self):
        messagebox.askquestion("EXIT PROGRAM", "Are you sure?")
        self.window.destroy()

    def submit_data(self):
        
        # respondent info
        name = self.name_textbox.get()
        age = self.age_spinbox.get()
        birthday = self.birthday_textbox.get()
        email_address = self.email_address_textbox.get()
        contact_number = self.contact_number_textbox.get()
        gender = self.gender_choice.get()
        address = self.address_textbox.get()

        # contact person info
        cp_name = self.cp_name_textbox.get()
        cp_contact_number = self.cp_contact_number_textbox.get()
        cp_email_address = self.cp_email_address_textbox.get()
        relationship_to_cp = self.relationship_to_cp_textbox.get()

        # health declaration
        vaccinated = self.vaccinated_choice.get()
        exposure = self.exposure_choice.get()
        data_privacy = self.data_privacy.get()

        # symptoms dictionary
        symptoms = {
            "cough": self.cough_symptom.get(),
            "colds": self.colds_symptom.get(),
            "sore throat": self.sore_throat_symptom.get(),
            "shortness of breath": self.shortness_of_breath_symptom.get(),
            "fatigue": self.fatigue_symptom.get(),
            "loss of taste": self.loss_of_taste_symptom.get(),
            "loss of smell": self.loss_of_smell_symptom.get(),
            "None": self.None_of_the_above.get()
        }
        symptom = ", ".join(key for key, value in symptoms.items() if value)
        ref_number = random.randint(1000, 9999)
        reference_number = str(ref_number)
  
        if name == '' or age == '' or birthday == '' or email_address == '' or contact_number == '' or gender == '0' or address == '' or cp_name == '' or cp_contact_number == '' or cp_email_address == '' or relationship_to_cp == '' or vaccinated == '0' or exposure == '0':
            messagebox.showerror("Error", "Please fill up all the required fields.")
            return

        elif age == '0':
            messagebox.showerror("Error", "Please enter your age.")
            return

        elif not contact_number.isnumeric() or not cp_contact_number.isnumeric() or not age.isnumeric():
            messagebox.showerror("Error", "Please enter numeric values only.")
            return

        elif symptom == '':
            messagebox.showerror("Error", "Please select atleast one of the symptoms.")
            return

        elif data_privacy == False:
            messagebox.showwarning("Data Privacy Consent", "You must agree to Privacy Notice and Data Privacy Consent.")
            return
            
        else:
            # Create table
            with open('data_list.csv', 'a', newline='') as file:   
                data_input = csv.writer(file)
                data_input.writerow([name, age, birthday,gender, email_address, contact_number, address, cp_name, cp_contact_number, cp_email_address, relationship_to_cp, vaccinated, symptom, exposure, reference_number])

            messagebox.showinfo("Registration Successful", f"Your Data has been registered successfully. Your reference number is {reference_number}")
    
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
        self.nota_checkbox.deselect()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    App = Register()
    App.run()