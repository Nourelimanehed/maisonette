from django.contrib import admin


from .models.category import Category
from .models.localisation import Localisation
from .models.type import Type
from .models.models import Annonce , Images

admin.site.register(Annonce)
admin.site.register(Category)
admin.site.register(Localisation)
admin.site.register(Type)
admin.site.register(Images)