from django.contrib import admin
from .models import Pizza, Topping, Sub, Dinner, Order

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Dinner)
admin.site.register(Order)
# Register your models here.
