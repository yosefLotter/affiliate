from django.conf.urls import url
from django.urls import include, path


from .import views

app_name = 'website'

urlpatterns = [
	path('', views.index, name="index"),
	# For Europe_list Page.
	path('europeiska-lotter/', views.europe, name='europe'),
	# For Sydamerika_list page
	path('sydamrikanska-lotter/', views.sydamerika, name='sydamerika'),
	# For Amerika list page
	path('amrikanska-lotter/', views.amerika, name='amerika'),
	# Asien Page
	path('asiatiska-lotter/', views.asien, name='asien'),

	#For the highest_jackpots page
	path('top-jackpottar/', views.highest_jackpots, name='highest_jackpots'),

	path('lottery-<slug>/', views.lottery_detail, name='lottery_detail'),

	path('vinnare/<slug>/', views.winner_page, name='winner_page'),

	path('faq-fragor/', views.faq_questions, name='faq_questions'),

	path('kontakta-oss/', views.contact_page, name='contact_page'),

	path('spela-ansvarsfullt/', views.spela_ansvarsfullt, name='spela_ansvarsfullt'),

	path('artiklar/', views.all_article_page, name='all_article_page'),

	path('utbetalning/', views.utbetalning, name='utbetalning'),

]

