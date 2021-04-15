from django.shortcuts import render, redirect
from your_app_name_here.models import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        user = User.objects.create(
            name=request.POST['name'],
            lastname=request.POST['lastname'],
            email=request.POST['email'],
            age=request.POST['age']
        )
        print(user)
        return redirect('/')
    
    context = {
        'users' : User.objects.all()
    }
    return render(request, 'index.html', context)


def dojo(request):
    if request.method == 'POST':
        dojo = Dojo.objects.create(
            name=request.POST['name'],
            city=request.POST['city'],
            state=request.POST['state'],
        )
        print(dojo)
        return redirect('/dojo')

    context = {
        'dojos' : Dojo.objects.all()
    }
    return render(request, 'dojo.html', context)

def ninja(request):
    if request.method == 'POST':
        ninja = Ninja.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            dojo_id=request.POST['dojo'],
        )
        print(ninja)
        return redirect('/dojo')