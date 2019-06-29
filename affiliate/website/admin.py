from django.contrib import admin

from .models import Lottery, Winner, Customer

admin.site.register(Lottery),

admin.site.register(Winner),

admin.site.register(Customer),
