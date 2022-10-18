import email
import imp
from unicodedata import name
from django.shortcuts import render, HttpResponse
from matplotlib.style import context
from datetime import datetime
from home.models import Contact, Rating
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse("this is home page")
    context = {
        "variable1":"Learning Django",
        "variable2":"Fastly"
    }
    # messages.success(request, "Welcome! to my web page")
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is service page")

def chat_with_us(request):
    return render(request, 'chatwithus.html')

def register_a_complaint(request):
    return render(request,'registeracomplaint.html')    


def rating(request):
    if request.method == "POST":
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        
        rating = Rating(name=name, rating=rating)
        rating.save();
        messages.success(request, 'Thanks! for your valuable rating')
        
    return render(request,'rating.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        #Creating an object
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save(); # storing into database
        messages.success(request, 'Your message has been sent!')
        
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")
