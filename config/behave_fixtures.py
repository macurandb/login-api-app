from behave import fixture
from django.contrib.auth import get_user_model
from django.test.runner import DiscoverRunner
from rest_framework.test import APITestCase, APIClient

UserModel = get_user_model()


@fixture
def django_test_runner(context):
    context.test_runner = DiscoverRunner()


@fixture
def django_test_case(context):
    context.test_case = APITestCase()
    context.test_case.setUpClass()
    context.test_case.apiClient = APIClient()
    context.test_user = UserModel.objects.create_user('test@example.com', 'test1', 'test111', 34, 'testpassword')

    yield
    context.test_case.tearDownClass()
    del context.test_case
