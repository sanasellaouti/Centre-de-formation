from tkinter import *
from Apprenant import Apprenant
import tkinter.ttk as ttk

class GestionApprenant():
    def __init__(self,root):
        self.root = root
        self.root.geometry('800x600')
        self.root.title("Gestion Apprenant")
        self.id_apprenant=IntVar()
        self.CIN=IntVar()
        self.nom_prénom=StringVar()
        self.filière=StringVar()
        self.téléphone=IntVar()
        self.email=StringVar()

        
    #Formulaire ajout Apprenant dans __init():
        #==============Id_apprenant TEXTFIELD AND LABEL
        a = Label(self.root,text = "Id_apprenant",anchor='w')
        a.grid(row = 1,column = 0,padx = 40,pady = 40)
        b = Entry(self.root,textvariable = self.id_apprenant)
        b.grid(row = 1,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================CIN apprenant LABEL AND TEXTFIELD
        a = Label(self.root,text = "CIN",anchor='w')
        a.grid(row = 1,column = 2,pady = 40)
        y = Entry(self.root,textvariable = self.CIN)
        y.grid(row = 1,column = 3,ipady = 7,ipadx = 20,padx = 20)
        #==============Nom_Prénom apprenant TEXTFIELD AND LABEL
        a = Label(self.root,text = "Nom_Prénom",anchor='w')
        a.grid(row = 2,column = 0,padx = 40,pady = 40)
        b = Entry(self.root,textvariable = self.nom_prénom)
        b.grid(row = 2,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================Filière apprenant LABEL AND TEXTFIELD
        a = Label(self.root,text="Filière",anchor='w')
        a.grid(row = 2,column = 2,pady = 40)
        b = Entry(self.root,textvariable = self.filière)
        b.grid(row = 2,column = 3,ipady = 7,ipadx = 20,padx = 20)
        #=======================Téléphone apprenant LABEL AND TEXTFIELD
        a = Label(self.root,text="Téléphone",anchor='w')
        a.grid(row = 3,column = 0,pady = 40)
        b = Entry(self.root,textvariable = self.téléphone)
        b.grid(row = 3,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #==============Email apprenant TEXTFIELD AND LABEL
        a = Label(self.root,text = "Email",anchor='w')
        a.grid(row = 3,column = 2,padx = 40,pady = 40)
        b = Entry(self.root,textvariable = self.email)
        b.grid(row = 3,column = 3,ipady = 7,ipadx = 20,padx = 20)

        #=====================Boutton ajout
        a = Button(self.root,text = "Ajouter",command = self.add,anchor='c')
        a.grid(row = 4,column = 0,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton affichage à ajouter après boutton "Ajouter" dans __init()__
        a = Button(self.root,text = "Afficher",command = self.view,anchor='c')
        a.grid(row = 4,column = 1,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        a = Button(self.root,text = "Supprimer",command = self.remove,anchor='c')
        a.grid(row = 4,column = 2,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton modification à ajouter après boutton "Suprimmer" dans __init()__
        a = Button(self.root,text = "Modifier",command = self.update,anchor='c')
        a.grid(row = 4,column = 3,ipady = 4,ipadx = 13,pady = 40)

        #Fonction d'ajout d'un apprenant (sera appelée dérière le boutton "Ajouter"
    def add(self):
        A = Apprenant(int(self.id_apprenant.get()),int(self.CIN.get()),self.nom_prénom.get(),self.filière.get(),int(self.téléphone.get()),self.email.get())
        print("Apprenant: ",A.nom_prénom)
        A.ajouterApprenant()
        
    def view(self):  
        #==========================Show Frame
        self.root=Tk()
        self.root.geometry('700x300')
        self.root.title("Gestion des apprenants")
        show_frame = Frame(self.root)
        show_frame.place(width = 800,x = 0,y = 0 ,height = 300)
        labl_show = Label(show_frame,text = "Affichage des apprenants")
        labl_show.pack()
        #========================Main Frame
        main_frame = Frame(self.root,bd = 10,relief = SUNKEN)
        main_frame.place(width = 600,height = 200,x = 8,y = 58)
        tree = ttk.Treeview(main_frame,height = 200)
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = RIGHT,fill = Y)
        tree.pack(side = TOP,fill = X)
        tree['columns'] = ("1","2","3","4","5","6")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.column('4',width=80)
        tree.column('5',width=80)
        tree.column('6',width=80)
        tree.heading("#0",text = "Id",anchor='c')
        tree.heading("1",text = "Id_apprenant",anchor='c')
        tree.heading("2",text = "CIN",anchor='c')
        tree.heading("3",text = "Nom_Prénom",anchor='w')
        tree.heading("4",text = "Filière",anchor='w')
        tree.heading("5",text = "Téléphone",anchor='w')
        tree.heading("6",text = "Email",anchor='w')
        A=Apprenant()
        rows= A.afficherApprenants()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}'))
            j+=1
#Fonction de suppression d'un apprenant sera appelée dans le boutton "Supprimer"  
    def remove(self):
        A = Apprenant()
        A.supprimerApprenant(self.id_apprenant.get())
#Fonction de modification d'un apprenant sera appelée dans le boutton "Modifier"
    def update(self):
        A = Apprenant(self.id_apprenant.get(),self.CIN.get(),self.nom_prénom.get(),self.filière.get(),self.téléphone.get(),self.email.get())
        A.modifierApprenant(self.id_apprenant.get())
       
             

root = Tk()
l = GestionApprenant(root)
root.mainloop()    
    
