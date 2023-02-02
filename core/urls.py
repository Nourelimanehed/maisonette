from django.urls import path

from . import views

urlpatterns = [
   
path('annonces/search/',views.show_annonce_detail,name="details"),
path('annonces/',views.ajout_Annonce , name = 'ajouter'),
path('annonces/search/<int:annonce_id>',views.consulterAnnonce,name="details"),
#path('profile/', profile, name='users-profile'),
]