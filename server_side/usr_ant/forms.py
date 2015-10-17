from django import forms

class UserInfo(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 20)
    email = forms.EmailField()



