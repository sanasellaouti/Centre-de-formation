# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 15:22:48 2021

@author: Maissa bessifi
"""
from formateurGUI import *
from certificationGUI import *
from tkinter import *
import mysql.connector

db_connection = mysql.connector.connect(  
host="localhost",  
user="maissa",  
password="maissa2021")  
# creating database_cursor to perform SQL operation  
db_cursor = db_connection.cursor(buffered=True) # "buffered=True".makes db_cursor.row_count return actual number of records selected otherwise would return -1 
class PrincipalApp(tk.Tk):
    def __init__(self): 
        super().__init__() 
        self.title("Gestion...")
        self.geometry("400x300")
        #bouton gestion formateur
        self.btn_formateur = tk.Button(self, text="Gestion Formateurs", font=("Helvetica", 11), bg="yellow", fg="blue",  
        command=self.gestion_formateur)
        #bouton getion certification
        self.btn_certification = tk.Button(self, text="Gestion certifications", font=("Helvetica", 11), bg="yellow", fg="blue",  
        command=self.gestion_certification)
        self.btn_formateur.place(x=100, y=100, height=25, width=200)
        self.btn_certification.place(x=100, y=150, height=25, width=200)
        self.create_table()
    def create_table(self):  
        if db_connection.is_connected() == False:  
            db_connection.connect()  
            # executing cursor with execute method and pass SQL query  
            db_cursor.execute("CREATE DATABASE IF NOT EXISTS formationsdb") # Create a Database Named formationsdb  
            db_cursor.execute("use formationsdb") # Interact with Student Database  
            # creating required tables  
            db_cursor.execute("create table if not exists formateurs(idformateurs INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,tel INT(15),nom VARCHAR(45),prenom VARCHAR(45),email VARCHAR(20),city VARCHAR(30)")  
            db_connection.commit()
            db_cursor.execute("create table if not exists certifications(idcertifications INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,idsalles INT(15),libelle VARCHAR(45),description LONTEXT,organisation VARCHAR(20),examen DATE")
            db_connection.commit()
    def gestion_formateur(self):
        app = FormateurApp()  
        app.mainloop()
    def gestion_certification(self):
        app = CertificationApp()  
        app.mainloop()
if __name__ == "__main__":  
    app = PrincipalApp()  
    app.mainloop() 
