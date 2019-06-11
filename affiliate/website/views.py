from django.shortcuts import render, redirect

from .models import  Lottery, Lottery_image, Article, Winner, First_page
# Create your views here.


def index(request):
	# content = First_page.objects.all()
	# context = {
	# 	'content' : content
	# }
	return render(request, 'index.html')

def europe_list(request):
	return render(request, 'europe_list.html')

# For Best_lottery Page
# Ta bort ARTICLE SKA VAR LOTTERY!!! 
def highest_jackpots(request):
	lotteries = Lottery.objects.all()
	context = {
		'lotteries' : lotteries
	}
	return render(request, 'highest_jackpots.html', context)


def faq_questions(request):
	winners = Winner.objects.filter(lottery_id=1)
	context = {
		'winners':winners
	}
	return render(request, 'faq.html', context)

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

