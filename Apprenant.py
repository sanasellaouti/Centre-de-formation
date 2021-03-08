import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="sana",password="sana2021")
print(mydb)

mycursor=mydb.cursor()
mycursor.execute("create database if not exists sana")

def connection():
    mydb=mysql.connector.connect(host="localhost",user="sana",password="sana2021",database="sanaBD")
    return(mydb)
db=connection()
mycursor=db.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Apprenant(id_apprenant INT PRIMARY KEY, CIN int, nom_prénom VARCHAR(255), filière VARCHAR(255), téléphone int, email VARCHAR(255))")
mycursor.execute("SHOW TABLES")

class Apprenant:
    db=connection()
    mycursor=db.cursor()
    def __init__(self,id_apprenant=0,CIN=0,nom_prénom="",filière="",téléphone=0,email=""):
        self.id_apprenant=id_apprenant
        self.CIN=CIN
        self.nom_prénom=nom_prénom
        self.filière=filière
        self.téléphone=téléphone
        self.email=email
        
    def ajouterApprenant(self):
       sql="INSERT INTO Apprenant (id_apprenant,CIN,nom_prénom,filière,téléphone,email) VALUES (%s, %s, %s, %s, %s, %s)"
       val = (self.id_apprenant,self.CIN,self.nom_prénom, self.filière, self.téléphone, self.email)
       self.mycursor.execute(sql, val)
       self.db.commit()
       print(self.mycursor.rowcount, "record inserted.")
       
    def afficherApprenants(self):
        self.mycursor.execute("SELECT * FROM Apprenant")
        result = self.mycursor.fetchall()
        return result
            
    def supprimerApprenant(self,id_apprenant):
        sql = "DELETE FROM Apprenant WHERE id_apprenant = %s"
        val = (id_apprenant,)
        self.mycursor.execute(sql, val)
        self.db.commit()
        
    def modifierApprenant(self,other):
        sql="UPDATE Apprenant SET  CIN =%s, nom_prénom =%s, filière=%s, téléphone=%s,email=%s WHERE id_apprenant=%s"
        val=(self.CIN,self.nom_prénom,self.filière,self.téléphone,self.email,other)
        self.mycursor.execute(sql,val)
        self.db.commit()
        print(self.mycursor.rowcount,"Apprenant bien modifié")



#a = Apprenant(22422,21345,"Ali Ahmed","BI",2211234,"ahmed@gmail.com")
#a.ajouterApprenant()
#a.afficherApprenants()
#print("avant suppression.....")
#a.afficherApprenants()
#a.supprimerApprenant(2)
#print("après suppression.....")
#a.afficherApprenants()
#a.modifierApprenant(242)
#a.afficherApprenants()
