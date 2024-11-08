from django.shortcuts import render
from django.http import HttpResponse
#from django.views.generic import View

# Create your views here.
context_contact = {'contact_person': 'Pawan Sharma',
               'tel_num': 'Tel # 98 712 63738',
               'addr1': 'Millennium City Centre Road',
               'addr2': 'Wazirabad Dhani, Sector 52',
               'city': 'Gurgaon',
               'state': 'Haryana',
               'biz_tel':'+91 74285 03874',
               'email': 'radheshgypsum@gmail.com',
               'designer': 'Ashwani Kumar ( Email: ash322.ash422@gmail.com )',
               }
def index(request):
    #return HttpResponse("Congratulations....You're inside app....")
    context = {}
    context.update(context_contact)
    return render(request, template_name='appmain/index.html', context=context)

def products(request):
    #return HttpResponse("Congratulations....You're inside app....")
    context = {}
    context.update(context_contact)
    return render(request, template_name='appmain/products.html', context=context)

def contact(request):
    #return HttpResponse("Congratulations....You're inside app....")
    context = {}
    context.update(context_contact)
    return render(request, template_name='appmain/contact.html', context=context)



"""
class NOT_USEDHomeView(View):
    template_name = "appmain/index.html"
#end class
"""