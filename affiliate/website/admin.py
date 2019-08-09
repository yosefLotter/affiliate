from django.contrib import admin

from .models import Lottery, Winner, Contact_us, Mini_lottery_list, Topp_10, Lottery_supplier, Article_links, Meta_tags_for_lottery, Meta_tags_for_winner, Loser

admin.site.register(Lottery),

admin.site.register(Winner),

admin.site.register(Contact_us),

admin.site.register(Mini_lottery_list),

admin.site.register(Topp_10),

admin.site.register(Lottery_supplier),

admin.site.register(Article_links),

admin.site.register(Meta_tags_for_lottery),

admin.site.register(Meta_tags_for_winner),

admin.site.register(Loser),