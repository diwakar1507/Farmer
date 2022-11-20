import requests
from django.conf import settings
from Tractor.models import Contact
from django.contrib import messages
from django.shortcuts import render,redirect,HttpResponse
# Create your views here.
def home(request):
     if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        tractor=request.POST.get('tractor')
        details=request.POST.get('details')
        contact=Contact(name=name,email=email,mobile=mobile,tractor=tractor,details=details)
        contact.save()
        messages.success(request, 'Contact request submitted successfully.')
     return render(request,'home.html')

def details(request):
     mydata = Contact.objects.all().values()
     context = {
           'mymembers': mydata,
            }
     return render(request,'details.html',context)
