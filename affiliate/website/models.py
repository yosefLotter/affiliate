from django.db import models



# For Lottery Page the content
class Lottery(models.Model):
	name_of_lottery = models.CharField(max_length=100)
	continent = models.CharField(max_length=100)
	jackpot = models.CharField(max_length=40)
	odds = models.CharField(max_length=100)
	dragnings_datum = models.CharField(max_length=400)
	intro_content = models.TextField(max_length=500, blank=True)
	logo = models.ImageField(default=None, blank=True)
	flaga = models.ImageField(default=None, blank=True)


	def __str__(self):
		return '{},{},{},{},{}'.format(
			self.name_of_lottery,
			self.continent,
			self.jackpot,
			self.odds,
			self.dragnings_datum,
		)


# Each Lottery has 3 Pictures in a Image-Libaray
class Lottery_image(models.Model):
	lottery = models.ForeignKey(Lottery, on_delete=models.CASCADE)
	rektangel = models.ImageField(default=None, blank=True)
	kvadrat = models.ImageField(default=None, blank=True)
	spare = models.ImageField(default=None, blank=True)

	def __str__(self):
		return '{},{},{}'.format(
			self.rektangel,
			self.kvadrat,
			self.spare,
		)





#{{ content.lottery.flaga.url
# Each Lottery has it own Lottery page with Articles.
class Article(models.Model):
	name_of_article = models.CharField(max_length=200)
	lottery = models.ForeignKey(Lottery, on_delete=models.CASCADE)
	welcome_text = models.TextField(blank=True)

	
	a_first_title = models.CharField(max_length=300, blank=True)
	a_top_big_content = models.TextField(blank=True)
	a_content_image_right = models.ImageField(default=None, blank=True)

	a_first_small_title = models.CharField(max_length=300, blank=True)
	a_first_small_content = models.TextField(blank=True)

	a_second_small_title = models.CharField(max_length=300, blank=True)
	a_second_small_content = models.TextField(blank=True)

# For middle part of the website.
	b_second_title = models.CharField(max_length=300, blank=True)
	b_top_big_content = models.TextField(blank=True)
	b_content_image_left = models.ImageField(default=None, blank=True)

	b_first_small_title = models.CharField(max_length=300, blank=True)
	b_first_small_content = models.TextField(blank=True)

	b_second_small_title = models.CharField(max_length=300, blank=True)
	b_second_small_content = models.TextField(blank=True)

# For Lower Part of the website Article page.
	c_second_title = models.CharField(max_length=300, blank=True)
	c_down_big_content = models.TextField(blank=True)
	c_content_image_right = models.ImageField(default=None, blank=True)

	c_first_small_title = models.CharField(max_length=300, blank=True)
	c_first_small_content = models.TextField(blank=True)

	c_second_small_title = models.CharField(max_length=300, blank=True)
	c_second_small_content = models.TextField(blank=True)

# Extra 
	d_second_title = models.CharField(max_length=300, blank=True)
	d_down_big_content = models.TextField(blank=True)
	d_content_image_left = models.ImageField(default=None, blank=True)

	d_first_small_title = models.CharField(max_length=300, blank=True)
	d_first_small_content = models.TextField(blank=True)

	d_second_small_title = models.CharField(max_length=300, blank=True)
	d_second_small_content = models.TextField(blank=True)

	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{}'.format(
			self.lottery.name_of_lottery,
		)




# For Winner Page
class Winner(models.Model):
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
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{},{}'.format(
			self.lottery,
			self.welcome_title,
		)


# For the First Page
class First_page(models.Model):
	welcome_title = models.CharField(max_length=100, blank=True)
	welcome_content = models.TextField(blank=True)
	title = models.CharField(max_length=100, blank=True)
	content = models.TextField(blank=True)
	def __str__(self):
		return '{}'.format(
			self.welcome_title
		)
