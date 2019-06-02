from django.contrib import admin

from .models import Lottery, Lottery_image, Article, Winner

admin.site.register(Lottery),

admin.site.register(Lottery_image),

admin.site.register(Article),

admin.site.register(Winner),