# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:37:38 2021

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
class Certification:
    db=connect_BD()
    mycursor=db.cursor()
    def __init__ (self,libelle="",organisation="",description="",idsalles=0,examen=0):
        self.libelle=libelle
        self.organisation=organisation
        self.description=description
        self.idsalles=idsalles
        self.examen=examen
    
    def ajouter(self):
        sql = "INSERT INTO certifications ( libelle, organisation, description,idsalles,examen) VALUES ( %s, %s, %s,%s,%s)"
        val = (self.libelle, self.organisation, self.description, self.idsalles, self.examen)
        self.mycursor.execute(sql, val)
        self.db.commit()
    def supprimer(self,num):
        sql = "DELETE FROM certifications WHERE idcertifications = %s"
        val = (num,)
        self.mycursor.execute(sql, val)
        self.db.commit()
    def afficher(self):
        sql = "SELECT idcertifications,libelle, organisation, description,idsalles,examen FROM certifications"
        self.mycursor.execute(sql)
        
        rows = self.mycursor.fetchall()
        
        return rows
    def update(self,libelle, organisation, description,idsalles,examen,roll_no):
        Update = "Update certifications set libelle='%s', organisation='%s', description='%s', idsalles='%s', examen='%s' where idcertifications='%s'"% (libelle, organisation, description,idsalles,examen,roll_no)  
        self.mycursor.execute(Update)  
        self.db.commit() 
        
    def chercher(self,cherche):
        sql = "SELECT idcertifications,libelle, organisation, description,idsalles,examen FROM certifications where libelle like '"+cherche+"%'"  
        self.mycursor.execute(sql)  
        rows = self.mycursor.fetchall()  
        return rows
        
        
        
