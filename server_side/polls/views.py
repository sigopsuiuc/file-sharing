from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse
from .forms import UploadFileForm

#this decorator is harmful in an aspect of security
#TODO: look for a way to get post requests with csrf token
@csrf_exempt
def upload_file(request):
    print("entered")
    if request.method == 'POST':
        print('post request received!')
    return HttpResponse("Hello, this is upload_file")
