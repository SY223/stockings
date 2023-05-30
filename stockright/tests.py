from django.test import TestCase
from stockright.models import Pond, StockingDensity
from django.contrib.auth.models import User
from datetime import date


#Test models
class PondModelTestCase(TestCase):
    def setUp(self):
        #setup the user object and pond object
        self.user = User.objects.create_user(username='Brighton', password='thankyou33')
        self.pond = Pond.objects.create(
            name='riverdale',
            date_added=date.today(),
            owner=self.user
        )
        self.density = StockingDensity.objects.create(
            pond=Pond.objects.get(pk=self.pond.id),
            length=7.5,
            width=5.0,
            height=3.0,
        )
    

    def test_pond_name(self):
        self.assertEqual(self.pond.name, 'riverdale')
    
    def test_date_added(self):
        self.assertEqual(date.isoformat(self.pond.date_added), '2023-05-30')
    
    def test_owner(self):
        self.assertEqual(self.pond.owner, self.user)
    
    def test_density_floats(self):
        self.assertEqual(self.density.length, 5)



    


