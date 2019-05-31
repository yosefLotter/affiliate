from django.shortcuts import render, redirect

from .models import Winner, Lottery, Article
# Create your views here.


def index(request):
	return render(request, 'index.html')

# For Best_lottery Page
def best_lottery(request):
	# Testa här lite
	articles = Article.objects.all()
	print(articles)
	context = {
		'articles' : articles
	}

	return render(request, 'best_lottery.html', context)
# Test for lottery page.

def lottery_page(request, lottery_id):
	lottery = Article.objects.filter(lottery_id=lottery_id)
	print(lottery)
	context = {
		'lottery': lottery
	}
	return render(request, 'lottery_page.html', context)






def winners(request):
	winners = Winner.objects.all()
	context = {
		'winners': winners
	}
	return render(request, 'winner.html', context)

def winner_article(request, article_id):
	winner = Winner.objects.get(pk=article_id)
	context = {
		'winner': winner
	}
	return render(request, 'winner.html', context)




