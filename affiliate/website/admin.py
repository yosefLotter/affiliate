from django.contrib import admin

from .models import Lottery, Winner, Contact_us, Mini_lottery_list

admin.site.register(Lottery),

admin.site.register(Winner),

admin.site.register(Contact_us),

admin.site.register(Mini_lottery_list),
