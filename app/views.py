from django.shortcuts import render
from app.models import *

def topic_name(request):
       
        if request.method=='POST':
                tn=request.POST['tn']
                TO=Topic.objects.get_or_create(topic_name=tn)[0]
                TO.save()
                QLTO=Topic.objects.all()
                d={'topics':QLTO}

                return render(request,'display_topic.html',d)
        return render(request,'topic_name.html',)
   

def insert_webpage(request):

    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
            
        tn=request.POST['tn']
        name=request.POST['name']
        email=request.POST['email']
        url=request.POST['url']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,email=email,url=url)[0]
            
        WO.save()
        QLTO=Webpage.objects.all()
        d1={'webpages':QLTO}
        return render(request,'display_webpages.html',d1)

   
    return render(request,'insert_webpage.html',d)


def multiple_webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}

    if request.method=='POST':
        topiclist=request.POST.getlist('tn')
       
        QLWO=Webpage.objects.none()
        for i in topiclist:
            QLWO=QLWO|Webpage.objects.filter(topic_name=i)

        d1={'webpages':QLWO}
        return render(request,'display_webpages.html',d1) 

    return render(request,'multiple_webpage.html',d)


def AccessRecord(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    
    if request.method=='POST':
        name=request.POST['name']
        date=request.POST['date']
        author=request.POST['author'] 
       
        WO=Webpage.objects.get(name=name)
        AO=AccessRecords.objects.get_or_create(name=WO,date=date,author=author)[0]
        AO.save()
        ARO=AccessRecords.objects.all()
        d1={'accessrecords':ARO}
        return render(request,'AccessRecords.html',d1)
    return render(request,'display_access.html',d)



