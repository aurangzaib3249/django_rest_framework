from unicodedata import category
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
     
     
class ItemCategory(models.Model):
    category=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.category
    
class Item(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(ItemCategory,on_delete=models.CASCADE)
    price=models.IntegerField(default=0)
    discount=models.DecimalField(default=0,decimal_places=2,max_digits=5)
    qty=models.IntegerField(default=0)
    remaining_qty=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
class Coupen(models.Model):
    code=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    expire_date=models.DateTimeField(auto_now_add=True)
    min_amount=models.IntegerField(default=10)
    amount=models.IntegerField(default=0)
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.DecimalField(default=0,decimal_places=2,max_digits=5)
    discount=models.DecimalField(default=0,decimal_places=2,max_digits=5)
    date=models.DateTimeField(auto_now_add=True)
    coupen=models.ForeignKey(Coupen,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    price=models.DecimalField(default=0,decimal_places=2,max_digits=5)
    qty=models.IntegerField(default=1)
    def __str__(self) -> str:
        return self.item.name