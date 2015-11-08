from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
import django.contrib.auth.hashers
from .models import Peer , PeerGroup
import json

from userGroupTools.groupmanage import *
# Create your views here.

def peerlist(request):
    if request.method == 'POST':
        form = UserInfo(request.POST)
        if form.is_valid():
            print 'valid info'
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            groupname = form.cleaned_data['group']
            print 'client name is: '+ name
            print 'client password is: '+ password
            print 'client email is: '+ email
            #saving the new peer
            try:
                usr = User.objects.create_user(name, email, password)
            except:
                return HttpResponse('failure: user already exists')
            p = Peer()
            p.user = usr;
            p.url = form.cleaned_data['url']
            p.save()

            login_peer_to_group_with_name(p, groupname)

            #giving the client a response

            response = get_response_for_new_user(groupname)

            return HttpResponse(json.dumps(response), content_type="application/json")
        else:
            msg = 'Message received not valid Please check your entered message\n'
            return HttpResponse(msg)
    else:
        form = UserInfo()
    return render(request, 'signupform.html', {'form': form})




def peerlogin(request):
    if request.method == 'POST':
        form = Userlogin(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                obj = User.objects.get(username = name)
            except:
                return HttpResponse('User does not exist')

            if not obj.check_password(password):
                return HttpResponse('Authentication Failure')


            peer = obj.peer
            response = get_response_for_old_user(peer)

            return HttpResponse(json.dumps(response), content_type="application/json")
    else:
        form = Userlogin()
    return render(request, 'loginform.html', {'form': form})



#TODO: add an view for adding, switching, or exiting a group

def groupmanager(request):
    if request.method == 'POST':
        form = GroupChange(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            groupname = form.cleaned_data['group']

            try:
                obj = User.objects.get(username = name)
            except:
                return HttpResponse('User does not exist')

            if not obj.check_password(password):
                return HttpResponse('Authentication Failure')


            try:
                group = PeerGroup.objects.get(groupname = groupname)
            except:
                return HttpResopnse('Group not found')

            peer = obj.peer

            group.peers.add(peer)
            group.save()

            response = get_response_for_old_user(peer)

            return HttpResponse(json.dumps(response), content_type="application/json")
        else:
            return HttpResopnse('form is not valid')
    else:
        form = GroupChange()
    return render(request, 'groupmanager.html', {'form': form})
