from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def loadregister(request):
    return render(request,'register.html')

def loadlogin(request):
    return render(request,'login.html')

def Register(request):
    if request.method=='POST':
            vfname=request.POST.get('fname')
            vlname=request.POST.get('lname')
            vuname=request.POST.get('uname')
            vemail=request.POST.get('email')
            vpasswd=request.POST.get('pass')
            vrpasswd=request.POST.get('rpass')
            #return HttpResponse(vemail)
            if vpasswd == vrpasswd:
                if User.objects.filter(username=vuname).exists():
                    messages.success(request,'Username already exist')
                    return redirect('/')
                elif User.objects.filter(email=vemail).exists() :
                    return redirect('/')
                else:
                    newuser=User.objects.create_user(first_name=vfname, last_name=vlname, username=vuname,email=vemail,password=vpasswd)
                    newuser.save()
                    return redirect('/account/login')
            else:
                return redirect('/')  

def Login(request):
    if request.method =='POST':
        vuname=request.POST.get('uname')
        vpasswd=request.POST.get('passwd')
        print(vuname)
        newuser =auth.authenticate(username=vuname,password=vpasswd)
        if newuser is not None:
            auth.login(request, newuser)
            return redirect('/home')
        else:
            return render(request, 'register.html')  


@login_required(login_url='login')
def Logout(request):
    auth.logout(request)
    return redirect('/account/login')

@login_required(login_url='login')
def Dashbord(request):
    return render(request,'dashbord.html')


    