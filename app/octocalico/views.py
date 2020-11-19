#from django.shortcuts import render ######original

from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request , user)
            return redirect('/success')
        else:
            messages.info(request, 'invalid username or password')
            return render(request, 'login.html', {'status' : "Invalid user or password"})
    else:
        return render(request,'login.html')


def register(request):

    if request.method == 'POST':

        email = request.POST['email']
        username = request.POST['username']
        password= request.POST['password']

        user = User.objects.create_user(username = username , password = password , email = email)
        user.save()
        print('user created')
        return redirect('/home')

    return render(request,'register.html')

def custom(request):
    return render(request, 'home.html')

def success(request):
    print(request.user)
    return render(request, 'success.html', {'user': request.user})

def home(request):
    return render(request, 'home.html')
