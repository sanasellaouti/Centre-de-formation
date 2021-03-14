
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
mycursor.execute("CREATE TABLE IF NOT EXISTS departement(id INT PRIMARY KEY , nom VARCHAR(255) ,chefDepartement VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

class departement:
    db=connection()
    mycursor=db.cursor()
    def __init__(self,i=0,nom='',chefDepartement=''):
        self.id=i
        self.nom=nom
        self.chefDepartement=chefDepartement
       
        
        
    def ajouterDepartement(self):
        sql="INSERT INTO departement (id,nom,chefDepartement) VALUES (%s,%s,%s) "


        val=(self.id,self.nom,self.chefDepartement)
        self.mycursor.execute(sql,val)
        self.db.commit()
        print(self.mycursor.rowcount,"AJOUT FAIS AVEC SUCCES")
    
    def afficherDepartement(self):
        l=[]
        self.mycursor.execute("SELECT * FROM departement")
        for row in self.mycursor:
            print(row)
            l.append(row)
        return (l)
            
    def supprimerDepartement(self,other):
        sql="DELETE FROM departement WHERE id=%s"
        val=(other,)
        self.mycursor.execute(sql,val)
        self.db.commit()
        print(self.mycursor.rowcount,"SUPPRESSION FAIS AVEC SUCCES")



    def modifierDepartement(self,other):
        
        sql="UPDATE departement SET  nom=%s,chefDepartement=%s WHERE id=%s"
        val=(self.nom,self.chefDepartement,other)
        self.mycursor.execute(sql,val)
        self.db.commit()
        print(self.mycursor.rowcount,"  UPDATE FAIS AVEC SUCCES")
        
    def rechercher(self,other):
        sql = "SELECT * FROM departement where chefDepartement like %s or nom like %s or id like %s  "
        other='%'+other+'%'
        val=(other,other,other)
        self.mycursor.execute(sql,val)  
        rows = self.mycursor.fetchall()  
        return rows


    

