# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 16:50:31 2021

@author: Maissa bessifi
"""
import mysql.connector
def connect_BD():
    mydb = mysql.connector.connect(
        host="localhost",
        user="maissa",
        password="maissa2021",
        database="formationsdb"
        )
    return mydb
class Formateur:
    db=connect_BD()
    mycursor=db.cursor()
    def __init__(self,nom="",prenom="",city="",email="",tel=0):
        self.nom=nom
        self.prenom=prenom
        self.city=city
        self.email=email
        self.tel=tel
    def ajouter(self):
        sql = "INSERT INTO formateurs ( nom, prenom, email,city,tel) VALUES ( %s, %s, %s,%s,%s)"
        val = (self.nom, self.prenom, self.email, self.city, self.tel)
        self.mycursor.execute(sql, val)
        self.db.commit()
    def supprimer(self,num):
        sql = "DELETE FROM formateurs WHERE idformateurs = %s"
        val = (num,)
        self.mycursor.execute(sql, val)
        self.db.commit()
    def afficher(self):
        sql = "SELECT idformateurs,nom, prenom, email, city, tel FROM formateurs"
        self.mycursor.execute(sql)
        
        rows = self.mycursor.fetchall()
        
        return rows
    def update(self,nom,prenom,email,city,tel,roll_no):
        Update = "Update formateurs set nom='%s', prenom='%s', tel='%s', city='%s', email='%s' where idformateurs='%s'" % (  
        nom, prenom, tel, city, email,roll_no)  
        self.mycursor.execute(Update)  
        self.db.commit() 

        
    def chercher(self,cherche):
        sql = "SELECT idformateurs,nom, prenom, email, city, tel FROM formateurs where prenom like'"+cherche+"%'"  
        self.mycursor.execute(sql)  
        rows = self.mycursor.fetchall()  
        return rows
       
    
    