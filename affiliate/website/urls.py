from django.conf.urls import url
from django.urls import include, path


from .import views

app_name = 'website'
urlpatterns = [
	path('', views.index, name="index"),
	# For Europe_list Page.
	path('europe_list/', views.europe_list, name='europe_list'),
	# For Sydamerika_list page
	path('sydamerika_list/', views.sydamerika_list, name='sydamerika_list'),
	# For Amerika list page
	path('amerika_list/', views.amerika_list, name='amerika_list'),
	#For the highest_jackpots page
	path('highest_jackpots/', views.highest_jackpots, name='highest_jackpots'),

	path('lottery_page/', views.lottery_page, name='lottery_page'),
	path('lottery_page/<int:lottery_id>', views.lottery_page, name='lottery_page'),


	path('winner_page/', views.winner_page, name='winner_page'),
	path('winner_page/<int:winner_id>/', views.winner_page, name='winner_page'),

	path('faq_questions/', views.faq_questions, name='faq_questions'),

]