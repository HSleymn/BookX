import sqlite3 
from impfunc import *
from tkinter import *

con = sqlite3.connect("bddsql.db")
cur = con.cursor()

class Table:
    def __init__(self, titre):
        self.title = titre
        
    
    def create_table(self):
        cur.execute("DROP TABLE IF EXISTS {}".format(self.title))
        requetenomtable = "CREATE TABLE {} (title TEXT, year INTEGER ,autor TEXT, statut TEXT)".format(self.title)
        return requetenomtable
    
    def ajout_livre(self, titre, auteur, year):
        
        statutbook = "Libre" 
        booktoadd = "INSERT INTO " + self.title +"(title,year,autor,statut) VALUES('{0}', {1}, '{2}', '{3}')".format(titre, year, auteur, statutbook)
        return booktoadd
    
    def supprimer_livre_par_titre(self):
        delbook = input("Veuillez insérer le titre du livre que vous souhaitez retirer :")
        booktodel = "DELETE FROM "+ self.title+" WHERE title ='{}'".format(delbook)
        return booktodel
    
    def supprimer_livre_par_auteur(self):
        delbook = input("Veuillez insérer le nom de l'auteur que vous souhaitez retirer :")
        booktodel = "DELETE FROM "+ self.title+" WHERE autor ='{}'".format(delbook)
        return booktodel    
    def sauvegarde(self):
        con.commit()


biblio = Table("BookX")
    
window = Tk()
window.title("Average Calculator")
window.geometry("1080x720")
window.minsize(480, 360)
window.config(background='#1068a4')

titre = StringVar()
auteur = StringVar()
year = StringVar()
myvar = StringVar()

def mywarWritten(*args):
    print ("mywarWritten"),myvar.get()

labelNum1 = Label(window, bg="#1068a4", fg="white", font=('Arial',"30", "bold"),text="Titre de l'oeuvre :", borderwidth=0, highlightthickness=0)
labelNum1.pack(expand=YES)


entryNum1 = Entry(window, textvariable=titre)
entryNum1.pack(expand=YES)

labelNum2 = Label(window, bg="#1068a4",fg="white", font=('Arial',"30", "bold"), text="Nom de l'auteur :", borderwidth=0, highlightthickness=0)
labelNum2.pack(expand=YES)
entryNum2 = Entry(window, textvariable=auteur )
entryNum2.pack(expand=YES)

labelNum3 = Label(window, bg="#1068a4",fg="white", font=('Arial',"30", "bold"), text="Année de publication:", borderwidth=0, highlightthickness=0)
labelNum3.pack(expand=YES)
entryNum3 = Entry(window, textvariable=year )
entryNum3.pack(expand=YES)

labelResult = Label(window, bg="#1068a4", fg="white",font=('Arial',"30", "bold"))
labelResult.pack(expand=YES)


click_btn_img = PhotoImage(file='button.jpg')
img_label= Label(image=click_btn_img)

CalculateBut = Button(window, image= click_btn_img,bg="#1068a4",activebackground="#1068a4",command=cur.execute(biblio.ajout_livre(titre, auteur, year)), height=150, width=500, borderwidth=0, highlightthickness=0)
CalculateBut.pack(expand=YES)

biblio.sauvegarde()
window.mainloop()