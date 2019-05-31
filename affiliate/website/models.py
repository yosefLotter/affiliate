from django.db import models



# For Lottery Page the content
class Lottery(models.Model):
	name_of_lottery = models.CharField(max_length=100)
	jackpot = models.CharField(max_length=40)
	odds = models.CharField(max_length=100)
	dragnings_datum = models.CharField(max_length=400)
	intro_content = models.TextField(max_length=500, blank=True)
	price_range = models.CharField(max_length=50)
	logo = models.ImageField(default=None, blank=True)
	flaga = models.ImageField(default=None, blank=True)

	def __str__(self):
		return '{},{},{},{},{}'.format(
			self.name_of_lottery,
			self.jackpot,
			self.odds,
			self.dragnings_datum,
			self.price_range,
			)


class Article(models.Model):
	lottery = models.ForeignKey(Lottery, on_delete=models.CASCADE)

	first_title = models.CharField(max_length=100, blank=True)
	first_content = models.TextField(blank=True)
	first_image = models.ImageField(default=None, blank=True)

	second_title = models.CharField(max_length=100, blank=True)
	second_content = models.TextField(blank=True)
	second_image = models.ImageField(default=None, blank=True)

	third_title = models.CharField(max_length=500, blank=True)
	third_content = models.TextField(blank=True)
	third_image = models.ImageField(default=None, blank=True)

	fourth_title = models.CharField(max_length=100, blank=True)
	fourth_content = models.TextField(blank=True)
	fourt_image = models.ImageField(default=None, blank=True)

	fith_title = models.CharField(max_length=100, blank=True)
	fith_content = models.TextField(blank=True)
	fifth_image = models.ImageField(default=None, blank=True)

	six_title = models.CharField(max_length=500, blank=True)
	six_content = models.TextField(blank=True)

	seven_title = models.CharField(max_length=500, blank=True)
	seven_content = models.TextField(blank=True)

	eight_title = models.CharField(max_length=500, blank=True)
	eight_content = models.TextField(blank=True)

	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{},{},{},{},{}'.format(
			self.lottery,
			self.first_title,
			self.second_title,
			self.third_title,
			self.fourth_title,
			self.date,
		)



# For Winner Page
class Winner(models.Model):
	lottery = models.ForeignKey(Lottery, on_delete=models.CASCADE)
	name_of_lottery = models.CharField(max_length=100)
	amount_they_won = models.CharField(max_length=400, blank=True)
	#intro = models.CharField(max_length=400, blank=True)
	first_title = models.CharField(max_length=500, blank=True)
	first_content = models.TextField(blank=True)
	second_title = models.CharField(max_length=500, blank=True)
	second_content = models.TextField(blank=True)
	third_title = models.CharField(max_length=500, blank=True)
	third_content = models.TextField(blank=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{},{}'.format(self.name_of_lottery, self.first_title)