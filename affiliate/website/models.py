from django.db import models



# For Lottery Page the content
class Lottery(models.Model):
	slug = models.SlugField(unique=True)
	name_of_lottery = models.CharField(max_length=100)
	continent = models.CharField(max_length=100)
	jackpot = models.CharField(max_length=40)
	odds = models.CharField(max_length=100)
	dragnings_datum = models.CharField(max_length=400)
	pris_biljett = models.CharField(max_length=100)
	intro_content = models.TextField(max_length=500, blank=True)
	logo = models.ImageField(default=None, blank=True)

	mini_content = models.TextField(blank=True)
	welcome_text = models.TextField(blank=True)

	a_title = models.CharField(max_length=200, blank=True)
	a_content = models.TextField(blank=True)
	a_content_image_right = models.ImageField(default=None, blank=True)

	b_title = models.CharField(max_length=200, blank=True)
	b_content = models.TextField(blank=True)
	b_image = models.ImageField(default=None, blank=True)
	
	c_title = models.CharField(max_length=200, blank=True)
	c_content = models.TextField(blank=True)

	d_title = models.CharField(max_length=200, blank=True)
	d_content = models.TextField(blank=True)

	e_title = models.CharField(max_length=200, blank=True)
	e_content = models.TextField(blank=True)

	f_title = models.CharField(max_length=200, blank=True)
	f_content = models.TextField(blank=True)

	g_title = models.CharField(max_length=200, blank=True)
	g_content = models.TextField(blank=True)

	h_title = models.CharField(max_length=200, blank=True)
	h_content = models.TextField(blank=True)

	k_title = models.CharField(max_length=200, blank=True)
	k_content = models.TextField(blank=True)


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
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{},{}'.format(
			self.lottery,
			self.welcome_title,
		)


class Customer(models.Model):
	name = models.CharField(max_length=100)
	email_adress = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return '{},{}'.format(
			self.name,
			self.email_adress,
		)


class Tabell(models.Model):
	lottery = models.ForeignKey(Lottery, on_delete=models.CASCADE)
	a_Vinstnivå = models.CharField(max_length=100, blank=True) 
	a_vinnarodds = models.CharField(max_length=100, blank=True)
	a_Matchningar = models.CharField(max_length=100, blank=True)

	b_Vinstnivå = models.CharField(max_length=100, blank=True)
	b_Matchningar = models.CharField(max_length=100, blank=True)
	b_vinnarodds = models.CharField(max_length=100, blank=True)

	c_Vinstnivå = models.CharField(max_length=100, blank=True)
	c_Matchningar = models.CharField(max_length=100, blank=True)
	c_vinnarodds = models.CharField(max_length=100, blank=True)
	
	d_Vinstnivå = models.CharField(max_length=100, blank=True)
	d_Matchningar = models.CharField(max_length=100, blank=True)
	d_vinnarodds = models.CharField(max_length=100, blank=True)

	e_Vinstnivå = models.CharField(max_length=100, blank=True)
	e_Matchningar = models.CharField(max_length=100, blank=True)
	e_vinnarodds = models.CharField(max_length=100, blank=True)

	f_Vinstnivå = models.CharField(max_length=100, blank=True)
	f_Matchningar = models.CharField(max_length=100, blank=True)
	f_vinnarodds = models.CharField(max_length=100, blank=True)

	g_Vinstnivå = models.CharField(max_length=100, blank=True)
	g_Matchningar = models.CharField(max_length=100, blank=True)
	g_vinnarodds = models.CharField(max_length=100, blank=True)

	h_Vinstnivå = models.CharField(max_length=100, blank=True)
	h_Matchningar = models.CharField(max_length=100, blank=True)
	h_vinnarodds = models.CharField(max_length=100, blank=True)

	k_Vinstnivå = models.CharField(max_length=100, blank=True)
	k_Matchningar = models.CharField(max_length=100, blank=True)
	k_vinnarodds = models.CharField(max_length=100, blank=True)

	l_Vinstnivå = models.CharField(max_length=100, blank=True)
	l_Matchningar = models.CharField(max_length=100, blank=True)
	l_vinnarodds = models.CharField(max_length=100, blank=True)









	
