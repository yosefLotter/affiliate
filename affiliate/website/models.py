from django.db import models

from django_bleach.models import BleachField


# For Lottery Page the content
class Lottery(models.Model):
	slug = models.SlugField(unique=True)
	name_of_lottery = models.CharField(max_length=100)
	continent = models.CharField(max_length=100)
	provider = models.CharField(max_length=50, blank=True)
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
	youtube_link = models.TextField(blank=True)
	
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{},{}'.format(
			self.lottery,
			self.welcome_title,
		)


class Mini_lottery_list(models.Model):
	lottery = models.ForeignKey(Lottery, on_delete=models.CASCADE)
	name_of_lottery = models.CharField(max_length=100, blank=True)
	mini_logo = models.ImageField(default=None, blank=True)
	mini_content = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return '{}'.format(
			self.name_of_lottery,
	)

class Contact_us(models.Model):
	namn = models.CharField(max_length=15)
	efternamn = models.CharField(max_length=15, blank=True)
	email_adress = models.CharField(max_length=50, blank=True)
	telefonnummer = models.CharField(max_length=15, blank=True)
	text = models.TextField(blank=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{},{},{}'.format(
			self.namn,
			self.email_adress,
			self.telefonnummer,
			self.date_created,
		)

class Montly_subscribes(models.Model):
	namn = models.CharField(max_length=50, blank=True)
	email_adress = models.CharField(max_length=100, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)


class Lottery_supplier(models.Model):
	Lottery = models.ForeignKey(Lottery, on_delete=models.CASCADE)
	slug = models.SlugField(unique=True)
	logo = models.ImageField(default=None, blank=True)
	content_box_1 = models.TextField(blank=True)
	content_box_2 = models.TextField(blank=True)
	content_box_3 = models.TextField(blank=True)
	content_box_4 = models.TextField(blank=True)
	content_box_5 = models.TextField(blank=True)
	content_box_6 = models.TextField(blank=True)

# A Model That Handle All The Article Links in One Place.
# Only A tags in this model And a SlugField. No Need For a Slug.
# This way You Will Be Able To Shuffle as Well Top First And Last.
class Article_links(models.Model):
	article_1 = models.CharField(max_length=200, blank=True)
	article_2 = models.CharField(max_length=200, blank=True)
	article_3 = models.CharField(max_length=200, blank=True)
	article_4 = models.CharField(max_length=200, blank=True)
	article_5 = models.CharField(max_length=200, blank=True)
	article_6 = models.CharField(max_length=200, blank=True)
	article_7 = models.CharField(max_length=200, blank=True)
	article_8 = models.CharField(max_length=200, blank=True)
	article_9 = models.CharField(max_length=200, blank=True)
	article_10 = models.CharField(max_length=200, blank=True)