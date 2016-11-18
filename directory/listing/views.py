from django.shortcuts import render,HttpResponse
from models import article
from models import linkimp
from models import linkmid
from models import link 
from models import contact
from django.core.mail import send_mail
from .forms import articles
from .forms import linkimps
from .forms import linkmids
from .forms import links
from .forms import contacts

# Create your views here.

def index(request):
    if request.method=='POST':
        
        return HttpResponse("hello")
     
    else:   
        g=linkimp(request)  
        return render(request,'listing/index.html',{'g':g})



def artikl(request):
    if request.method=='POST':
        
        o=articles(request.POST)
        o.save() 
        return HttpResponse("Done")
    else:
        o=articles()
        return render (request, 'listing/article.html',{'o':o})

def linkss(request):
    if request.method=='POST':
        ab=request.POST.get('link')
        if ab=='linkimp':
            
            l=linkimps(request.POST)
            l.save()
            return HttpResponse("Thanks for the registration")
        elif ab=='linkmid':
            l=linkmids(request.POST)
            l.save()
            return HttpResponse("Thanks for the registration, We will get back to you asap")
        else:
            l=links(request.POST)
            l.save()
            return HttpResponse("Thanks for the registration, We will get back to you")
        return HttpResponse("Saved")
        
    else:
        l=links()
        return render (request, 'listing/link.html',{'l':l})
def contactss(request):
    
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        print (name,email,message)
        email_subject = 'Message recieved'
        email_body = "%s, thank you for contacting. We will contact you within 24 hrs" %(name)

        send_mail(email_subject, email_body, '',[email], fail_silently=False)

        
        return HttpResponse("Done")
    else:
        f=contact()
        return render(request,'listing/contact.html',{'f':f}) 
