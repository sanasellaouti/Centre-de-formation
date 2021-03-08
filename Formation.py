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
mycursor.execute("CREATE TABLE IF NOT EXISTS Formation(id_formation INT PRIMARY KEY, libellé VARCHAR(255) , responsable VARCHAR(255), durée int)")
mycursor.execute("SHOW TABLES")

class Formation:
    db=connection()
    mycursor=db.cursor()
    def __init__(self,id_formation=0,libellé="",responsable="",durée=0):
        self.id_formation=id_formation
        self.libellé=libellé
        self.responsable=responsable
        self.durée=durée
        
    def ajouterFormation(self):
       sql="INSERT INTO Formation (id_formation,libellé,responsable,durée) VALUES (%s, %s, %s, %s)"
       val = (self.id_formation, self.libellé, self.responsable, self.durée)
       self.mycursor.execute(sql, val)
       self.db.commit()
       print(self.mycursor.rowcount, "record inserted.")
       
    def afficherFormations(self):
        self.mycursor.execute("SELECT * FROM Formation")
        result = self.mycursor.fetchall()
        return result
        
    def supprimerFormation(self,id_formation):
        sql = "DELETE FROM Formation WHERE id_formation = %s"
        val = (id_formation,)
        self.mycursor.execute(sql, val)
        self.db.commit()
        
    def modifierFormation(self,other):
        
        self.libellé=input('libellé')
        self.responsable=input('responsable')
        self.durée=int(input('durée'))
        
        sql="UPDATE Formation SET  libellé =%s, responsable =%s, durée=%s WHERE id_formation=%s"
        val=(self.libellé,self.responsable,self.durée,other)
        self.mycursor.execute(sql,val)
        self.db.commit()
        print(self.mycursor.rowcount,"updtate FAIS AVEC SUCCES")
        

#f=Formation(123,"BI","Ameni Amri",6)
#f.ajouterFormation()
#f.afficherFormations()
#print("avant suppression.....")
#f.afficherFormations()
#f.supprimerFormation(11)
#print("après suppression.....")
#f.afficherFormations()
#f.modifierFormation(8)
#f.afficherFormations()
        
