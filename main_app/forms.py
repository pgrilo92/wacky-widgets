from django.forms import ModelForm
from .models import WackyWidget
from django import forms

class WackyWidgetForm(ModelForm):
	class Meta:
		model = WackyWidget
		fields = ['description', 'quantity']