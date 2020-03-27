from django.shortcuts import render
from .forms import URLinputform
from django.http import HttpResponse
from .models import Database
#from django.contrib.auth.decorators import login_required

def home(request):  
    shortcode=''
    msg=''
    url=''
    form=URLinputform()
    if request.method == 'POST':
        form=URLinputform(request.POST)
        if form.is_valid():
            url=form.cleaned_data['url']
            obj,created=Database.objects.get_or_create(url=url,user=request.user)
            if not created:
                msg='URL Already exists!'
            else:
                msg='URL shortened:'
                obj.user=request.user
                obj.save()
            shortcode=obj.shortcode
           
    else:
        form=URLinputform()
    return render(request,'main/home.html',{"form":form,"msg":msg,"shortcode":shortcode,"url":url})

#@login_required
def showURLs(request):
    urls=Database.objects.all().filter(user=request.user)
    return render(request,'main/shortcode.html',{"urls":urls})

