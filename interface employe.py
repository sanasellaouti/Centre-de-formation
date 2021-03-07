from tkinter import *
from employe import employe
import tkinter.ttk as ttk

class gestionEmploye():
    def __init__(self,root):
        self.root = root
        self.root.geometry('800x600')
        self.root.title("Gestion employé")
        self.id=StringVar()
        self.cin=StringVar()
        self.nom=StringVar()
        self.prenom=StringVar()
        self.telephone=StringVar()
        self.mail=StringVar()
        self.adresse=StringVar()
        self.poste=StringVar()
        self.compteBancaire=StringVar()
        self.compteCNSS=StringVar()
  
        
  
        
    #Formulaire ajout Departement dans __init():
        #==============Num employe TEXTFIELD AND LABEL
        x = Label(self.root,text = "Id Unique",anchor='w')
        x.grid(row = 1,column = 0,padx = 40,pady = 40)
        y= Entry(self.root,textvariable = self.id)
        y.grid(row = 1,column = 1,ipady = 7,ipadx = 20,padx = 20)
    
        #==============Nom departement TEXTFIELD AND LABEL
        x = Label(self.root,text = "CIN",anchor='w')
        x.grid(row = 1,column = 2,padx = 40,pady = 40)
        y= Entry(self.root,textvariable = self.cin)
        y.grid(row = 1,column = 3,ipady = 7,ipadx = 20,padx = 20)
        
        #=======================chef departement LABEL AND TEXTFIELD
        x= Label(self.root,text="Nom",anchor='w')
        x.grid(row = 2,column = 0,pady = 40)
        y = Entry(self.root,textvariable = self.nom)
        y.grid(row = 2,column = 1,ipady = 7,ipadx = 20,padx = 20)
         #=======================chef departement LABEL AND TEXTFIELD
        x= Label(self.root,text="Prenom",anchor='w')
        x.grid(row = 2,column = 2,pady = 40)
        y = Entry(self.root,textvariable = self.prenom)
        y.grid(row = 2,column = 3,ipady = 7,ipadx = 20,padx = 20)
         #=======================chef departement LABEL AND TEXTFIELD
        x= Label(self.root,text="Téléphone",anchor='w')
        x.grid(row = 3,column = 0,pady = 40)
        y = Entry(self.root,textvariable = self.telephone)
        y.grid(row = 3,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================chef departement LABEL AND TEXTFIELD
        x= Label(self.root,text="Mail",anchor='w')
        x.grid(row = 3,column = 2,pady = 40)
        y = Entry(self.root,textvariable = self.mail)
        y.grid(row = 3,column = 3,ipady = 7,ipadx = 20,padx = 20)
        #=======================chef departement LABEL AND TEXTFIELD
        x= Label(self.root,text="adresse",anchor='w')
        x.grid(row = 4,column = 0,pady = 40)
        y = Entry(self.root,textvariable = self.adresse)
        y.grid(row = 4,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================chef departement LABEL AND TEXTFIELD
        x= Label(self.root,text="Compte bancaire",anchor='w')
        x.grid(row = 4,column = 2,pady = 40)
        y = Entry(self.root,textvariable = self.compteBancaire)
        y.grid(row = 4,column = 3,ipady = 7,ipadx = 20,padx = 20)
        #=======================chef departement LABEL AND TEXTFIELD
        x= Label(self.root,text="Compte CNSS",anchor='w')
        x.grid(row = 5,column = 0,pady = 40)
        y = Entry(self.root,textvariable = self.compteCNSS)
        y.grid(row = 5,column = 1,ipady = 7,ipadx = 20,padx = 20)

        
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        x= Button(self.root,text = "Supprimer",command = self.remove,anchor='c')
        x.grid(row = 6,column = 1,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton affichage à ajouter après boutton "Ajouter" dans __init()__
        x= Button(self.root,text = "Afficher",command = self.view,anchor='c')
        x.grid(row = 6,column = 2,ipady = 4,ipadx = 13,pady = 40)
 
        
        #=====================Boutton ajout
        x = Button(self.root,text = "Ajouter",command = self.add,anchor='c')
        x.grid(row = 6,column = 0,ipady = 4,ipadx = 13,pady = 40)

        #=====================Boutton modifier
        x = Button(self.root,text = "Modifier",command = self.modifier,anchor='c')
        x.grid(row = 6,column = 3,ipady = 4,ipadx = 13,pady = 40)


        
        #Fonction d'ajout d'un étudiant (sera appelée dérière le boutton "Ajouter"
    def add(self):
        E = employe(self.id.get(),self.cin.get(),self.nom.get(),self.prenom.get(),self.telephone.get(),self.mail.get(),self.adresse.get(),self.poste.get(),self.compteBancaire.get(),self.compteCNSS.get())
        print("Employe: ",E.nom)
        E.ajouterEmploye()

        #Fonction dse suppression d'un étudiant sera appelée dans le boutton "Supprimer"  
    def remove(self):
        E = employe()
        E.supprimerEmploye(self.id.get())
    def modifier(self):
        E = employe(self.id.get(),self.cin.get(),self.nom.get(),self.prenom.get(),self.telephone.get(),self.mail.get(),self.adresse.get(),self.poste.get(),self.compteBancaire.get(),self.compteCNSS.get())
        E.modifierEmploye(self.id.get())
    def view(self):
        #self.root.title("Student Management(Details)")
        #==========================Show Frame
        self.root=Tk()
        self.root.geometry('800x400')
        self.root.title("Affichage des employés")
        show_frame = Frame(self.root)
        show_frame.place(width = 1000,x = 0,y = 0 ,height = 300)
        labl_show = Label(show_frame,text = "Affichage des employés")
        labl_show.pack()
        
        #========================Main Frame
        x= Frame(self.root,bd = 10,relief = SUNKEN)
        x.place(width = 800,height = 300,x = 8,y = 58)
        tree = ttk.Treeview(x,height = 200)
        vsb = ttk.Scrollbar(x,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = RIGHT,fill = Y)
        tree.pack(side = TOP,fill = X)
        tree['columns'] = ("1","2","3","4","5","6","7","8","9","10")
        tree.column('#0',width=20)
        tree.column('1',width=20)
        tree.column('2',width=60)
        tree.column('3',width=60)
        tree.column('4',width=60)
        tree.column('5',width=50)
        tree.column('6',width=80)
        tree.column('7',width=80)
        tree.column('8',width=80)
        tree.column('9',width=80)
        tree.column('10',width=80)
        tree.heading("#0",text = "num",anchor='c')
        tree.heading("1",text = "Id",anchor='c')
        tree.heading("2",text = "CIN",anchor='c')
        tree.heading("3",text = "Nom",anchor='w')
        tree.heading("4",text = "Prenom",anchor='w')
        tree.heading("5",text="telephone",anchor='w')
        tree.heading("6",text = "mail",anchor='c')
        tree.heading("7",text = "adresse",anchor='c')
        tree.heading("8",text = "Compte bancaire",anchor='w')
        tree.heading("9",text="compte CNSS",anchor='w')
        tree.heading("10",text = "poste",anchor='w')
        
        E=employe()
        rows=E.afficherEmploye()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}',f'{i[6]}',f'{i[7]}',f'{i[8]}',f'{i[9]}'))
            j+=1

        
        
root = Tk()
l = gestionEmploye(root)
root.mainloop()
