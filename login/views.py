# accounts/views.py

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse  # Import reverse

from django.http import HttpResponseRedirect

def login_view(request):
    return render(request, 'login/register.html')


def custsign(request):
        if request.method=='POST':
            uname=request.POST.get('username')
            email=request.POST.get('email')
            pass1=request.POST.get('password1')
            pass2=request.POST.get('password2')
            if pass1!=pass2:
                return HttpResponse("Your password and confrom password are not Same!!")
            else:
                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save()
                return redirect('custlogin')
    
        return render (request,'login/register.html')
def custlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/todos/')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login/loginc.html')


