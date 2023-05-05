from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password= "root",
    db = "airline",
)
# Create your views here.
def index(response, id):
    pass
    #ls = customer.objects.all()
    #return HttpResponse("<h1>%s</h1>" % (ls.first_name, %ls.last_name)

def home(response):
    return render(response, 'airline/home.html')

def login(request):
    if request.user.is_authenticated:
        return render(request)
    else:
        messages.info(request, "Please login to continue")
        return HttpResponseRedirect('/')
    def 