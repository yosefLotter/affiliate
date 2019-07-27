from django.shortcuts import render, redirect

from .models import  Lottery, Winner, Contact_us, Mini_lottery_list, Montly_subscribes, Meta_tags_for_lottery, Lottery_supplier, Article_links, Meta_tags_for_winner, Loser

from .forms import ContactForm, Subscribers
# For Flash Messages
from django.contrib import messages
# To send Email to my Outlook Account.
from django.core.mail import send_mail



def index(request):
    article_links = Article_links.objects.all()
    lottery_supplier = Lottery_supplier.objects.all()
    mini_list_lotteries = Lottery.objects.all()[:4]
    winners = Winner.objects.all()[:1]
    context = {
        'article_links': article_links,
        'lottery_supplier': lottery_supplier,
        'mini_list_lotteries': mini_list_lotteries,
        'winners': winners,
    }
    return render(request, 'index.html', context)

# Europa sida
def europe(request):
    europe_list = Lottery.objects.filter(continent='Europa')
    print(europe_list)
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
    print(sydamerika_list)
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


def highest_jackpots(request):
    lotteries = Lottery.objects.all().order_by('-jackpot')
    context = {
        'lotteries' : lotteries
    }
    return render(request, 'highest_jackpots.html', context)


def lottery_detail(request, slug):
    lottery = Lottery.objects.get(slug=slug)
    article_links = Article_links.objects.all()
    lottery_supplier = Lottery_supplier.objects.filter(id=lottery.id)
    meta_tags = Meta_tags_for_lottery.objects.filter(lottery_id=lottery.id)
    winners_of_that_lottery = Winner.objects.filter(lottery_id=lottery.id)[:1]
    mini_list_lotteries = Lottery.objects.all()[:4]
    winner = Winner.objects.filter().last()
    context = {
        'article_links': article_links,
        'lottery_supplier': lottery_supplier,
        'meta_tags': meta_tags,
        'lottery': lottery,
        'winners_of_that_lottery': winners_of_that_lottery,
        'mini_list_lotteries': mini_list_lotteries,
        'winner': winner,
    }
    return render(request, 'lottery_page.html', context)


def winner_page(request, slug):
    winner = Winner.objects.get(slug=slug)
    meta_tags = Meta_tags_for_winner.objects.get(winner_id=winner.id)
    article_links = Article_links.objects.all()
    mini_list_lotteries = Lottery.objects.all()[:5]
    context = {
        'meta_tags': meta_tags,
        'winner': winner,
        'article_links': article_links,
        'mini_list_lotteries': mini_list_lotteries
    }
    return render(request, 'winner_page.html', context)

def loser_page(request, slug):
    loser = Loser.objects.get(slug=slug)
    print(loser)
    article_links = Article_links.objects.all()
    mini_list_lotteries = Lottery.objects.all()[:5]
    context = {
        'loser':loser,
        'article_links': article_links,
        'mini_list_lotteries': mini_list_lotteries
    }
    return render(request, 'loser.html', context)





def faq_questions(request):
    article_links = Article_links.objects.all()
    winners = Winner.objects.all()[:1]
    mini_list_lotteries = Lottery.objects.all()[:4]
    context = {
        'article_links': article_links,
        'winners':winners,
        'mini_list_lotteries':mini_list_lotteries
    }
    return render(request, 'faq.html', context)



def contact_page(request):
    article_links = Article_links.objects.all()
    mini_list_lotteries = Lottery.objects.all()[:4]
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            send_mail('Customer Contacted us {} '.format(form.email_adress),
            form.text,
            # Yosef is the email it sends from.
            'yosef.lotter@outlook.com',
            # Yossi is the Reciver can add more Recivers if its needed.
            ['yossi.kayhko@gmail.com'],
            fail_silently=True)
            form.save()
            messages.add_message(request, messages.SUCCESS, 'We will be in touch {}'.format(form.namn))
            return redirect('website:contact_page')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
        context = {
            'form': form,
            'article_links': article_links,
            'mini_list_lotteries': mini_list_lotteries,
        }
    return render(request, 'contact_page.html', context)


def spela_ansvarsfullt(request):
    return render(request, 'spela_ansvarfullt.html')


def all_article_page(request):
    article_links = Article_links.objects.all()
    lottery_supplier = Lottery_supplier.objects.all()
    form = Subscribers()
    if request.method == 'POST':
        form = Subscribers(request.POST)
        if form.is_valid():
            Montly_subscriber = form.save()
            return redirect('website:all_article_page')
    winners = Winner.objects.all()
    context = {
        'form':form,
        'article_links': article_links,
        'lottery_supplier': lottery_supplier,
        'winners': winners,
    }
    return render(request, 'all_article_page.html', context)

def utbetalning(request):
    article_links = Article_links.objects.all()
    lottery_supplier = Lottery_supplier.objects.all()
    mini_list_lotteries = Mini_lottery_list.objects.all()[:3]
    winners = Winner.objects.all()[:1]
    context = {
        'article_links': article_links,
        'lottery_supplier': lottery_supplier,
        'mini_list_lotteries': mini_list_lotteries,
        'winners': winners,
    }
    return render(request, 'utbetalning.html', context)