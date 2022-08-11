from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(Todo)
admin.site.register(Coupen)
admin.site.register(ItemCategory)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
