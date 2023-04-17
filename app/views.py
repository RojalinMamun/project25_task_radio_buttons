from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.

# it is used to inserting topic objects
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        print(request.POST)
        return HttpResponse(f'<h1>{tn} data is inserted</h1>')

    d={'topic':Topic.objects.all()}
    return render(request,'insert_topic.html',d)

# it is used to inserting webpage objects
def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'topic':LTO}
    if request.method=='POST':
        tn=request.POST['topic']
        n=request.POST['name']
        url1=request.POST['url']
        mail=request.POST['email']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url1,email=mail)[0]
        WO.save()
        return HttpResponse(f'<h1>{n} data is inserted</h1>')
    return render(request,'insert_webpage.html',d)
# it is used to inserting taccess record  objects
def insert_accessrecords(request):
    d={'wo':Webpage.objects.all()}
    if request.method=='POST':
        wo=request.POST['wo']
        
        at=request.POST['at']
        da=request.POST['da']
        print(request.POST)

        WO=Webpage.objects.get(name=wo)
        AO=AccessRecord.objects.get_or_create(name=WO,author=at,date=da)[0]
        AO.save()
        return HttpResponse(f'<h1>{at} data is submitted</h1>')
    return render(request,'insert_accessrecords.html',d)




# it is used to display topic objects's data
def display_topic(request):
    d={'topic':Topic.objects.all()}
    return render(request,'display_topic.html',d)



# it is used to display multi selected webpage objects's data
def display_webpage(request):
    LTO=Topic.objects.all()
    d={'topic':LTO}
    if request.method=='POST':
        td=request.POST.getlist('topic')
        print(td)
        webquery=Webpage.objects.none()
        for a in td:
            webquery=webquery|Webpage.objects.filter(topic_name=a)
        d1={'webpages':webquery}
        return render(request,'display_webpage.html',d1)
    return render(request,'select_multi_web.html',d)

# it is used to display only single selected webpage objects
def single_select_web(request):
    d={'topic':Topic.objects.all()}
    return render(request,'single_select_web.html',d)

# it is used to display only multi selected webpage objects
def checkbox_web(request):
    d={'topic':Topic.objects.all()}
    return render(request,'checkbox_web.html',d)

# it is used to display only single selected webpage objects
def radio_webpage(request):
    d={'topic':Topic.objects.all()}
    return render(request,'radio_webpage.html',d)



# it is used to display only multi selected webpage objects
def display_access(request):
    d={'name':Webpage.objects.all()}
    if request.method=='POST':
        td=request.POST.getlist('name')
        print(td)
        access=Webpage.objects.none()
        for a in td:
            access=access|AccessRecord.objects.filter(name=a)
        d1={'access':access}
        return render(request,'display_access.html',d1)
    return render(request,'multi_select_access.html',d)

# it is used to display only single selected webpage objects
def single_select_access(request):
    d={'name':Webpage.objects.all()}
    return render(request,'single_select_access.html',d)
# it is used to display only multi selected webpage objects
def checkbox_access(request):
    d={'name':Webpage.objects.all()}
    return render(request,'checkbox_access.html',d)
    
# it is used to display only single selected webpage objects
def radio_access(request):
    d={'name':Webpage.objects.all()}
    return render(request,'radio_access.html',d)