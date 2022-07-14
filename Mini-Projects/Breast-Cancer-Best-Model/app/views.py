from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from .models import userData
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import random as r
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pycaret.classification import*
import pandas as pd
from io import StringIO


extension = '.csv'
path = settings.MEDIA_ROOT+'/outputs/'
csvfile = StringIO()


def email_sender(email):
    print(email)
    print(settings.EMAIL_HOST_USER)
    message = "Breast-Cancer:\nHere are your best Model Attached in the mail\n"    
    subject = "Best Model"
    email = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
    )
    email.attach_file(path+'output.csv')
    email.send()
    print("email sended")


def data_process(doc,email):
    print(doc)
    fs = FileSystemStorage()
    if os.path.exists(settings.MEDIA_ROOT+'/'+doc.name):#deletes pre existing file with same name
        os.remove(settings.MEDIA_ROOT+'/'+doc.name)
    fs.save(doc.name,doc)
    data = pd.read_csv(settings.MEDIA_ROOT+'/'+doc.name)
    data=data.drop(['Unnamed: 32'],axis=1)
    clf=setup(data,target='diagnosis',silent=True)
    best = compare_models()
    model = create_model(best)
    tuned_model = tune_model(best) 
    p_model = predict_model(tuned_model)
    dt_result = pull()
    dt_result.to_csv(path+'output.csv')
    email_sender(email)
    os.remove(path+'output.csv')


def input_doc(request):
    if request.method == "POST":
        email = request.POST['email']
        description = request.POST['description']
        doc = request.FILES['doc']# get the uploaded file
        if not doc.name.endswith('.csv'):
            messages.error(request,"Upload only csv file")
            print("Your file must be a CSV type")
            return redirect('input_doc')
        else :            
            user = userData.objects.create(email=email,doc=doc,description=description)
            user.save()
            data_process(doc,email)
            print("data processed")
            context = {}
            return render(request,'thankyou.html',context)
    return render(request,'index.html',{}) #add here


