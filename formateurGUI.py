# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 14:59:34 2021

@author: Meriem
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 14:35:33 2021

@author: Meriem
"""
from Formateur import Formateur 
from tkcalendar import Calendar, DateEntry  
import tkinter as tk  
import tkinter.messagebox as mb  
import tkinter.ttk as ttk  
## Connecting to the database  
## importing 'mysql.connector' for connection to mysql database  
import mysql.connector  
## connecting to the database using 'connect()' method  
## it takes 3 required parameters 'host', 'user', 'password'  
#Please change user and password values to your  
#user and password values to connect to MySQL Database server   
"""db_connection = mysql.connector.connect(  
host="localhost",  
user="maissa",  
password="maissa2021")  
# creating database_cursor to perform SQL operation  
db_cursor = db_connection.cursor(buffered=True) # "buffered=True".makes db_cursor.row_count return actual number of records selected otherwise would return -1  
"""
class FormateurApp(tk.Tk):  
    def __init__(self):  
        super().__init__()  
        self.title("Gestion Des Formateurs")  
        self.geometry("800x650+351+174")  
        self.lblTitle = tk.Label(self, text="Gestion Des Formateurs", font=("Helvetica", 16), bg="yellow", fg="green")  
        self.lblFName = tk.Label(self, text="Entrer Nom:", font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.lblLName = tk.Label(self, text="Entrer Prenom:", font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.lblContactNo = tk.Label(self, text="Entrer Tel No:", font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.lblCity = tk.Label(self, text="Entrer City:", font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.lblEmail = tk.Label(self, text="Entrer Email:", font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.lblSelect = tk.Label(self, text="Please select one record below to update or delete", font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.lblSearch = tk.Label(self, text="SVP,Entrer le prenom à chercher:",font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.entFName = tk.Entry(self)  
        self.entLName = tk.Entry(self)  
        self.entContact = tk.Entry(self)  
        self.entCity = tk.Entry(self)  
        self.entEmail = tk.Entry(self)  
         
        #self.entDOB = tk.Entry(self)  
        self.entSearch = tk.Entry(self)  
        self.btn_register = tk.Button(self, text="Register", font=("Helvetica", 11), bg="yellow", fg="blue",  
        command=self.ajouter_formateur)  
        self.btn_update = tk.Button(self,text="Update",font=("Helvetica",11),bg="yellow", fg="blue",
        command=self.update_formateur)  
        self.btn_delete = tk.Button(self, text="Delete", font=("Helvetica", 11), bg="yellow", fg="blue",  
        command=self.supprimer_formateur)  
        self.btn_clear = tk.Button(self, text="Clear", font=("Helvetica", 11), bg="yellow", fg="blue",  
        command=self.clear_form)  
        self.btn_show_all = tk.Button(self, text="Show All", font=("Helvetica", 11), bg="yellow", fg="blue",  
        command=self.afficher_formateur)  
        self.btn_search = tk.Button(self, text="Search", font=("Helvetica", 11), bg="yellow", fg="blue",  
        command=self.show_search_record)  
        self.btn_exit = tk.Button(self, text="Exit", font=("Helvetica", 16), bg="yellow", fg="blue",command=self.exit)  
        columns = ("#1", "#2", "#3", "#4", "#5", "#6")  
        self.tvStudent= ttk.Treeview(self,show="headings",height="5", columns=columns)  
        self.tvStudent.heading('#1', text='RollNo', anchor='center')  
        self.tvStudent.column('#1', width=60, anchor='center', stretch=False)  
        self.tvStudent.heading('#2', text='Nom', anchor='center')  
        self.tvStudent.column('#2', width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#3', text='Prenom', anchor='center')  
        self.tvStudent.column('#3',width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#4', text='City', anchor='center')  
        self.tvStudent.column('#4',width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#5', text='Email', anchor='center')  
        self.tvStudent.column('#5',width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#6', text='Tel', anchor='center')  
        self.tvStudent.column('#6', width=10, anchor='center', stretch=True)  
        #Scroll bars are set up below considering placement position(x&y) ,height and width of treeview widget  
        vsb= ttk.Scrollbar(self, orient=tk.VERTICAL,command=self.tvStudent.yview)  
        vsb.place(x=40 + 640 + 1, y=310, height=180 + 20)  
        self.tvStudent.configure(yscroll=vsb.set)  
        hsb = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.tvStudent.xview)  
        hsb.place(x=40 , y=310+200+1, width=620 + 20)  
        self.tvStudent.configure(xscroll=hsb.set)  
        self.tvStudent.bind("<<TreeviewSelect>>", self.show_selected_record)  
        self.lblTitle.place(x=280, y=30, height=27, width=400)  
        self.lblFName.place(x=100, y=70, height=23, width=150)  
        self.lblLName.place(x=100, y=100, height=23, width=150)  
        self.lblContactNo.place(x=100, y=129, height=23, width=150)  
        self.lblCity.place(x=100, y=158, height=23, width=150)  
        self.lblEmail.place(x=100, y=187, height=23, width=150)  
        self.lblSelect.place(x=150, y=280, height=23, width=400)  
        self.lblSearch.place(x=20, y=560, height=23, width=250)  
        self.entFName.place(x=277, y=72, height=21, width=186)  
        self.entLName.place(x=277, y=100, height=21, width=186)  
        self.entContact.place(x=277, y=129, height=21, width=186)  
        self.entCity.place(x=277, y=158, height=21, width=186)  
        self.entEmail.place(x=278, y=188, height=21, width=186)  
        self.entSearch.place(x=310, y=560, height=21, width=186)  
        self.btn_register.place(x=290, y=245, height=25, width=76)  
        self.btn_update.place(x=370, y=245, height=25, width=76)  
        self.btn_delete.place(x=460, y=245, height=25, width=76)  
        self.btn_clear.place(x=548, y=245, height=25, width=76)  
        self.btn_show_all.place(x=630, y=245, height=25, width=76)  
        self.btn_search.place(x=498, y=558, height=26, width=60)  
        self.btn_exit.place(x=320, y=610, height=31, width=60)  
        self.tvStudent.place(x=40, y=310, height=200, width=640)  
       # self.create_table()  
        self.afficher_formateur()  
    def clear_form(self):  
        self.entFName.delete(0, tk.END)  
        self.entLName.delete(0, tk.END)  
        self.entContact.delete(0, tk.END)  
        self.entCity.delete(0, tk.END)  
        self.entEmail.delete(0, tk.END)  
    def exit(self):  
       MsgBox = mb.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')  
       if MsgBox == 'yes':  
            self.destroy() 
    def supprimer_formateur(self):  
        MsgBox = mb.askquestion('Delete Record', 'Etes vous sûr de vouloir supprimer le formateur selectionné', icon='warning')  
        if MsgBox == 'yes':  
            f=Formateur()
            f.supprimer(roll_no)
            mb.showinfo("Information", "Student Record Deleted Succssfully")  
            self.afficher_formateur()  
            self.entFName.delete(0, tk.END)  
            self.entLName.delete(0, tk.END)  
            self.entContact .delete(0, tk.END)  
            self.entCity.delete(0, tk.END)  
            self.entEmail.delete(0, tk.END)  
           

    def ajouter_formateur(self):  
        
        fname = self.entFName.get() # Retrieving entered first name  
        lname = self.entLName.get() # Retrieving entered last name  
        contact_no = self.entContact.get() # Retrieving entered contact number  
        city = self.entCity.get() # Retrieving entered city name  
        email = self.entEmail.get() # Retrieving entered state name  
              
        # validating Entry Widgets  
        if fname == "":  
            mb.showinfo('Information', "SVP Entrer nom")  
            self.entFName.focus_set()  
            return  
        if lname == "":  
            mb.showinfo('Information', "SVP Entrer prenom")  
            self.entLName.focus_set()  
            return  
        if contact_no == "":  
            mb.showinfo('Information', "SVP Entrer Tel NO")  
            self.entContact.focus_set()  
            return  
        if city == "":  
            mb.showinfo('Information', "SVP Entrer City")  
            self.entCity.focus_set()  
            return  
        if email == "":  
            mb.showinfo('Information', "SVP Entrer Email")  
            self.entEmail.focus_set()  
            return  
        f=Formateur(fname,lname,city,email,contact_no)
        f.ajouter()
      
 
    def show_search_record(self):  
         
        prenom= self.entSearch.get() # Retrieving entered first name  
             
        if prenom == "":  
            mb.showinfo('Information', "SVP, entrer le prenom du formateur")  
            self.entSearch.focus_set()  
            return  
        self.tvStudent.delete(*self.tvStudent.get_children()) # clears the treeview tvStudent  
 
        f=Formateur()
        rows=f.chercher(prenom)
        RollNo = ""  
        First_Name = ""  
        Last_Name = ""  
        City = ""  
        Email = ""  
        Phone_Number = ""  
          
        for row in rows:  
            RollNo = row[0]  
            First_Name = row[1]  
            Last_Name = row[2]  
            City = row[3]  
            Email = row[4]  
            Phone_Number = row[5]  
            print( Phone_Number)  
            self.tvStudent.insert("", 'end', text=RollNo, values=(RollNo, First_Name, Last_Name, City, Email, Phone_Number))  
   
    def show_selected_record(self, event):  
        self.clear_form()  
        for selection in self.tvStudent.selection():  
                item = self.tvStudent.item(selection)  
        global roll_no  
        roll_no,first_name,last_name,city,email,contact_no = item["values"][0:6]  
        self.entFName.insert(0, first_name)  
        self.entLName.insert(0, last_name)  
        self.entCity.insert(0, city)  
        self.entEmail .insert(0, email)  
        self.entContact.insert(0, contact_no)  
        
        return roll_no 
    def update_formateur(self):  
         
            print("Updating")  
            
            First_Name = self.entFName.get()  
            Last_Name = self.entLName.get()  
            Phone_Number = self.entContact.get()  
            City = self.entCity.get()  
            Email = self.entEmail.get()  
              
            print( roll_no) 
            f=Formateur()
            f.update(First_Name,Last_Name,Email,City,Phone_Number,roll_no)
            mb.showinfo("Info", "Le formateur selectionné est mis à jour ")  
            self.afficher_formateur() 
    
    def afficher_formateur(self):  
                      
            self.tvStudent.delete(*self.tvStudent.get_children()) # clears the treeview tvStudent  
            f=Formateur()
            rows = f.afficher()  
            RollNo = ""  
            First_Name = ""  
            Last_Name = ""  
            City = ""  
            Email = ""  
            Phone_Number = ""  
            
            for row in rows:  
                RollNo = row[0]  
                First_Name = row[1]  
                Last_Name = row[2]  
                Email = row[3]  
                City = row[4]  
                Tel = row[5]  
                self.tvStudent.insert("", 'end', text=RollNo, values=(RollNo, First_Name, Last_Name, City, Email, Tel))  

if __name__ == "__main__":  
    app = FormateurApp()  
    app.mainloop()   