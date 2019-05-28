from django.db import models

# Create your models here.

class Winner(models.Model):
	lottery = models.CharField(max_length=500)
	first_title = models.CharField(max_length=500, blank=True)
	first_content = models.TextField(blank=True)
	second_title = models.CharField(max_length=500, blank=True)
	second_content = models.TextField(blank=True)
	third_title = models.CharField(max_length=500, blank=True)
	third_content = models.TextField(blank=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{},{}'.format(self.lottery, self.first_title)

	def snippet(self):
		return self.first_content[:100]



# Full Test here! DELETE Maybe

class Lottery(models.Model):
	name_of_lottery = models.CharField(max_length=100)
	first_content = models.TextField(blank=True)
	second_title = models.CharField(max_length=100, blank=True)
	second_content = models.TextField(blank=True)
	third_title = models.CharField(max_length=500, blank=True)
	third_content = models.TextField(blank=True)
	right_side_content_first = models.TextField(blank=True)
	right_side_content_second = models.TextField(blank=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{},{},{},{},{},{},{},{}'.format(
			self.name_of_lottery,
			self.first_content,
			self.second_title,
			self.second_content,
			self.third_title,
			self.third_content,
			self.right_side_content_first,
			self.right_side_content_second,
		)










# For Best lottery page html 
class Best_lottery(models.Model):
	lottery = models.ForeignKey(Lottery, on_delete=models.CASCADE)
	name_of_lottery = models.CharField(max_length=100, blank=True)
	logo = models.ImageField(default=None)
	winning_amount = models.CharField(max_length=100, blank=True)
	dragnings_datum = models.CharField(max_length=100, blank=True)
	odds = models.CharField(max_length=100, blank=True)
	price_range = models.CharField(max_length=100, blank=True)
	flaga = models.ImageField(default=None, blank=True)
	content = models.TextField(max_length=400)

	def __str__(self):
		return '{},{},{},{},{},{}'.format(
			self.name_of_lottery,
			self.logo,
			self.winning_amount,
			self.dragnings_datum,
			self.odds,
			self.price_range,
			self.flaga,
			self.content,
			)