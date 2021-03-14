# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 15:22:48 2021

@author: Maissa bessifi
"""
from formateurGUI import *
from certificationGUI import *
from tkinter import *
class PrincipalApp(tk.Tk):
    def __init__(self): 
        super().__init__() 
        self.title("Gestion...")
        self.geometry("400x300")
        #bouton gestion formateur
        self.btn_formateur = tk.Button(self, text="Gestion Formateurs", font=("Helvetica", 11), bg="yellow", fg="blue",  
        command=self.gestion_formateur)
        #bouton getion vertification
        self.btn_certification = tk.Button(self, text="Gestion certifications", font=("Helvetica", 11), bg="yellow", fg="blue",  
        command=self.gestion_certification)
        self.btn_formateur.place(x=100, y=100, height=25, width=200)
        self.btn_certification.place(x=100, y=150, height=25, width=200)
    
    def gestion_formateur(self):
        app = FormateurApp()  
        app.mainloop()
    def gestion_certification(self):
        app = CertificationApp()  
        app.mainloop()
if __name__ == "__main__":  
    app = PrincipalApp()  
    app.mainloop() 
