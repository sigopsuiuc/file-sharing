from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse
from .forms import UploadFileForm, NameForm

#this decorator is harmful in an aspect of security
#TODO: look for a way to get post requests with csrf token
#@csrf_exempt
def upload_file(request):
    print("entered")
    if request.method == 'POST':
        print('post request received!')
        form = NameForm(request.POST)
        if form.is_valid():
            print('valid form received')
            return HttpResponse('valid!')
    else:
        form = NameForm()
    return render(request, 'list.html', {'form': form})
# return HttpResponse("Hello, this is upload_file")
