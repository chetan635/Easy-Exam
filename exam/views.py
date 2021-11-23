from django.shortcuts import render , redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"template.html")

def handleSignup(request):
    if request.method=='POST' :
        username = request.POST.get('username', False)
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for input
        if(len(username)>10):
            messages.error(request,"The Length of Username Should be less than 10")
            return redirect('home')

        # username should be less than 10 char
        if  not username.isalnum() :
            messages.error(request,"The Length of Username Should be less than 10")
            return redirect('home')

        # pass should not equal to pass1
        if pass1!=pass2:
            messages.error(request,"PassWord Do not Match")
            return redirect('home')
            
        
    # creating user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your Account Has Been Successfully Created")
        return redirect('home')


    else:
        return HttpResponse("Page  found")


def handlelogin(request):
    if request.method=='POST' :
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user=authenticate(username=loginusername,password=loginpass)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentiles : please try again")
            return redirect('home')

        
    return HttpResponse("404 page not found")

def handlelogout(request):
    logout(request)
    return redirect('home')
    


