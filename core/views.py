from django.shortcuts import render,HttpResponse
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

        prayerdata=Prayer(pname=pname,pemail=pemail,pphone=pphone,pmessage=pmessage)
        prayerdata.save()

    return render(request,'prayer.html')


def contact(request):

    if request.method=="POST":
        name=request.POST["fullname"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        subject=request.POST['subject']
        message=request.POST["message"]

        contact=Contact(name=name,email=email,phone=phone,subject=subject,message=message)
        contact.save()

        print(name)
        print(email)
        print(phone)
        print(subject)
        print(message)
    return render(request,'contact.html')


def location(request):
    return render(request,'location.html')


