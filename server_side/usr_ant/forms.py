from django import forms

class UserInfo(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 20, widget=forms.PasswordInput)
    email = forms.EmailField()
    url = forms.URLField()

class Userlogin(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 20, widget=forms.PasswordInput)
