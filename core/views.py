from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from core.models import Contact
from core.models import Prayer

# Create your views here.
def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')



def watch(request):
    return render(request,'watch.html')


def prayer(request):
    if request.method=="POST":

        pname=request.POST["fullname"]
        pemail=request.POST["email"]
        pphone=request.POST["phone"]
        pmessage=request.POST["message"]

        if pname!="" and pemail!="" and pphone!=""  and pmessage!="":


            prayerdata=Prayer(pname=pname,pemail=pemail,pphone=pphone,pmessage=pmessage)
            prayerdata.save()

            messages.info(request,'Your details are successfully submitted')
            return redirect('prayer')


               
        else:
            messages.info(request,'All fields are required')
            return redirect('prayer')

    return render(request,'prayer.html')


def contact(request):

    if request.method=="POST":
        name=request.POST["fullname"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        subject=request.POST['subject']
        message=request.POST["message"]

        if name!="" and email!="" and phone!=""  and subject!="" and message!="":
             
            
             

             contactdata=Contact(name=name,email=email,phone=phone,subject=subject,message=message)
             contactdata.save()
             
             messages.info(request,'Your details are successfully submitted')
             return redirect('contact')
             
             
        else:
            messages.info(request,'All fields are required')
            return redirect('contact')

       

        print(name)
        print(email)
        print(phone)
        print(subject)
        print(message)
    else:
         return render(request,'contact.html')
   


def location(request):
    return render(request,'location.html')


