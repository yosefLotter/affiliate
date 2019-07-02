from django.conf.urls import url
from django.urls import include, path


from .import views

app_name = 'website'
urlpatterns = [
	path('', views.index, name="index"),
	# For Europe_list Page.
	path('europe/', views.europe, name='europe'),
	# For Sydamerika_list page
	path('sydamerika/', views.sydamerika, name='sydamerika'),
	# For Amerika list page
	path('amerika/', views.amerika, name='amerika'),
	# Asien Page
	path('asien/', views.asien, name='asien'),

	#For the highest_jackpots page
	path('highest-jackpots/', views.highest_jackpots, name='highest_jackpots'),

	path('lottery-<slug>/', views.lottery_detail, name='lottery_detail'),


	path('winner/<slug>/', views.winner_page, name='winner_page'),

	path('faq-questions/', views.faq_questions, name='faq_questions'),


]