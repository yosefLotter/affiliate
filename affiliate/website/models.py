from django.db import models

from django_bleach.models import BleachField
from django.utils.importlib import import_module

# For Lottery Page the content
class Lottery(models.Model):
	slug = models.SlugField(unique=True)
	name_of_lottery = models.CharField(max_length=100)
	continent = models.CharField(max_length=100)
	jackpot = models.CharField(max_length=40, blank=True)
	odds = models.CharField(max_length=100, blank=True)
	dragnings_datum = models.CharField(max_length=400)
	pris_biljett = models.CharField(max_length=100, blank=True)
	intro_content = models.TextField(max_length=500, blank=True)
	logo = models.ImageField(default=None, blank=True)

	mini_content = models.CharField(max_length=100, blank=True)
	welcome_text = BleachField(blank=True)

	a_title = models.CharField(max_length=200, blank=True)
	a_content = BleachField(blank=True)
	a_content_image_right = models.ImageField(default=None, blank=True)

	b_title = models.CharField(max_length=200, blank=True)
	b_content = BleachField(blank=True)
	b_image = models.ImageField(default=None, blank=True)
	
	c_title = models.CharField(max_length=200, blank=True)
	c_content = BleachField(blank=True)

	d_title = models.CharField(max_length=200, blank=True)
	d_content = BleachField(blank=True)

	e_title = models.CharField(max_length=200, blank=True)
	e_content = BleachField(blank=True)

	f_title = models.CharField(max_length=200, blank=True)
	f_content = BleachField(blank=True)

	g_title = models.CharField(max_length=200, blank=True)
	g_content = BleachField(blank=True)

	h_title = models.CharField(max_length=200, blank=True)
	h_content = BleachField(blank=True)

	i_title = models.CharField(max_length=200, blank=True)
	i_content = BleachField(blank=True)


	j_title = models.CharField(max_length=200, blank=True)
	j_content = BleachField(blank=True)

	k_title = models.CharField(max_length=200, blank=True)
	k_content = BleachField(blank=True)

	l_title = models.CharField(max_length=200, blank=True)
	l_content = BleachField(blank=True)



	def __str__(self):
		return '{},{}'.format(
			self.name_of_lottery,
			self.continent,
		)



# For Winner Page
class Winner(models.Model):
	slug = models.SlugField(unique=True)
	lottery = models.ForeignKey(Lottery, on_delete=models.CASCADE)
	amount_they_won = models.CharField(max_length=400, blank=True)
	profil_bild = models.ImageField(default=None, blank=True)

	welcome_title = models.CharField(max_length=100, blank=True)
	welcome_text = models.TextField(blank=True)

	a_title = models.CharField(max_length=200, blank=True)
	a_content = models.TextField(blank=True)

	b_title = models.CharField(max_length=200, blank=True)
	b_content = models.TextField(blank=True)
	b_image = models.ImageField(default=None, blank=True)
	
	c_title = models.CharField(max_length=200, blank=True)
	c_content = models.TextField(blank=True)

	d_title = models.CharField(max_length=200, blank=True)
	d_content = models.TextField(blank=True)

	e_title = models.CharField(max_length=200, blank=True)
	e_content = models.TextField(blank=True)

	bild = models.ImageField(default=None, blank=True)
	youtube_link = models.CharField(max_length=1000, blank=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{},{}'.format(
			self.lottery,
			self.welcome_title,
		)


class Customer(models.Model):
	name = models.CharField(max_length=100)
	email_adress = models.CharField(max_length=200, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{},{},{}'.format(
			self.name,
			self.email_adress,
			self.date_created,
		)


