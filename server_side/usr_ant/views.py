from django.shortcuts import render
from .forms import UserInfo
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Peer
import json
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
            #saving the new peer
            usr = User.objects.create_user(name, email, password)
            p = Peer()
            p.user = usr;
            p.url = form.cleaned_data['url']
            p.save()
            #giving the client a response
            peernamelist = {}
            userlist = User.objects.all()
            plist = Peer.objects.all()
            for individual in plist:
                print individual.user.username
                print individual.url
                peernamelist[individual.user.username] = individual.url
            print plist
            print userlist
            print peernamelist
            return HttpResponse(json.dumps(peernamelist), content_type="application/json")
    else:
        form = UserInfo()
    return render(request, 'simpleform.html', {'form': form})
