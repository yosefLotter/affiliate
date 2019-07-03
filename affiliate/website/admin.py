from django.contrib import admin

from .models import Lottery, Winner, Customer, Mini_lottery_list

admin.site.register(Lottery),

admin.site.register(Winner),

admin.site.register(Customer),

admin.site.register(Mini_lottery_list),
