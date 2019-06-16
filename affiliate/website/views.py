from django.shortcuts import render, redirect

from .models import  Lottery, Lottery_image, Article, Winner, First_page
# Create your views here.


def index(request):
	return render(request, 'index.html')

# Europa sida
def europe_list(request):
	europe_list = Lottery.objects.filter(continent='Europa')
	context = {
		'europe_list': europe_list,
	}
	return render(request, 'europe_list.html', context)


def sydamerika_list(request):
	sydamerika_list = Lottery.objects.filter(continent='Sydamerika')
	context = {
		'sydamerika_list': sydamerika_list,
	}
	return render(request, 'sydamerika_list.html', context)



def amerika_list(request):
	amerika_list = Lottery.objects.filter(continent='Amerika')
	context = {
		'amerika_list': amerika_list,
	}
	return render(request, 'amerika_list.html', context)


# For Best_lottery Page
def highest_jackpots(request):
	lotteries = Lottery.objects.all().order_by('-jackpot')
	context = {
		'lotteries' : lotteries
	}
	return render(request, 'highest_jackpots.html', context)




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
	lotteries = Lottery.objects.all()
	context = {
		'winners': winners,
		'lottery_images': lottery_images,
		'lotteries': lotteries
	}
	return render(request, 'winner_page.html', context)

def faq_questions(request):
	winners = Winner.objects.all()[:3]
	context = {
		'winners':winners
	}
	return render(request, 'faq.html', context)