from django.conf.urls import url
from django.urls import include, path


from .import views

app_name = 'website'
urlpatterns = [
	path('', views.index, name="index"),
	#For the best_lottery page
	path('best_lottery/', views.best_lottery, name='best_lottery'),



	path('winner/', views.winners, name="winners"),
	path('winner/<int:article_id>/', views.winner_article, name="winners"),

	path('lottery_page/', views.lottery_page, name='lottery_page'),
	path('lottery_page/<int:lottery_id>', views.lottery_page, name='lottery_page'),
]