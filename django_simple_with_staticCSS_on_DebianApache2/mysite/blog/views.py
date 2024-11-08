from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  #return HttpResponse("Congratulations....You're inside blog app....")
  context = {"app": 'blog'}
  return render(request, "blog/index.html", context=context)