from tkinter import *
from departement import departement
import tkinter.ttk as ttk

class gestionDepartement():
    def __init__(self,root):
        self.root = root
        self.root.geometry('800x300')
        self.root.title("Gestion département")
        self.id=StringVar()
        self.nom=StringVar()
        self.chefDepartement=StringVar()
  
        
  
        
    #Formulaire ajout Departement dans __init():
        #==============Num Departement TEXTFIELD AND LABEL
        x = Label(self.root,text = "Id Unique",anchor='w')
        x.grid(row = 1,column = 0,padx = 40,pady = 20)
        y= Entry(self.root,textvariable = self.id)
        y.grid(row = 1,column = 1,ipady = 6,ipadx = 40,padx = 40)
    
        #==============Nom departement TEXTFIELD AND LABEL
        x = Label(self.root,text = "Nom de département",anchor='w')
        x.grid(row = 2,column = 0,padx = 40,pady = 20)
        y= Entry(self.root,textvariable = self.nom)
        y.grid(row = 2,column = 1,ipady = 6,ipadx = 40,padx = 40)
        
        #=======================chef departement LABEL AND TEXTFIELD
        x= Label(self.root,text="Chef de département",anchor='w')
        x.grid(row = 3,column = 0,pady = 20)
        y = Entry(self.root,textvariable = self.chefDepartement)
        y.grid(row = 3,column = 1,ipady = 6,ipadx = 40,padx = 40)

        #=====================Boutton ajout
        x = Button(self.root,text = "Ajouter",command = self.add,anchor='c')
        x.grid(row = 5,column = 0,ipady = 4,ipadx = 13,padx = 10,pady=30)
        #=====================Boutton modifier
        x = Button(self.root,text = "Modifier",command = self.modifier,anchor='c')
        x.grid(row = 5,column = 3,ipady = 4,ipadx = 13,padx = 10,pady=30)
        #=====================Boutton Supprimer 
        x= Button(self.root,text = "Supprimer",command = self.remove,anchor='c')
        x.grid(row = 5,column = 2,ipady = 4,ipadx = 13,padx = 10,pady=30)
        #=====================Boutton affichage 
        x= Button(self.root,text = "Afficher",command = self.view,anchor='c')
        x.grid(row = 5,column = 1,ipady = 4,ipadx = 13,padx = 10,pady=30)
    #Fonction d'ajout d'un étudiant (sera appelée dérière le boutton "Ajouter"
    def add(self):
            D = departement(self.id.get(),self.nom.get(),self.chefDepartement.get())
            print("Departement: ",D.nom)
            D.ajouterDepartement()
    #Fonction dse suppression d'un étudiant sera appelée dans le boutton "Supprimer"  
    def remove(self):
        E = departement()
        E.supprimerDepartement(self.id.get())
    def modifier(self):
        E = departement(self.id.get(),self.nom.get(),self.chefDepartement.get())
        E.modifierDepartement(self.id.get())
    def view(self):
    
        #==========================Show Frame
        self.root=Tk()
        self.root.geometry('800x400')
        self.root.title("Affichage des départements")
        show_frame = Frame(self.root)
        show_frame.place(width = 1000,x = 0,y = 0 ,height = 300)
        labl_show = Label(show_frame,text = "Affichage des départements")
        labl_show.pack()
        
        #========================Main Frame
        x= Frame(self.root,bd = 10,relief = SUNKEN)
        x.place(width = 800,height = 300,x = 8,y = 58)
        tree = ttk.Treeview(x,height = 200)
        vsb = ttk.Scrollbar(x,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = RIGHT,fill = Y)
        tree.pack(side = TOP,fill = X)
        tree['columns'] = ("1","2","3")
        tree.column('#0',width=20)
        tree.column('1',width=20)
        tree.column('2',width=60)
        tree.column('3',width=60)
        
        tree.heading("#0",text = "num",anchor='c')
        tree.heading("1",text = "Id",anchor='c')
        tree.heading("2",text = "Nom",anchor='c')
        tree.heading("3",text = "Chef département",anchor='w')
        
        E=departement()
        rows=E.afficherDepartement()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}'))
            j+=1

        
root = Tk()
l = gestionDepartement(root)
root.mainloop()
