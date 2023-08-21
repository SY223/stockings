from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from .serializers import PondSerializer
from stockright.models import Pond



User = get_user_model()


class PondListCreateTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.User = get_user_model()
    
    def setUp(self):
        self.user_data = {
            "username": "john",
            "email": "onlyme@gmail.com",
            "password1":"welcomeback",
            "password2": "welcomeback",
        }
        self.client = APIClient()
    
    def tearDown(self):
        self.User.objects.all().delete()
    
    def test_user_can_register_with_right_info(self):
        response = self.client.post(reverse_lazy('rest_register'), self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.user = self.User.objects.get()
        self.assertEqual(self.User.objects.count(), 1)
        self.assertEqual(self.User.objects.get().email, "onlyme@gmail.com")
        self.assertFalse(self.User.objects.get().email_address_verified)

    def test_user_cannot_register_with_empty_data(self):
        response = self.client.post(reverse_lazy('rest_register'), {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_user_can_login(self):
        self.client.post(reverse_lazy('rest_register'), self.user_data, format='json')
        response = self.client.post(reverse_lazy('rest_login'), {"email": "onlyme@gmail.com", "password":"welcomeback"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        






    # def test_login_successful(self):
    #     url = reverse('rest_login') #actual name of the login endpoint
    #     data = {
    #         'email':'onlyme@gmail.com',
    #         'password':'welcomeback'
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIn('access', response.data)

    # def test_login_unsuccessful(self):
    #     url = reverse('rest_login') #actual name of the login endpoint
    #     data = {
    #         'email':'onlyme@gmail.com',
    #         'password':'wrongpassword'
    #     }
    #     response = self.client.post(url, data, format='json')
    #     print(response.data)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    



        