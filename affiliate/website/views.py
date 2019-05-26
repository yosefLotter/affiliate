from django.shortcuts import render, redirect

from .models import Winner
# Create your views here.


def index(request):
	winner = Winner.objects.all().order_by('date')[0:1]

	context = {
		'winner': winner
	}
	return render(request, 'index.html', context)


def us_powerball(request):
	winner = Winner.objects.all()[:1].get()
	context = {
		'winner':winner
	}
	return render(request, 'us_powerball.html', context)

def mega_millions(request):
	return render(request,  'mega_millions.html')

def cash4life(request):
	return render(request, 'cash4life.html')

def best_lottery(request):
	return render(request, 'best_lottery.html')

def winners(request):
	winners = Winner.objects.all()
	context = {
		'winners': winners
	}
	return render(request, 'winner.html', context)

def winner_article(request, article_id):
	winner = Winner.objects.get(pk=article_id)
	print(winner)
	context = {
		'winner': winner
	}
	return render(request, 'winner.html', context)