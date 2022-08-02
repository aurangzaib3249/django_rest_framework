from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
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