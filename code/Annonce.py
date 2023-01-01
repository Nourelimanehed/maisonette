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
    

    
    def afficherDetailsAnnonce(self, id_Annonce):
        self.c.execute("SELECT * FROM Annonce WHERE id = %s", (id_Annonce, ))
        return self.c.fetchone()
    def consulterMessages(self, id_user):
        # Consulter les messages d'un utilisateur
        self.c.execute("SELECT * FROM Message WHERE id_destination = %s", (id_user, ))
        return self.c.fetchone()

   

    