import pandas
from tkinter import *
import tkinter.ttk as ttk

class excel():
    def __init__(self,root):
        self.root = root
        self.root.geometry('800x800')
        self.root.title("Fichier excel")
        self.nom=StringVar()
        self.var=StringVar()
        

        
        #==============Nom fichier TEXTFIELD AND LABEL
        x = Label(self.root,text = "nom de ficher",anchor='w')
        x.grid(row = 1,column = 0,padx = 40,pady = 20)
        y= Entry(self.root,textvariable = self.nom)
        y.grid(row = 1,column = 1,ipady = 6,ipadx = 40,padx = 40)
    
       

        #=====================Boutton excel
        x = Button(self.root,text = "importer",command = self.read,anchor='c')
        x.grid(row = 1,column = 3,ipady = 4,ipadx = 13,padx = 10,pady=30)
        
         #=====================Boutton excel
        x = Button(self.root,text = "afficher",command = self.view,anchor='c')
        x.grid(row = 2,column = 3,ipady = 4,ipadx = 13,padx = 10,pady=30)
       
        
      
    def read(self):
        ch=self.nom.get()
        df=pandas.read_excel(ch,header=0)
        a=df.shape
        b=df.head()
        return df
    
    def view(self):
        #==========================Show Frame
        self.root=Tk()
        self.root.geometry('800x400')
        self.root.title("Affichage fichier excel")
        show_frame = Frame(self.root)
        show_frame.place(width = 1000,x = 0,y = 0 ,height = 300)
        texte=self.read()
        print(texte)
        labl_show = Message(show_frame,text = texte)
        labl_show.pack()
        
      



        
        
        
        
     
        
            



        
root = Tk()
l = excel(root)
root.mainloop()
