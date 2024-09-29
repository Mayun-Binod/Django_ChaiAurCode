from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello,World.You are at chai aur django home page.")
    return render(request,'website/index.html')

def about(request):
    # return HttpResponse("Hello,World.You are at chai aur django about page.")
    return render(request,'website/about.html')
def contact(request):
    # return HttpResponse("Hello,World.You are at chai aur django contact page.")    
    return render(request,'website/contact.html')
