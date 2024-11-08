from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from django.contrib import messages

# Create your views here.
base_context = {
    'address': '1111 Mars Rd, Cool Beach, Haryana 122008, India',
    'email': 'do-not-email-me@gmail.com',
    'tel_no': '111-222-4444',
    'company_name' : 'Company Co., Ltd.',
}

extra_context = {
    'home_store_loc' : '1111 Mars Rd, Cool Beach, Haryana 122008, India',
    'home_phone' : '333-999-1234',
    'home_office_loc' : 'New Delhi, India',
    'home_work_hours' : '07:30 AM - 9:30 PM Daily',
    'home_email' : 'home_email@gmail.com',
}
        
class HomeView(View):
    template_name = 'core/index.html'
    
    def get(self, request):#override
        context = {}
        context.update(base_context)
        context.update(extra_context)
                
        return render(request, self.template_name, context)
    
    def post(self, request):#override
        msg = "Subscription added for " + request.POST.get("name") + \
            " ( " + request.POST.get("email") + " )" 
        
        messages.add_message(request, messages.INFO, msg)# works for messages.{INFO,SUCCESS,WARNING)
        return redirect('core:home')        
        
#end class
    
class AboutView(View):
    template_name = 'core/about.html'
    
    def get(self, request):#override
        context = {}
        context.update(base_context)
        context.update(extra_context)
        
        return render(request, self.template_name, context)

    def post(self, request):#override
        msg = "Subscription added for " + request.POST.get("name") + \
            " ( " + request.POST.get("email") + " )" 
        
        messages.add_message(request, messages.INFO, msg)
        return redirect('core:about')        
    
#end class

class ProductsView(View):
    template_name = 'core/products.html'
    
    def get(self, request):#override
        context = {}
        context.update(base_context)
        context.update(extra_context)
        
        return render(request, self.template_name, context)
    
#end class

class SingleProductView(View):
    template_name = 'core/single-product.html'
    
    def get(self, request):#override
        context = {}
        context.update(base_context)
        item, price = "New Green Jacket", '10.99'
        total_price = price
        context = {
            'item': item,
            'price': price,
            'total_price': total_price,
        }
        
        return render(request, self.template_name, context)

    def post(self, request):#override
        msg = "POST data: quantity=" + request.POST.get("quantity") \
            + "; price=" + request.POST.get("price") \
            + "; total_price=" + request.POST.get("total_price") 
        return HttpResponse(msg)        

    
#end class

class ContactView(View):
    template_name = 'core/contact.html'
    
    def get(self, request):#override
        context = {}
        context.update(base_context)
        context.update(extra_context)
        
        return render(request, self.template_name, context)
    
    def post(self, request):#override
        msg = "Subscription added for " + request.POST.get("name") + \
            " ( " + request.POST.get("email") + " )" 
        
        messages.add_message(request, messages.INFO, msg)
        return redirect('core:contact')        

    
#end class
