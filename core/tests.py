from django.test import TestCase
from .models.category import Category
from .models.localisation import Localisation
from .models.offre import Offre
from .models.type import Type
from .models.models import Annonce, Images
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LocationTestCase(TestCase):
    def setUp(self):
        Localisation.objects.create(adresse = 'Oued Smar', wilaya= 'Alger', commune='Oued Smar',zip = '1600')
        Localisation.objects.create(adresse = 'El Kifan', wilaya= 'Tlemcen', commune='Mansourah',zip = '1310')
    def test_Location(self):
        
        adr1 = Localisation.objects.get(zip = '1600')
        adr2 = Localisation.objects.get(zip = '1310')
        self.assertEqual(adr1.__str__, 'Alger Oued Smar')
        self.assertEqual(adr2.__str__, 'Tlemcen Mansourah')


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name= 'Location')
        Category.objects.create(name = 'Vente')
    def test_Category(self):
        c1 = Category.objects.get(name='Location')
        c2 = Category.objects.get(name='Vente')
        self.assertEqual(c1.__str__, 'Location')
        self.assertEqual(c2.__str__, 'Vente')

class TypeTestCase(TestCase):
    def setUp(self):
        Type.objects.create(name='Terrain')
    def test_Type(self):
        c1 = Type.objects.get(name = 'Terrain')
        self.assertEqual(c1.__str__, 'Terrain')

#------------------------Selinuim test
class AnnonceFormTest(LiveServerTestCase):

  def testajoutAnnonceform(self):
    selenium = webdriver.Chrome()
    #Choose your url to visit
    selenium.get('http://127.0.0.1:8000/core/annonces/ajout/')
    #find the elements you need to submit form

    titre_Annonce = selenium.find_element_by_id('id_titre_Annonce')
    type_Annonce = selenium.find_element_by_id('id_type_Annonce ')
    category_Annonce= selenium.find_element_by_id('id_category_Annonce')
    surface_Annonce = selenium.find_element_by_id('id_surface_Annonce')
    description_Annonce = selenium.find_element_by_id('id_description_Annonce')
    prix_Annonce = selenium.find_element_by_id('id_prix_Annonce')
    date_Annonce = selenium.find_element_by_id('id_date_Annonce')
    localisation_Annonce =selenium.find_element_by_id('id_localisation_Annonce')
    submit = selenium.find_element_by_id('submit_button')

    #populate the form with data
    titre_Annonce = send_keys('Maison1')
    type_Annonce =send_keys('Terrain')
    category_Annonce= send_keys('Vente')
    surface_Annonce = send_keys('1344')
    description_Annonce = send_keys('Maison pour vente')
    prix_Annonce = send_keys('123')
    date_Annonce = send_keys('2023-02-02 09:12:10')
    localisation_Annonce = send_keys('Alger Oued Smar')
    submit = selenium.find_element_by_id('submit_button')

    #submit form
    submit.send_keys(Keys.RETURN)

    #check result; page source looks at entire html document
    assert 'Maison1' in selenium.page_source
