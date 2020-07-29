from django.forms import ModelForm
from myapp.models import Usregister
from django import forms

class UsForm(ModelForm):
	class Meta:
		model = Usregister
		fields="__all__"
		widgets = {
		"uname":forms.TextInput(attrs={
			"class":"form-control col-md-3",
			"placeholder":"Enterusername"
		}),
		}
