from django.shortcuts import render
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.views import View

#from django.core import mail

class EmailView(View): #sends one email
    
    def get(self, request, *args, **kwargs):#override
        return render(request, 'emailapp/index.html')
    
    def post(self, request, *args, **kwargs):#override
        with get_connection(  
            host=settings.EMAIL_HOST, 
        port=settings.EMAIL_PORT,  
        username=settings.EMAIL_HOST_USER, 
        password=settings.EMAIL_HOST_PASSWORD, 
        use_tls=settings.EMAIL_USE_TLS  
        ) as connection:  
            subject = request.POST.get("subject")  
            email_from = settings.EMAIL_HOST_USER  
            recipient_list = [request.POST.get("email"), ]  
            message = request.POST.get("message")  
            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()  
    
        return render(request, 'emailapp/index.html')

class EmailManyView(View):
    
    def get(self, request, *args, **kwargs):#override
        return render(request, 'emailapp/email_many.html')
    
    def post(self, request, *args, **kwargs):#override
        connection = get_connection( host=settings.EMAIL_HOST,
                                    port=settings.EMAIL_PORT,  
                                    username=settings.EMAIL_HOST_USER, 
                                    password=settings.EMAIL_HOST_PASSWORD, 
                                    use_tls=settings.EMAIL_USE_TLS  
        )
        # Manually open the connection
        connection.open()

        email_from = settings.EMAIL_HOST_USER  
        # Construct an email message that uses the connection
        email1 = EmailMessage(
            "Hello1",
            "Body1 goes here",
            email_from,
            ["ash522.ash622@gmail.com",],#more sender can  be added to the list
        )
        #email1.send()  # Send the email

        # Construct two more messages
        email2 = EmailMessage(
            "Hello2",
            "Body2 goes here",
            email_from,
            ["parikshit.swami@gmail.com",], #more sender can  be added to the list
        )

        # Send the two emails in a single call -
        connection.send_messages([email1, email2])
        # The connection was already open so send_messages() doesn't close it.
        # We need to manually close the connection.
        connection.close()    

        return render(request, 'emailapp/email_many.html')
