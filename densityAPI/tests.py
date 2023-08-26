from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from .serializers import PondSerializer
from stockright.models import Pond, StockingDensity
import json



User = get_user_model()


class UserListCreateTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.User = get_user_model()
        cls.Pond = Pond.objects.all()
        cls.Density = StockingDensity.objects.all()
    
    def setUp(self):
        self.user_data = {
            "username": "john",
            "email": "onlyme@gmail.com",
            "password1":"welcomeback",
            "password2":"welcomeback",
        }
        self.client = APIClient()
    
    def tearDown(self):
        # self.User.objects.all().delete()
        # self.Density.delete()
        # self.Pond.delete()
        self.client.logout()

    def test_user_can_register_with_right_info(self):
        response = self.client.post(reverse('rest_register'), self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.user = self.User.objects.get()
        self.assertEqual(self.User.objects.count(), 1)
        self.assertEqual(self.User.objects.get().email, "onlyme@gmail.com")
        self.assertFalse(self.User.objects.get().email_address_verified)


    def test_user_cannot_register_with_empty_data(self):
        response = self.client.post(reverse('rest_register'), {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_user_can_login(self):
        self.test_user_can_register_with_right_info()
        response = self.client.post(reverse('rest_login'),
                                    {"email": "onlyme@gmail.com", "password": "welcomeback"},format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_user_can_verify_email_address(self):
        pass


    def test_user_can_reset_password(self):
        pass
    
    def force_login_user(self):
        self.test_user_can_register_with_right_info()
        self.client.force_authenticate(user=self.user)

    def test_create_pond(self):
        self.force_login_user()
        data = {"name": "Concrete"}
        response = self.client.post('/api/v1/ponds/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pond.objects.count(), 1)
        self.assertEqual(Pond.objects.get().name, "Concrete")
        self.assertEqual(Pond.objects.get().owner, self.user)

    def test_get_pond_list(self):
        self.force_login_user()
        pond1 = Pond.objects.create(name='Pond One', owner=self.user)
        pond2 = Pond.objects.create(name='Pond Two', owner=self.user)
        response = self.client.get('/api/v1/ponds/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(pond1.name, 'Pond One')
        self.assertEqual(pond2.name, 'Pond Two')
        self.assertEqual(Pond.objects.count(), 2)
    
    
    def test_user_can_update_pond(self):
        self.force_login_user()
        pond1 = Pond.objects.create(name='Pond One', owner=self.user)
        pond = Pond.objects.get(id=pond1.id)
        updated_data = {
            'name': 'Earthen',
        }
        response = self.client.put(f'/api/v1/pond/{pond.id}/', data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_delete_pond(self):
        self.force_login_user()
        pond1 = Pond.objects.create(name='Pond One', owner=self.user)
        pond = Pond.objects.get(id=pond1.id)
        response = self.client.delete(f'/api/v1/pond/{pond.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Pond.objects.count(), 0)

    def test_user_can_post_a_density(self):
        self.force_login_user()
        pond1 = Pond.objects.create(name='Concrete', owner=self.user)
        pond= Pond.objects.get(id=pond1.id)
        one_density = {"pond": pond.id, "length": 12, "width": 6, "height":3}
        response = self.client.post(f'/api/v1/check-stocks/{pond.id}/', one_density, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        


    def test_user_can_get_a_density(self):
        self.force_login_user()
        pond1 = Pond.objects.create(name='Earthen', owner=self.user)
        pond= Pond.objects.get(id=pond1.id)
        one_density = StockingDensity.objects.create(
            pond=pond,
            length=3,
            width=6, 
            height=3,
            to_stock=20,
            verdict=20,
            twenty_percent_decrease=10,
            thirty_percent_decrease=10
        )
        one_density.save()
        response = self.client.get(f'/api/v1/single-stock/{one_density.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.Density.count(), 1)

        