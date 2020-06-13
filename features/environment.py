from behave import use_fixture
from config.behave_fixtures import django_test_runner, django_test_case
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')


def before_all(context):
    use_fixture(django_test_runner, context)


def before_scenario(context, scenario):
    use_fixture(django_test_case, context)