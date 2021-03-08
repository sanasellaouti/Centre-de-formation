
from Certification import Certification 
from Formateur import Formateur
from PIL import Image, ImageTk
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
        self.title("Gestion Des Certifications")  
        """ photo = PhotoImage(file="ma_photo.png")
        canvas = Canvas(fenetre,width=350, height=200)
        canvas.create_image(0, 0, anchor=NW, image=photo)
        canvas.pack()"""
        self.geometry("800x650+351+174")  
        self.lblTitle = tk.Label(self, text="Gestion Des Certifications", font=("Helvetica", 16), bg="yellow", fg="green")  
        self.lblLibelle = tk.Label(self, text="Entrer Libelle:", font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.lblOrganisation = tk.Label(self, text="Entrer Organisation:", font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.lblDescription = tk.Label(self, text="Entrer Description:", font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.lblSalle = tk.Label(self, text="Entrer la salle:", font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.lblExamen = tk.Label(self, text="Entrer Date d'Examen:", font=("Helvetica", 10), bg="blue", fg="yellow")
        self.lblSelect = tk.Label(self, text="Please select one record below to update or delete", font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.lblSearch = tk.Label(self, text="SVP,Entrer le libelle à chercher:",font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.entLibelle = tk.Entry(self)  
        self.entOrganisation = tk.Entry(self)  
        self.entDescription = tk.Entry(self)  
        self.entSalle = tk.Entry(self)  
          
        self.entExamen = DateEntry(self, width=12, background='darkblue',  
        foreground='white', borderwidth=2, year=2021,locale='en_US', date_pattern='y-mm-dd')  
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
        self.tvStudent.heading('#2', text='Libelle', anchor='center')  
        self.tvStudent.column('#2', width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#3', text='Organisation', anchor='center')  
        self.tvStudent.column('#3',width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#4', text='Description', anchor='center')  
        self.tvStudent.column('#4',width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#5', text='Salle', anchor='center')  
        self.tvStudent.column('#5',width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#6', text='Date Examen', anchor='center')  
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
        self.lblLibelle.place(x=100, y=70, height=23, width=150)  
        self.lblOrganisation.place(x=100, y=100, height=23, width=150)  
        self.lblDescription.place(x=100, y=129, height=23, width=150)  
        self.lblSalle.place(x=100, y=158, height=23, width=150)  
        self.lblExamen.place(x=100, y=217, height=23, width=150) 
        self.lblSelect.place(x=150, y=280, height=23, width=400)  
        self.lblSearch.place(x=20, y=560, height=23, width=250)  
        self.entLibelle.place(x=277, y=72, height=21, width=186)  
        self.entOrganisation.place(x=277, y=100, height=21, width=186)  
        self.entDescription.place(x=277, y=129, height=21, width=186)  
        self.entSalle.place(x=277, y=158, height=21, width=186)  
        self.entExamen.place(x=278, y=218, height=21, width=186) 
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
        self.entLibelle.delete(0, tk.END)  
        self.entOrganisation.delete(0, tk.END)  
        self.entDescription.delete(0, tk.END)  
        self.entSalle.delete(0, tk.END)  
        self.entExamen.delete(0, tk.END)  
    def exit(self):  
       MsgBox = mb.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')  
       if MsgBox == 'yes':  
            self.destroy() 
    def supprimer_formateur(self):  
        MsgBox = mb.askquestion('Delete Record', 'Etes vous sûr de vouloir supprimer la certification selectionnée', icon='warning')  
        if MsgBox == 'yes':  
            c=Certification()
            c.supprimer(roll_no)
            mb.showinfo("Information", " Record Deleted Succssfully")  
            self.afficher_formateur()  
            self.entLibelle.delete(0, tk.END)  
            self.entOrganisation.delete(0, tk.END)  
            self.entDescription.delete(0, tk.END)  
            self.entSalle.delete(0, tk.END)  
            self.entExamen.delete(0, tk.END)  
           

    def ajouter_formateur(self):  
        
        Libelle = self.entLibelle.get() # Retrieving entered first name  
        Organisation = self.entOrganisation.get() # Retrieving entered last name  
        Description = self.entDescription.get() # Retrieving entered contact number  
        Salle = self.entSalle.get() # Retrieving entered city name  
        Examen = self.entExamen.get() # Retrieving entered state name  
              
        # validating Entry Widgets  
        if Libelle == "":  
            mb.showinfo('Information', "SVP Entrer libelle")  
            self.entLibelle.focus_set()  
            return  
        if Organisation == "":  
            mb.showinfo('Information', "SVP Entrer organisation")  
            self.entOrganisation.focus_set()  
            return  
        if Description == "":  
            mb.showinfo('Information', "SVP Entrer Description")  
            self.entDescription.focus_set()  
            return  
        if Salle == "":  
            mb.showinfo('Information', "SVP Entrer la salle")  
            self.entSalle.focus_set()  
            return  
        if Examen == "":  
            mb.showinfo('Information', "SVP Entrer date examen")  
            self.entExamen.focus_set()  
            return  
        c=Certification(Libelle, Organisation,Description,Salle,Examen)
        c.ajouter()
      
 
    def show_search_record(self):  
         
        libelle= self.entSearch.get() # Retrieving entered first name  
             
        if libelle == "":  
            mb.showinfo('Information', "SVP, entrer le libelle de certification:")  
            self.entSearch.focus_set()  
            return  
        self.tvStudent.delete(*self.tvStudent.get_children()) # clears the treeview tvStudent  
 
        f=Certification()
        rows=f.chercher(libelle)
        RollNo = ""  
        Libelle = ""  
        Organisation = ""  
        Description= ""  
        Salle = ""  
        Examen = ""   
          
        for row in rows:  
            RollNo = row[0]  
            Libelle = row[1]  
            Organisation = row[2]  
            Description = row[3]  
            Salle = row[4]  
            Examen = row[5]   
             
            self.tvStudent.insert("", 'end', text=RollNo, values=(RollNo,Libelle,Organisation, Description,Salle,Examen))  
   
    def show_selected_record(self, event):  
        self.clear_form()  
        for selection in self.tvStudent.selection():  
                item = self.tvStudent.item(selection)  
        global roll_no  
        roll_no,first_name,last_name,city,email,contact_no = item["values"][0:6]  
        self.entLibelle.insert(0, first_name)  
        self.entOrganisation.insert(0, last_name)  
        self.entDescription.insert(0, city)  
        self.entSalle .insert(0, email)  
        self.entExamen.insert(0, contact_no)  
        
        return roll_no 
    def update_formateur(self):  
         
            print("Updating")  
            
            Libelle = self.entLibelle.get()  
            Organisation = self.entOrganisation.get()  
            Description = self.entDescription.get()  
            Salle = self.entSalle.get()  
            Examen = self.entExamen.get()  
              
            print( roll_no) 
            f=Certification()
            f.update(Libelle, Organisation, Description,Salle,Examen,roll_no)
            mb.showinfo("Info", "La certification selectionnée est mise à jour ")  
            self.afficher_formateur() 
    
    def afficher_formateur(self):  
                      
            self.tvStudent.delete(*self.tvStudent.get_children()) # clears the treeview tvStudent  
            f=Certification()
            rows = f.afficher()  
            RollNo = ""  
            Libelle = ""  
            Organisation = ""  
            Description= ""  
            Salle = ""  
            Examen = ""  
            
            for row in rows:  
                RollNo = row[0]  
                Libelle = row[1]  
                Organisation = row[2]  
                Description = row[3]  
                Salle = row[4]  
                Examen = row[5]  
                self.tvStudent.insert("", 'end', text=RollNo, values=(RollNo, Libelle,Organisation, Description,Salle,Examen))  

if __name__ == "__main__":  
    app = FormateurApp()  
    app.mainloop()   