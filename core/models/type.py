from django.db import models

class Type(models.Model):
    name= models.CharField(max_length=50)

    @staticmethod
    def get_all_types():
        return Type.objects.all()

    def __str__(self):
        return self.name
