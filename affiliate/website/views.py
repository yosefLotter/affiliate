from django.shortcuts import render, redirect

from .models import  Lottery, Winner, Customer, Tabell
# Create your views here.



def extra_lottery_page(request):
	return render(request, 'extra_lottery_page.html')

def index(request):
	mini_list_lotteries = Lottery.objects.all()[:4]
	winner = Winner.objects.all().last()
	context = {
		'mini_list_lotteries': mini_list_lotteries,
		#'winner': winner,
	}
	return render(request, 'index.html', context)

# Europa sida
def europe(request):
	europe_list = Lottery.objects.filter(continent='Europa')
	context = {
		'europe_list': europe_list,
	}
	return render(request, 'europe_list.html', context)

def asien(request):
	asien_list = Lottery.objects.filter(continent='Asien')
	context = {
		'asien_list':asien_list,
	}
	return render(request, 'asien_list.html', context)


def sydamerika(request):
	sydamerika_list = Lottery.objects.filter(continent='Sydamerika')
	context = {
		'sydamerika_list': sydamerika_list,
	}
	return render(request, 'sydamerika_list.html', context)



def amerika(request):
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



def lottery_detail(request, slug):
	lottery = Lottery.objects.get(slug=slug)
	winners = Winner.objects.filter(lottery_id=lottery.id)
	context = {
		'lottery': lottery,
		'winners': winners,
	}
	return render(request, 'lottery_page.html', context)


def winner_page(request, slug):
	winner = Winner.objects.get(slug=slug)
	mini_list_lotteries = Lottery.objects.all()[:5]
	context = {
	 	'winner': winner,
	 	'mini_list_lotteries': mini_list_lotteries
	}
	return render(request, 'winner_page.html', context)

def faq_questions(request):
	winners = Winner.objects.all()[:3]
	mini_list_lotteries = Lottery.objects.all()[:5]
	context = {
		'winners':winners,
		'mini_list_lotteries':mini_list_lotteries
	}
	return render(request, 'faq.html', context)