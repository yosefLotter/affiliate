from django.db import models

# Create your models here.

class Winner(models.Model):
	lottery = models.CharField(max_length=100)
	first_title = models.CharField(max_length=100, blank=True)
	first_content = models.TextField(blank=True)
	second_title = models.CharField(max_length=100, blank=True)
	second_content = models.TextField(blank=True)
	third_title = models.CharField(max_length=100, blank=True)
	third_content = models.TextField(blank=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{},{}'.format(self.lottery, self.first_title)

	def snippet(self):
		return self.first_content[:100]