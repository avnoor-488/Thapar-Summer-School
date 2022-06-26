from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from .models import userData
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os



path = settings.MEDIA_ROOT+'/outputs/'



def email_sender(email):
    print(email)
    print(settings.EMAIL_HOST_USER)
    message = "Text Converter:\nHere is your converted file Attached in the mail\n"    
    subject = "Output File"
    email = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
    )
    email.attach_file(path+'output.txt')
    email.send()
    print("email sended")


def data_process(doc,email):
    print(doc)
    fs = FileSystemStorage()
    if os.path.exists(settings.MEDIA_ROOT+'/'+doc.name):
        os.remove(settings.MEDIA_ROOT+'/'+doc.name)
    fs.save(doc.name,doc)
    fo = open(settings.MEDIA_ROOT+'/'+doc.name, 'r')
    for x in fo.read():
        y = x.lower()
        fo1 = open(path+'output.txt', 'a')
        fo1.write(y)
    email_sender(email)


def input(request):
    if request.method == "POST":
        email = request.POST['email']
        doc = request.FILES['doc']# get the uploaded file
        if not doc.name.endswith('.txt'):
            messages.error(request,"Upload only txt file")
            print("Your file must be a TXT type")
            return redirect('input')
        else :            
            user = userData.objects.create(email=email,doc=doc)
            user.save()
            data_process(doc,email)
            print("data processed")
            context = {}
            return render(request,'thankyou.html',context)
    return render(request,'index.html',{}) #add here


