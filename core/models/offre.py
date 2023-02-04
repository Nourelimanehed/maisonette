
from django.db import models
from .models import Profile
from .models  import Annonce

class Offre(models.Model):
    annonce = models.ForeignKey(Annonce,
                             on_delete=models.CASCADE)
    body = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    #id_sender = models.ForeignKey(Profile,on_delete=models.CASCADE )
    class Meta:
        ordering = ('created',)
    def str(self):
        return self.body
    