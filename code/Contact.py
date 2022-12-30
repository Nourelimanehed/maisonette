class Contact:
    def __init__(self,nom,prenom,adresse,email,telephone):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse 
        self.email = email
        self.telephone = telephone
    
    def getContact(self):
        return (self.nom,self.prenom,self.adresse,self.email,self.telephone)
    
    def setNom(self,nom):
        self.nom = nom
    def setPrenom(self,prenom):
        self.prenom = prenom
    def setAdresse(self,adresse):
        self.adresse = adresse
    def setTelephone(self,telephone):
        self.telephone = telephone
    def getNom(self):
        return self.nom
    def getPrenom(self):
        return self.nom
    def getAdresse(self):
        return self.adresse
    def getTelephone(self):
        return self.telephone
