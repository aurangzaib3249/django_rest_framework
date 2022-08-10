from django.test import TestCase
from ..models import *
from django.contrib.auth import authenticate
# Create your tests here.


class UserModelTest(TestCase):
    def setUp(self):
        self.user=User.objects.create(email="admin@gmail.com")
        self.user.set_password("admin")
        self.user.save()
    def test_existance(self):
        u=User.objects.get(id=1)
        self.assertEqual(u,self.user)
    def test_login_correct(self):
        user=authenticate(email="admin@gmail.com",password="admin")
        self.assertTrue(user is not None and user.is_authenticated)
    def test_login_wrong(self):
        user=authenticate(email="admin@gmail.com",password="admin1122334455")
        self.assertFalse(user is not None and user.is_authenticated)
    def test_delete_user(self):
        self.user.delete()

