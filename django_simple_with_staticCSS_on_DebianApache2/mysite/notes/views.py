from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  #return HttpResponse("Congratulations....You're inside notes app....")
  context = {"app": 'notes'}
  return render(request, "notes/index.html", context=context)