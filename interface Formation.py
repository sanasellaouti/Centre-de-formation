from tkinter import *
from Formation import Formation
import tkinter.ttk as ttk

class GestionFormation():
    def __init__(self,root):
        self.root = root
        self.root.geometry('800x600')
        self.root.title("Gestion Formation")
        self.id_formation=IntVar()
        self.libellé=StringVar()
        self.responsable=StringVar()
        self.durée=IntVar()

     #Formulaire ajout Apprenant dans __init():
        #==============Id_formation TEXTFIELD AND LABEL
        a = Label(self.root,text = "Id_formation",anchor='w')
        a.grid(row = 1,column = 0,padx = 40,pady = 40)
        b = Entry(self.root,textvariable = self.id_formation)
        b.grid(row = 1,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================Libellé formation LABEL AND TEXTFIELD
        a = Label(self.root,text = "Libellé",anchor='w')
        a.grid(row = 1,column = 2,pady = 40)
        y = Entry(self.root,textvariable = self.libellé)
        y.grid(row = 1,column = 3 ,ipady = 7,ipadx = 20,padx = 20)
        #==============Responsable formation TEXTFIELD AND LABEL
        a = Label(self.root,text = "Responsable",anchor='w')
        a.grid(row = 2,column = 0,padx = 40,pady = 40)
        b = Entry(self.root,textvariable = self.responsable)
        b.grid(row = 2,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================Durée formation LABEL AND TEXTFIELD
        a = Label(self.root,text="Durée",anchor='w')
        a.grid(row = 2,column = 2,pady = 40)
        b = Entry(self.root,textvariable = self.durée)
        b.grid(row = 2,column = 3,ipady = 7,ipadx = 20,padx = 20)

        #=====================Boutton ajout
        a = Button(self.root,text = "Ajouter",command = self.add,anchor='c')
        a.grid(row = 3,column = 0,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton affichage à ajouter après boutton "Ajouter" dans __init()__
        a = Button(self.root,text = "Afficher",command = self.view,anchor='c')
        a.grid(row = 3,column = 1,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        a = Button(self.root,text = "Supprimer",command = self.remove,anchor='c')
        a.grid(row = 3,column = 2,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton modification à ajouter après boutton "Suprimmer" dans __init()__
        a = Button(self.root,text = "Modifier",command = self.update,anchor='c')
        a.grid(row = 3,column = 3,ipady = 4,ipadx = 13,pady = 40)
        
        #Fonction d'ajout d'une formation (sera appelée dérière le boutton "Ajouter"
    def add(self):
        F = Formation(int(self.id_formation.get()),self.libellé.get(),self.responsable.get(),int(self.durée.get()))
        print("Formation: ",F.libellé)
        F.ajouterFormation()

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
        tree['columns'] = ("1","2","3","4")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.column('4',width=80)
        tree.heading("#0",text = "Id",anchor='c')
        tree.heading("1",text = "Id_formation",anchor='c')
        tree.heading("2",text = "Libellé",anchor='c')
        tree.heading("3",text = "Ronsponsable",anchor='w')
        tree.heading("4",text = "Durée",anchor='w')
        F=Formation()
        rows=F.afficherFormations()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}'))
            j+=1
       #Fonction de suppression d'un apprenant sera appelée dans le boutton "Supprimer"  
    def remove(self):
        F = Formation() 
        F.supprimerFormation(self.id_formation.get())
       #Fonction de modification d'un apprenant sera appelée dans le boutton "Modifier"
    def update(self):
        F = Formation(self.id_formation.get(),self.libellé.get(),self.responsable.get(),self.durée.get())
        F.modifierFormation(self.id_formation.get())


root = Tk()
l = GestionFormation(root)
root.mainloop()  
