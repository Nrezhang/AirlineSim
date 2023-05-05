from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(response, id):
    pass
    #ls = customer.objects.all()
    #return HttpResponse("<h1>%s</h1>" % (ls.first_name, %ls.last_name)

def home(response):
    return render(response, 'airline/home.html')