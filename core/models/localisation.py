from django.db import models

class Localisation(models.Model):
    adresse = models.CharField(max_length= 100,default='')
    wilaya= models.CharField(max_length=50)
    commune = models.CharField(max_length=50)
    zip = models.CharField(max_length=100)

    @staticmethod
    def get_all_Locations():
        return Category.objects.all()

    def __str__(self):
        loc = self.wilaya +' ' + self.commune
        return loc
'''class Localisation (models.TextChoices):
        ('1',"Adrar"),
        ('2',"Chlef"),
        ('3',"Laghouat"),
        ('4',"Oum El Bouaghi"),
        ('5',"Batna"),
        ('6',"Bejaia"),
        ('7',"Biskra"),

"Bechar",
    "Blida",
    "Bouira",
     "Tamanrasset",
    "Tebessa",
    "Tlemcen",
     "Tiaret",
    "Tizi Ouzou",
     "Alger",
     "Djelfa",
     "Jijel",
    "Setif",
    "Saida",
     "Skikda",
     "Sidi Bel Abbes","Annaba","Guelma","Constantine","Medea","Mostaganem","M'sila","Mascara","Ouargla",
    "Oran","El Baydah","Illizi","Bordj Bou Arreridj", "Boumerdes","El Taref","Tindouf","Tissemslit","El Oued","Khenchela",
    "Souk Ahras","Tipaza","Mila","Ain Defla","Naama", "Ain Temouchent","Ghardaia","Relizane","Timimoun","Bordj Baji Mokhtar","Ouled Djellal",
    "Beni Abbes","In Salah","In Guezzam","Touggourt","Djanet","El M'Ghair","El Meniaa",'''
