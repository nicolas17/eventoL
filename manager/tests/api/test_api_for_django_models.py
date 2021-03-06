import unittest
from django.contrib.auth.models import User
from manager.tests.api.test_api import api_test


# Django Models
@api_test()
class TestApiUser():
    str_model = 'auth.User'
    model = User
    url_base = '/api/users/'
    filter_fields = ['username']
    example = {
        'username': 'Example username',
    }
