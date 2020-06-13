from behave import given, when, then

from django.urls import reverse
from rest_framework import status

@given(u'the email is "{email}"')
def step_impl(context, email):
    context.email= email

@given(u'the password is "{password}"')
def step_impl(context, password):
    context.password = password

@when(u'the user send data to login URL')
def step_impl(context):
    context.url = reverse("sign-in",)

    email = context.email
    password = context.password
    context.body = {
        "email": "%s" % (context.email),
        "password": "%s" % (context.password)
    }
    context.response = context.test_case.apiClient.post(context.url, context.body, format='json')

@then(u'the system should response "{status_code}" and "{status_text}"')
def step_impl(context, status_code , status_text):

    context.test_case.assertEqual(context.response.status_code, int(status_code))
    context.test_case.assertEqual(context.response.status_text, status_text)

    if context.response.status_code == status.HTTP_200_OK :
        context.test_case.assertIn("token", context.response.data)
