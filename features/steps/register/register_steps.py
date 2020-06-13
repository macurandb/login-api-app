from behave import given, when, then

from django.urls import reverse
from rest_framework import status


@given(u'the user put "{first_name}", "{last_name}", "{email}",  "{password}", "{age}"')
def step_impl(context, first_name, last_name, email,  password, age):
    context.url = reverse("register-user")
    data = {
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'password': password
    }
    context.response = context.test_case.apiClient.post(context.url, data, format='json')


@when(u'the user send data to register URL')
def step_impl(context):
    pass


@then(u'the system register "{status_code}" and "{status_text}" and token')
def step_impl(context, status_code, status_text):

    context.test_case.assertEqual(context.response.status_code, int(status_code))
    context.test_case.assertEqual(context.response.status_text, status_text)

    if status_code == status.HTTP_201_CREATED:
        context.test_case.assertIn('token', context.response)


@then(u'the system register "400" and "Bad Request"')
def step_impl(context):
    context.test_case.assertEqual(context.response.status_code, 400)
    context.test_case.assertEqual(context.response.status_text, "Bad Request")


