from django.urls import path

from . import views

urlpatterns = [
   
path('annonces/index/',views.show_annonces,name="index"),
path('annonces/ajout/',views.ajout_Annonce , name = 'ajouter'),
path('annonces/search/<int:annonce_id>/ajoutOffre/',views.ajout_Offre , name = 'ajouterOffre'),
path('annonces/search/<int:annonce_id>',views.consulterAnnonce,name="details"),
path('profile/', profile, name='users-profile'),
path('annonces/filtrer/',views.rechercheranc , name = 'filtrer'),
path('annonces/affich/',views.afficherPropreanc , name = 'afficher_propre_anc'),

]
