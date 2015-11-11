from django import forms

class UserInfo(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 20, widget=forms.PasswordInput)
    email = forms.EmailField(required = False)
    url = forms.URLField(required = False)
    group = forms.CharField(max_length = 32, label='Your Group', required = False)
    ip_addr = forms.GenericIPAddressField(label = 'Your IP Address')
    port = forms.IntegerField()

class Userlogin(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 20, widget=forms.PasswordInput)

class GroupChange(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 20, widget=forms.PasswordInput)
    group = forms.CharField(max_length = 32, label='Your dream group', required = False)
