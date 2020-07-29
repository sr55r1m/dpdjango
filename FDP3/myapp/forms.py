from django.forms import ModelForm
from myapp.models import Usregister
from django import forms

class UsForm(ModelForm):
	class Meta:
		model = Usregister
		#fields="__all__"
		fields = ["uname"]
		widgets = {
		"uname":forms.TextInput(attrs={
			"class":"form-control col-md-7",
			"placeholder":"Enter username",
			"required":True}),
		}
