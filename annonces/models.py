from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from localisation.models import Localisation
from categorie.models import Categorie
from django.urls import reverse
import os


class Annonce(models.Model):
    titre_Annonce = models.CharField(max_length=300)
    categorie_Annonce = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    type_Annonce = models.CharField(max_length=50)
    surface_Annonce = models.IntegerField(null = True)
    description_Annonce = models.TextField()
    prix_Annonce = models.FloatField(null=True)
    date_Annonce = models.DateTimeField(default=timezone.now)
    #file = models.FileField(null=True,blank=True,upload_to='Files')
    user_Annonce = models.ForeignKey(User, on_delete=models.CASCADE)
    localisation_Annonce = models.ForeignKey(Localisation, on_delete=models.CASCADE)
    images_Annonce = models.FilePathField(path="/img")

    objects = AnnonceManager()

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

    

