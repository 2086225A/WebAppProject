from django import forms
from django.contrib.auth.models import User
from kinkyCuts.models import UserProfile

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=50)
	file = forms.FileField()

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('profilepic',)