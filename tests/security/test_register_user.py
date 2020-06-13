from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status

UserModel = get_user_model()


class RegisterUser(APITestCase):

    def setUp(self):
        self.test_user = UserModel.objects.create_user('test@example.com', 'test1', 'test111',34 , 'testpassword')

        # URL for creating an account.
        self.create_url = reverse('register-user')

    def test_register_user_successful(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'email': 'foobar@example.com',
            'first_name': 'foobar',
            'last_name': 'foobar11',
            'age': 33,
            'password': 'somepassword'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(UserModel.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'], data['first_name'])
        self.assertEqual(response.data['email'], data['email'])

    def test_register_user_fail(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'email': 'foobar@example.com',
            'first_name': 'foobar',
            'last_name': 'foobar11',

        }

        response = self.client.post(self.create_url , data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertContains(response.data['password'], 'This field is required.')

