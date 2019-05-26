from django.conf.urls import url
from django.urls import include, path


from .import views

app_name = 'website'
urlpatterns = [
	path('', views.index, name="index"),

	path('us_powerball/', views.us_powerball, name="us_powerball"),
	path('mega_millions/', views.mega_millions, name="mega_millions"),
	path('cash4life/', views.cash4life, name="cash4life"),
	path('best_lottery/', views.best_lottery, name="best_lottery"),

	path('winner/', views.winners, name="winners"),
	path('winner/<int:article_id>/', views.winner_article, name="winners"),
]