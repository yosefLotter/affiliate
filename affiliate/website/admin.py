from django.contrib import admin

from .models import Lottery, Winner, Customer, Tabell

admin.site.register(Lottery),

admin.site.register(Winner),

admin.site.register(Customer),

admin.site.register(Tabell),
