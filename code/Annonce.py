# -*- coding: UTF-8 -*-
import mysql.connector
from mysql.connector.constants import ClientFlag

connexion = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="nourelimane13", 
    database="db", 
    port=3306,
     )
 
connexion.autocommit = True
class Annonce:
    def __init__(self):
        self.id_Annonce:None
        self.Surface: None
        self.Discription:None
        self.prix:None
        self.localisation:None
        self.categorie:None
        self.type:None
    
    