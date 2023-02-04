from django import forms

from django.contrib.auth.models import User
from .models.models import Profile, Images ,Offre
from .models.models import Annonce
from .models.localisation import Localisation
from .models.category import Category
from .models.type import Type
from django.forms import ModelForm

class UpdateProfileForm(forms.ModelForm):
    adresse = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    numero = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = [ 'adresse', 'numero']

#----------------------------------------------
class AjoutAnnonceForm(ModelForm):
    class Meta :
        model = Annonce
        fields = ['titre_Annonce','description_Annonce','localisation_Annonce','type_Annonce','category_Annonce','surface_Annonce','prix_Annonce']
#----------------------------------------------
class AjoutLocalisationForm(ModelForm):
    class Meta :
        model = Localisation
        fields = '__all__'

 #----------------------------------------------
 
class ImageForm(ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = Images
        fields = ('image', )
        
#----------------------------------------------
class OffreForm(ModelForm):
    class Meta:
        model = Offre
        fields = ('body',)
