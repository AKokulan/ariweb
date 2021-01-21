from django.shortcuts import render

def show_home(requests):
    return render(requests,'index.html',{})
# Create your views here.
