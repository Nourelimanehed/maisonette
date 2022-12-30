# -*- coding: UTF-8 -*-
import mysql.connector
from mysql.connector.constants import ClientFlag
 
class Message:
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
        self.content:None
        self.source: None
        self.destination:None
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    
    def ajouterMessage(self, fields):
        try:
            self.c.execute("INSERT INTO Message (content,id_source,id_destination) VALUES (%s, %s, %s)",
                       (fields[0].get(), fields[1].get(), fields[2].get()))
        except:
            pass

    
    def consulterMessages(self, id_user):
        # Consulter les messages d'un utilisateur
        self.c.execute("SELECT * FROM Message WHERE id_destination = %s", (id_user, ))
        return self.c.fetchone()

   

    def supprimerMessage(self, id_Message):
        self.c.execute("DELETE FROM Annonce WHERE id_Message = %s", (id_Message, ))
    