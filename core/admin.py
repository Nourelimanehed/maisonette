from django.contrib import admin


from .models.category import Category
from .models.localisation import Localisation
from .models.type import Type
from .models.offre import Offre
from .models.models import Annonce , Images , Profile , AnnonceManager

admin.site.register(Category)
admin.site.register(Localisation)
admin.site.register(Type)
admin.site.register(Images)
admin.site.register(Profile)
@admin.register(Annonce)
class AnnonceAdmin(admin.ModelAdmin):
    list_filter = ('type_Annonce','category_Annonce','date_Annonce','prix_Annonce')
    
@admin.register(AnnonceManager)
class AnnonceManagerAdmin(admin.ModelAdmin):
    list_filter = ('titre_Annonce','type_Annonce','wilaya_Annonce','commune_Annonce','periode_Annonce')
    
@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display = ('annonce','body', 'created')
    list_filter = ('created','annonce')
    
