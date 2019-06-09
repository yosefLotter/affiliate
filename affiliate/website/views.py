from django.shortcuts import render, redirect

from .models import  Lottery, Lottery_image, Article, Winner, First_page
# Create your views here.


def index(request):
	# content = First_page.objects.all()
	# context = {
	# 	'content' : content
	# }
	return render(request, 'index.html')

# For Best_lottery Page
def best_lottery(request):
	articles = Article.objects.all()
	context = {
		'articles' : articles
	}
	return render(request, 'best_lottery.html', context)


def faq_questions(request):
	return render(request, 'faq.html')

def lottery_page(request, lottery_id):
	lottery = Article.objects.filter(lottery_id=lottery_id)
	images = Lottery_image.objects.filter(lottery_id=lottery_id).all()
	winners = Winner.objects.filter(lottery_id=lottery_id)
	context = {
		'lottery': lottery,
		'images': images,
		'winners': winners,
	}
	return render(request, 'lottery_page.html', context)






def winner_page(request):
	return render(request, 'winner_page.html')

def winner_page(request, winner_id):
	winners = Winner.objects.filter(pk=winner_id)
	lottery_images = Lottery_image.objects.filter(lottery_id=winner_id)
	context = {
		'winners': winners,
		'lottery_images': lottery_images,
	}
	return render(request, 'winner_page.html', context)

