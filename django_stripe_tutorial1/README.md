# django_stripe_tutorial
 I am using python3.12 in  virtual env.
 1) 'python -m pip install django' , 'python -m pip install stripe==7.10.0',
    "python -m pip install python-decouple==3.8"

1) PS C:\Users\hi\Desktop\projects\python_projects\django_stripe_tutorial> django-admin.exe startproject django_stripe_project

2) PS C:\Users\hi\Desktop\projects\python_projects\django_stripe_tutorial\django_stripe_project> cd .\django_stripe_project\; python manage.py startapp products

3) Goto 'https://dashboard.stripe.com/register' and register for stripe account

4) Goto https://dashboard.stripe.com/test/dashboard and click 'Developers' Make sure you are in 'Test mode'
   
   Copy STRIPE_PUBLIC_KEY = "<your_test_public_api_key>", STRIPE_SECRET_KEY = "<your_test_secret_api_key>" in settings.py .You copy and paste these keys here

5) On LHS, click '...More" and choose 'Product Catalogue'

6) Click the "+ Add product" button in the upper right-hand corner to create a product to sell. The required fields are name, 'recurring' or 'one-off' , and the amount. We are processing a 'one-off' payment here. 'amount'=10.00. Click the "Add Product" button.
   
7) Click on the new product to open up its page. Under the Pricing section, note the "API ID" which we will use shortly.
   
   USE credit card number=4000 0035 6000 0008. (DO NOT USE credit card number= 4242 4242 4242 4242). See https://docs.stripe.com/testing#international-cards
   Enter whatever expiry date, CVC and Name.