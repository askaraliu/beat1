from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from poll.models import Person
from django.views.decorators.csrf import csrf_exempt

# def home(request):
    # t=loader.get_template("home.html")
    # context={
    #     'name':'john',
    #     'age':21
    # }
    # return HttpResponse(t.render(context,request))

def home(request):
    return render(request,'home.html',{
        'name':'john',
        'age': 21
    })


def Persons(request):
    t=loader.get_template("Persons.html")
    p=Person.objects.all()
    context={
        'p':p
    }
    return HttpResponse(t.render(context,request))

def persondetails(request,id):
    t=loader.get_template("persondetails.html")
    p=Person.objects.get(id=id)
    context={
        'p':p
    }
    return HttpResponse(t.render(context,request))

def addperson(request):
    t=loader.get_template("addperson.html")
    return HttpResponse(t.render())

@csrf_exempt
def addpersonpageprocess(request):
    t=loader.get_template('addsuccess.html')
    if request.method=="POST":
        name=request.POST['name']
        eid=request.POST['eid']
        address=request.POST['address']
        dob=request.POST['dob']
        email=request.POST['email']
        mob=request.POST['mob']
        p=Person(name=name,eid=eid,address=address,dob=dob,email=email,mob=mob)
        p.save()
    return HttpResponse(t.render())

def deleteperson(request,id):
    t=loader.get_template("deletedsuccess.html")
    p=Person.objects.get(id=id)
    p.delete()
    return HttpResponse(t.render())

def updateperson(request,id):
    t=loader.get_template("updatepage.html")
    p=Person.objects.get(id=id)
    context={
        'p':p
    }
    return HttpResponse(t.render(context,request))

@csrf_exempt
def updatepersonprocess(request,id):
    t=loader.get_template('updatesuccess.html')
    if request.method=="POST":
        name=request.POST['name']
        eid=request.POST['eid']
        address=request.POST['address']
        dob=request.POST['dob']
        email=request.POST['email']
        mob=request.POST['mob']

        p=Person.objects.get(id=id)

        p.name=name
        p.address=address
        p.eid=eid
        p.email=email
        p.dob=dob
        p.mob=mob

    p.save()
    return HttpResponse(t.render())