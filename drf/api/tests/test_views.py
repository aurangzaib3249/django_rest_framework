from email import header
import json
from wsgiref import headers
from django.test import TestCase
from django.test import Client
from ..models import *
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
class TestViews(TestCase):
    def setUp(self):
        self.user=User.objects.create(email="admin@gmail.com")
        self.user.set_password("admin")
        self.user.save()
        token=Token.objects.create(user=self.user)
    def test_login(self):
        client= Client()
        res=client.post('http://127.0.0.1:8000/login', {'email': 'admin@gmail.com', 'password': 'admin'})
        self.assertEquals(res.status_code,200)
    def test_wrong_email_or_password(self):
        client= Client()
        res=client.post('http://127.0.0.1:8000/login', {'email': 'wrong@gmail.com', 'password': 'wadmin'})
        self.assertEquals(res.status_code,200)
    def get_login(self):
        client= Client()
        res=client.post('http://127.0.0.1:8000/login', {'email': 'admin@gmail.com', 'password': 'admin'})
        data=self.convert_response(res)
        return data["data"]["token"]
    def convert_response(self,res):
        my_json = res.content.decode('utf8').replace("'", '"')
        data=json.loads(my_json)
        return data
    def test_list(self):
        client = APIClient()
        token=self.get_login()
        print(token)     
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        res=client.get('http://127.0.0.1:8000',content_type='application/json')
        data=self.convert_response(res)
        self.assertEquals(data,{"Data": [], "Count": 0})
    def test_list_pk(self):
        client = APIClient()
        token=self.get_login()
        print(token)     
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        res=client.get('http://127.0.0.1:8000/1',content_type='application/json')
        data=self.convert_response(res)
        self.assertEquals(data,{"Data": [], "Count": 0})
    def test_create_todo(self):
        client = APIClient()
        token=self.get_login()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        res=client.post('http://127.0.0.1:8000/', {'title': 'Django', 'status': 'Pending'})
        print(res.content)
        self.assertEquals(res.status_code,200)
    def test_create_todo_wrong(self):
        client = APIClient()
        token=self.get_login()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        res=client.post('http://127.0.0.1:8000/', {'status': 'Pending'})
        print(res.content)
        self.assertEquals(res.status_code,200)
    def test_delete_todo(self):
        client = APIClient()
        token=self.get_login()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        res=client.delete('http://127.0.0.1:8000/1', {'status': 'Pending'})
        self.assertEquals(res.status_code,200)
    def test_update_todo(self):
        client = APIClient()
        token=self.get_login()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        res=client.patch('http://127.0.0.1:8000/1', {'title': 'Update todo',"status":"Completed"})
       
        self.assertEquals(res.status_code,200)