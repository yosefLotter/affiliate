from django import forms

from .models import Contact_us, Montly_subscribes


class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact_us
		fields = ['namn', 'email_adress', 'text']


class Subscribers(forms.ModelForm):

	class Meta:
		model = Montly_subscribes
		fields = ['namn', 'email_adress']