from django.shortcuts import render
from .forms import UserInfo
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def peerlist(request):
    if request.method == 'POST':
        form = UserInfo(request.POST)
        if form.is_valid():
            print 'valid info'
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            print 'client name is: '+ name
            print 'client password is: '+ password
            print 'client email is: '+ email
            usr = User.objects.create_user(name, email, password)
            usr.save()
            userlist = User.objects.all()
            print userlist
            return HttpResponse('your info is received')
    else:
        form = UserInfo()
    return render(request, 'simpleform.html', {'form': form})
