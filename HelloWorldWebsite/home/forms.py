# forms.py 
from django import forms 
from .models import *

class ImageForm(forms.ModelForm): 

	class Meta: 
		model = Dummy 
		fields = ['name', 'dummy_img'] 
