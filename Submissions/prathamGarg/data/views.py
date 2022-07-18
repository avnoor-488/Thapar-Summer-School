from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import userData
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import random as r
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def combo(d_path,low1,high1):
    print("entring combo")
    fp=open(d_path)
    D={}
    x=0
    for line in fp:
        if x==0:
            x=1
            continue
        l=line.split(',')
        D[l[0]]=int(l[1].strip())
    result=set()
    setlb=2       # least elements in a combo
    setub=len(D)      # max items in a combo
    loops=6000   
    low=int(low1)           # lower bound of cost
    high=int(high1)         # upper bound of cost
    # print(low,high)
    for i in range(loops):
        SetSize=r.randint(setlb,setub)    
        x=r.sample(list(D.values()),SetSize) # using list 'coz we need a sequence or set
        x.sort()
        chromosome=tuple(x)    
        if sum(chromosome) in range(low, high + 1): # if the selected products fall in range
            l=[]                                 # creating alist to store product names
            for i in chromosome:                 # this takes each price and finds corresponding product
                k=[key for key, value in D.items() if value == i][0] # list comprehension used to extract
                                                                    #  keys using given value
                l.append(k)
            l=tuple(l) # list is not hashable so we need to convert list into tuple
            result.add(l)	
    return result




def email_sender(result, email):
    print(email)
    message = "ComboFinder:\nHere are your best Combinations\n"+str(result).replace('\'','')
    subject = "ComboFinder"
    send_mail(subject,
    message,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False)
    print(settings.EMAIL_HOST_USER)


def data_process(doc,upper_limit,lower_limit,email):
    # print(doc)
    context={'done':"File  UplOaded"}
    fs = FileSystemStorage()
    if os.path.exists(settings.MEDIA_ROOT+'/'+doc.name):#deletes pre existing file with same name
        os.remove(settings.MEDIA_ROOT+'/'+doc.name)
    fs.save(doc.name,doc)
    result=combo(settings.MEDIA_ROOT+'/'+doc.name,lower_limit,upper_limit)
    print(result)
    if len(result)==0:
        print("result is zero")
        context['result']=99
    else:
        print("result is not zero")	
        context['result']= result
        email_sender(result,email)
        print("email sent")
    return context



def input_doc(request):
    if request.method == "POST":
        email = request.POST['email']
        upper_limit = request.POST['upper_limit']
        lower_limit = request.POST['lower_limit']
        doc = request.FILES['doc']# get the uploaded file
        if not doc.name.endswith('.csv'):
            messages.error(request,"Upload only csv file")
            # message.errors()
            print("Your file must be a CSV type")
            return redirect('input_doc')
        else :            
            user = userData.objects.create(email=email,lower_limit=lower_limit,upper_limit=upper_limit,doc=doc)
            user.save()
            context = data_process(doc,upper_limit,lower_limit,email)
            print("data processed")
            return render(request,'thankyou.html',context)
    return render(request,'index.html',{}) #add here

