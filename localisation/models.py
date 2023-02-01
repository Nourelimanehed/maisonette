from django.db import models

# Create your models here.
class Localisation(models.models.TextChoices):
    choix_categorie(
    (VENTE ,'VENTE'),
    (ECHANGE ,'ECHANGE'),
    (LOCATION , 'LOCATION'),
    (LOCATION_VACANCES , 'LOCATION VACANCES'),
    )
    choix_categorie = models.CharField(
        choices=Categorie.choices,
        default=Categorie.LOCATION
    )