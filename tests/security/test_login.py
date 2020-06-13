from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from rest_framework import status

UserModel = get_user_model()


class LoginTest(APITestCase):

    def setUp(self):
        self.test_user = UserModel.objects.create_user('test@example.com', 'test1', 'test111', 34, 'testpassword')
        self.signin = reverse("sign-in",)

    def test_login_successful(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        self.assertEqual(UserModel.objects.count(), 1)
        self.assertEqual(UserModel.objects.all()[0],self.test_user)
        response = self.client.post(self.signin, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)

    def test_register_user_fail(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'email': 'foobar@example.com',
            'first_name': 'foobar',
            'last_name': 'foobar11',

        }

        response = self.client.post(self.signin , data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertContains(response.data['password'], 'This field is required.')

