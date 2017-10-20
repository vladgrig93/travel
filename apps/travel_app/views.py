from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages
import bcrypt
def index(request):
    return render(request,'travel_app/index.html')

def register(request):
    errors=Users.objects.validator(request.POST)#sends the post info to validator in models
    if errors:
        for error in errors:
            messages.error(request, errors[error])
        return redirect('/')
    else:
        hashedpassword=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user=Users.objects.create(name=request.POST['name'], username=request.POST['username'],password=hashedpassword)
        print user
        request.session['id']=user.id#logs this user into system
        return redirect('/')#change name

def login(request):
    login_return=Users.objects.login_model(request.POST)
    if 'user' in login_return:
        request.session['id']=login_return['user'].id 
        request.session['name']=login_return['user'].name 
        return redirect('/newpage')#change name
    else:
        messages.error(request,login_return['error'])
        return redirect('/')

def logout(request):
    del request.session['id']
    return redirect('/')

def display(request):
    trips=Trips.objects.filter(user=(Users.objects.get(id=request.session['id'])))|Trips.objects.filter(joiners=(Users.objects.get(id=request.session['id'])))
    alltrips=Trips.objects.exclude(user=(Users.objects.get(id=request.session['id']))).exclude(joiners=(Users.objects.get(id=request.session['id'])))
    context={'trips':trips, 'alltrips':alltrips}
    return render(request, "travel_app/newpage.html", context)#add context if necessary #change folder name

#travel functions
def add(request):
    return render(request, 'travel_app/addtravel.html')

def process(request):
    errors=Trips.objects.trip_validator(request.POST)
    if errors:
        for error in errors:
            messages.error(request, errors[error])
        return redirect('/add')
    else:
        trips=Trips.objects.create(destination=request.POST['destination'], description=request.POST['description'], start=request.POST['start'], end=request.POST['end'], user=Users.objects.get(id=request.session['id']))
        return redirect('/newpage')


def goto(request, trip_id):
    trip=Trips.objects.get(id=trip_id)
    # otherjoiners=Trips.objects.exclude(user=Users.objects.get(id=request.session['id']))
    context={'trip':trip}
    return render(request, 'travel_app/destination.html', context)

def jointripprocess(request, trip_id):
    this_trip=Trips.objects.get(id=trip_id)
    this_joiner=Users.objects.get(id=request.session['id'])
    this_joiner.jtrips.add(this_trip)
    return redirect('/newpage')


