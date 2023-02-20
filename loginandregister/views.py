from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from loginandregister.models import soeuser
from django.contrib import messages

def loginpage(request):
    rend = render(request, 'loginandregister/login.html')
    return rend

def register(request):
    rend = render(request, 'loginandregister/register.html')
    return rend

def forgotpassword(request):
    rend = render(request, 'loginandregister/forgotPassword.html')
    return rend

def createnewuser(request):
    if request.method!='POST':
        return HttpResponseRedirect('http://localhost:8000/loginandregister/registration/')
    else:
        name=request.POST['name']
        phno=request.POST['phno']
        email=request.POST['email']
        pwd=request.POST['pwd']

        if User.objects.filter(email= email).exists():
            messages.info(request,'This Email is already registered')
            return HttpResponseRedirect('http://localhost:8000/loginandregister/registration/')

        if(len(phno)!=10):
            messages.info(request, 'Invalid Phone Number.')
            return HttpResponseRedirect('http://localhost:8000/loginandregister/registration/')
        else:
            user= User.objects.create_user(username=email, password=pwd, email=email, first_name=name)
            user.save()
            myuser=soeuser()
            myuser.mainuser= user
            myuser.name= name
            myuser.phno= phno
            myuser.save()
            dic={'msg': "**Registration Successful. Login to your account.**"}
            rend = render(request, 'loginandregister/login.html',dic )
            return rend


def loginvalidation(request):
    if request.method!='POST':
        return HttpResponseRedirect('http://localhost:8000/loginandregister/loginpage/')
    else:
        email = request.POST['email']
        pwd = request.POST['pwd']
        user = auth.authenticate(username=email, password=pwd)
        if user is not None:
            request.session['islogin']= True
            request.session['user_name']= user.username
            auth.login(request, user)
            return HttpResponseRedirect('http://localhost:8000/soesite/home/')
        else:
            messages.info(request, 'Invalid Credentials')
            return HttpResponseRedirect('http://localhost:8000/loginandregister/loginpage/')


def userlogout(request):
    auth.logout(request)
    return HttpResponseRedirect('http://localhost:8000/loginandregister/loginpage/')




