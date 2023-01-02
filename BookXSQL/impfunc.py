import sqlite3

def creationtable(cur):
    nomtable = input("Quel est le nom de la table ? ")
    requetenomtable = "CREATE TABLE {} (title TEXT, year INTEGER,autor TEXT)".format(nomtable)
    cur.execute(requetenomtable)




def ajout_livre(tablename, cursor):
    compteur = input("Combien de livre souhaitez vous ajouter : ")
    for i in range(compteur):
        addbook = input("Veuillez insérer le titre du livre que vous souhaitez ajouter : ")
        booktoadd = """INSERT INTO {0} VALUES('{1}', 1976, 8.2)""".format(tablename ,addbook)
        cursor.execute(booktoadd)



def supprimer_livre_par_titre(cursor):
    delbook = input("Veuillez insérer le titre du livre que vous souhaitez retirer :")
    booktodel = "DELETE FROM movie WHERE title ='{}'".format(delbook)
    cursor.execute(booktodel)

def supprimer_livre_par_auteur(cursor):
    delbook = input("Veuillez insérer le nom de l'auteur que vous souhaitez retirer :")
    booktodel = "DELETE FROM movie WHERE title ='{}'".format(delbook)
    cursor.execute(booktodel)
