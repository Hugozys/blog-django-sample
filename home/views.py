from django.shortcuts import render

from django.http import HttpResponse 
# Create your views here.

def home(request):
    user=request.user
    context={"user":user}
    return render(request, 'home/home.html',context)


def about(request):
    return render(request, 'home/about.html')


def joinme(request):
    return render(request, 'home/joinme.html')


