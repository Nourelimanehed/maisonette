# -*- coding: UTF-8 -*-
import mysql.connector
from mysql.connector.constants import ClientFlag
 
class Annonce:
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="nourelimane13", 
            database="db", 
            port=3306,
        )
        self.c = self.db.cursor()
        self.id_Annonce:None
        self.Surface: None
        self.Discription:None
        self.prix:None
        self.localisation:None
        self.categorie:None
        self.type:None
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    def ajouterAnnonce(self, fields):
        try:
            self.c.execute("INSERT INTO Annonce (categorie,type,surface,description,prix,id_user,id_localisation) VALUES (%s, %s, %s, %s,%s,%s,%s)",
                       (fields[0].get(), fields[1].get(), fields[2].get(), fields[3].get(),fields[4].get(),fields[5].get(),fields[6].get()))
        except:
            pass

    
    def consulterAnnonce(self, id_Annonce):
        self.c.execute("SELECT * FROM Annonce WHERE id = %s", (id_Annonce, ))
        return self.c.fetchone()

   

    def supprimerAnnonce(self, id_Annonce):
        self.c.execute("DELETE FROM Annonce WHERE id = %s", (id_Annonce, ))