import random
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.
import string  
class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        domain="@gmail.com"
        password="adminasdfghjqweq"
        if not email:
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))    
            email="{}{}".format(ran,domain)
           
        if not password:
            password=''.join(random.choices(string.ascii_uppercase + string.digits, k = 8))    
            
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        if password:
            user.set_password(password)
       
        user.save()
        return user
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        return self.create_user(email,password,**extra_fields)
class User(AbstractUser):
    username=None
    email=models.EmailField(_("E-mail"),unique=True)
    full_name=models.CharField(_("Full name"),max_length=30)
    phone_number=models.CharField(_("Phone Number"),max_length=20)
    address=models.CharField(_("Home Address"),max_length=200)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    objects=UserManager()
    
    
choices=(
    ("Pending","Pending"),
    ("Completed","Completed"),
    ("Rejected","Rejected"),
    
)
class Todo(models.Model):
    #user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=30,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=choices,default="Pending",max_length=20)
    def __str__(self) -> str:
         return "{} create at {} and status {}".format(self.title,self.created_at,self.status)