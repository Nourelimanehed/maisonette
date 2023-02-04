from django.shortcuts import render, get_list_or_404

# Create your views here.
from django.http import HttpResponse
from .models.models import Annonce , Profile,Images , AnnonceManager
from .models.offre import Offre
from .forms import AjoutAnnonceForm, AjoutLocalisationForm, ImageForm, OffreForm ,UpdateProfileForm
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect


'''def index(request,annonce_id):
    annonce = get_object_or_404(Annonce, pk=annonce_id)
    return render(request, 'core/index.html', {'annonce': annonce})
from .models import Book, Author, BookInstance, Genre'''

def show_annonces(request) :
    list_annonce = Annonce.objects.all().order_by('-date_Annonce')
    context = {'list_annonce': list_annonce}

    return render(request,"annonce_details.html", context)
#----------------------------------------------
def consulterAnnonce(request,annonce_id) :
    annonce = Annonce.objects.get(pk=annonce_id)
    #context = {'annonce':annonce}
    offres = Offre.objects.filter(annonce = annonce_id).values()

    return render(request,"consulterAnnonce.html", {'annonce':annonce, 'offres': offres,})
#----------------------------------------------
@login_required
 def profile(request):
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if  profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'updateprofile.html', { 'profile_form': profile_form})
#----------------------------------------------

def ajout_Annonce(request):
    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=5)
    if request.method == 'POST':
        ajout_Annonce_form = AjoutAnnonceForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())
    

        if ajout_Annonce_form.is_valid()  and formset.is_valid(): 
            annonce_form = ajout_Annonce_form.save(commit=False)
            annonce_form.user =request.user
            annonce_form.save()
            
            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(annonce_id=annonce_form, image=image)
                    photo.save()
            # use django messages framework
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("core/annonces/search")
        else:
            print(AjoutAnnonceForm.errors, formset.errors)
    else:
        ajout_Annonce_form = AjoutAnnonceForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'ajouterAnnonce.html',
                  {'ajout_Annonce_form': ajout_Annonce_form, 'formset': formset})
#----------------------------------------------

def ajout_Offre(request, annonce_id):
    annonce = Annonce.objects.get(pk=annonce_id)
    new_offre = None
    if request.method == 'POST':
        # An offer was posted
        offre_form = OffreForm(request.POST)
        if offre_form.is_valid():
            new_offre = offre_form.save(commit=False)
            new_offre.annonce = annonce
            # Save the offre to the database
            new_offre.save()
        return HttpResponseRedirect('annonces/search/<int:annonce_id>')
    else:
        offre_form = OffreForm()
    return render(request,
                  'ajouterOffre.html',
                  {
                    'annonce_id':annonce_id,
                    'annonce' : annonce,
                    'new_offre' : new_offre,
                   'offre_form': offre_form})
#----------------------------------------------
def rechercheranc(request) :
    if request.method=='POST':
        type_Annnonce= request.POST.get('Type')
        wilaya_Annonce= request.POST.get('Wilaya')
        commune_Annonce= request.POST.get('Commune')
        periode_Annonce= request.POST.get('Periode')
        ancsearchobj = AnnonceManager.objects.raw('select * from liste_annonce where type="'+type_Annonce+'" and wilaya="'+wilaya_Annonce+'" and commune="'+commune_Annonce+'" and periode="'+periode_Annonce+'" ')
        return render(request,'afficher_annonce.html',{"AnnonceManager":ancsearchobj})
    else :
        ancobj = AnnonceManager.objects.raw('select * from liste_annonce')
        return render(request,'afficher_annonce.html',{"AnnonceManager":ancobj})
  
#----------------------------------------------

def afficherPropreanc(request) :
    current_user = request.user
    if request.user.is_authenticated :
        annonce_id = current_user.id
        ancobj = AnnonceManager.objects.raw('select * from liste_annonce where type="'+annonce_id+'" ')
        return render(request,'afficher_annonce.html',{"AnnonceManager":ancobj})
