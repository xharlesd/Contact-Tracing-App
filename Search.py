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
        self.search_label = tk.Label(self.window, text = "Reference No.", fg = "#494F55", bg = "white", font=("Helvetica",16,"bold"))
        self.search_label.place(x = 435, y = 175, width = 170, height = 20)
        self.search_textbox = tk.Entry(self.window, font=("MS Sans Serif",12), fg = "black", bg = "#F5F5F5")
        self.search_textbox.place(x = 597 , y = 168, width = 235, height = 30)
        
        # define search function
        self.search_Button = tk.Button(self.window, text = "SEARCH", command=self.search_data, fg = "white", bg = "#008080", font=("Century Gothic",12,"bold"))
        self.search_Button.place(x = 843, y = 165, width = 71, height = 35)
    
    def search_data(self):
        reference_number = self.search_textbox.get()
        data_list = []
        with open("data_list.csv", "r") as file:
            data_read = csv.reader(file)
            for row in data_read:
                data_list.append(row)

        data_found = None
        for data in data_list:
            if reference_number in data:
                messagebox.showinfo("Ref No.", "Reference number found.")
                data_found = data
                break
            
            
        if data_found:""""""

    def run(self):
        self.window.mainloop()
        
if __name__ == "__main__":
    App = Search()
    App.run()