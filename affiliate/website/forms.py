from django import forms

from .models import Customer


class ContactForm(forms.ModelForm):

	class Meta:
		model = Customer
		fields = ['namn', 'email_adress', 'text']