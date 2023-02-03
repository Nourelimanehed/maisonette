from django.test import TestCase
from .models.category import Category
from .models.localisation import Localisation
from .models.offre import Offre
from .models.type import Type
from .models.models import Annonce, Images

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