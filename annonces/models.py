from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os


class Annonce(models.Model):

    class Categorie(models.TextChoices):
        
        ('VENTE' ,'VENTE'),
        ('ECHANGE' ,'ECHANGE'),
        ('LOCATION' , 'LOCATION'),
        ('LOCATION_VACANCES' , 'LOCATION VACANCES'),
        

    class Localisation (models.TextChoices):
        ('1',"Adrar"),
        ('2',"Chlef"),
        ('3',"Laghouat"),
        ('4',"Oum El Bouaghi"),
        ('5',"Batna"),
        ('6',"Bejaia"),
        ('7',"Biskra"),
    ''' 
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
    #-------------------------------------------
    titre_Annonce = models.CharField(max_length=300)
    categorie_Annonce = models.CharField(
        max_length = 100,
        choices = Categorie,
        default = 'LOCATION'
        )
    type_Annonce = models.CharField(max_length=50)
    surface_Annonce = models.IntegerField(null = True)
    description_Annonce = models.TextField()
    prix_Annonce = models.FloatField(null=True)
    date_Annonce = models.DateTimeField(default=timezone.now)
    #file = models.FileField(null=True,blank=True,upload_to='Files')
    user_Annonce = models.ForeignKey(User, on_delete=models.CASCADE)
    localisation_Annonce = models.CharField(
        max_length= 100,
        choices= Localisation,
        default= 'Alger'
        )
    images_Annonce = models.FilePathField(path="/img")

    '''objects = AnnonceManager()

    class Meta:
        ordering = ['-datetime']

    def __str__(self):
        return self.titre_Annonce
    def save(self, *args, **kwargs):
        super(Annonce, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        x = 300
        y = 400

        if img.height > x or img.width > y:
            output_size = (x,y)
            img.thumbnail(output_size)
            img.save(self.image.path)

class AnnonceQuerySet(models.QuerySet):
    def feed(self, user):
        followed_users_id = user.following.values_list("user__id", flat=True)
        return self.filter(
            Q(user__id__in=followed_users_id) |
            Q(user=user)
        ).distinct()

   

class AnnonceManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return AnnonceQuerySet(self.model, using=self._db)

    '''

