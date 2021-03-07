
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="formation",password="19915537")
print(mydb)

mycursor=mydb.cursor()
mycursor.execute("create database if not exists formation")
def connection():
    mydb=mysql.connector.connect(host="localhost",user="formation",password="19915537",database="formation")
    return(mydb)

db=connection()
mycursor=db.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS employe(id INT PRIMARY KEY,cin INT  , nom VARCHAR(255), prenom VARCHAR(255) , telephone INT,mail VARCHAR(255),adresse VARCHAR(255),compteBancaire INT,compteCNSS INT,poste VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

class employe:
    db=connection()
    mycursor=db.cursor()
    def __init__(self,i=0,cin=0,nom='',prenom='',telephone=0,mail='',adresse='',poste='',compteBancaire=0,compteCNSS=0):
        self.id=i
        self.cin=cin
        self.nom=nom
        self.prenom=prenom
        self.telephone=telephone
        self.mail=mail
        self.adresse=adresse
        self.poste=poste
        self.compteBancaire=compteBancaire
        self.compteCNSS=compteCNSS
        
        
        
    def ajouterEmploye(self):
        sql="INSERT INTO employe (id,cin,nom,prenom,telephone,mail,adresse,poste,compteBancaire,compteCNSS) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "


        val=(self.id, self.cin,self.nom,self.prenom,self.telephone,self.mail,self.adresse,self.poste,self.compteBancaire,self.compteCNSS)
        self.mycursor.execute(sql,val)
        self.db.commit()
        print(self.mycursor.rowcount,"AJOUT FAIS AVEC SUCCES")
    
    def afficherEmploye(self):
        l=[]
        self.mycursor.execute("SELECT * FROM employe")
        for row in self.mycursor:
            print(row)
            l.append(row)  
        return(l)
            
    def supprimerEmploye(self,other):
        sql="DELETE FROM employe WHERE id=%s"
        val=(other,)
        self.mycursor.execute(sql,val)
        self.db.commit()
        print(self.mycursor.rowcount,"suppression FAIS AVEC SUCCES")



    def modifierEmploye(self,other):
        
        
        
        sql="UPDATE employe SET  cin =%s,nom =%s, prenom =%s,telephone=%s,mail=%s,adresse=%s,poste=%s,compteBancaire=%s,compteCNSS=%s WHERE id=%s"
        val=(self.cin,self.nom,self.prenom,self.telephone,self.mail,self.adresse,self.poste,self.compteBancaire,self.compteCNSS,other)
        self.mycursor.execute(sql,val)
        self.db.commit()
        print(self.mycursor.rowcount,"UPDATE FAIS AVEC SUCCES")
        
a=employe()
a.supprimerEmploye(7)


