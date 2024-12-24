from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
import random,re,string
from . import forms
from . import models
from django.conf import settings



# Create your views here.
def index(request):
    return render(request, 'index.html')

def psw_checker(request):
    if request.method== 'POST':
        psw= request.POST['Password']
        
        if len(psw) <= 10:
            messages.info(request, "A very weak Password, it should be longer than 10 characters!!")

        elif not re.search('[a-z]', psw):
            messages.info(request, "No small letters in your Password!!")

        elif not re.search('[0-9]', psw):
            messages.info(request,"No digits in your Password!!")        
        
        elif not re.search('[A-Z]', psw):
            messages.info(request,"No CAPS in Password!!")        

        elif not re.search('[!@#$%^&*(_)+/?{*}|\-]', psw):
            messages.info(request,"No Special character in your Password!!")

        elif re.search('[" "]', psw):
            messages.info(request,"Spaces not allowed in password!!")
        else:
            messages.info(request, f"Great!! Your Password is {psw} which is okay to use")
        psw=psw
    
    return render(request, 'psw_checker.html') # {'psw':psw})

# @login_required
def psw_maker(request): 
    if not request.user.is_authenticated:
        messages.info(request, "You must be logged in to access this page. Please login")
        return render(request, 'registration/login.html')
        # return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    if request.method== 'POST':
        num=request.POST['length']
        psw= request.POST['Password']

        char=string.ascii_letters + string.digits + string.punctuation
        pswd= ''
        num=int(num)
        print(num)


        for i in range(num):
                pswd+=random.choice(char)
                # messages.info(request, f'Your Password is {pswd}')   
        
        if psw != "PaSs" or num <=5:
            messages.info(request, "You are stupid, Bure sana")
            
        elif num <=10:
            messages.info(request, f'Password must be more than 10 letters, this password: | {pswd}| is not recommended.  You can use it if you are contented with it')
        
        else:
            messages.info(request, f'Your Password is(ommit "||"): | {pswd} |')
        pswd=pswd 
       
    return render(request, 'psw_maker.html')

def profile(request):
    obj= models.Profile.objects.all()
    form= forms.Profileform()  
    if request.method=="POST":
        if not request.user.is_authenticated:
            messages.info(request, "You must be logged in to access this page. Please login")
            return render(request, 'registration/login.html')
        else:
           form = forms.Profileform(request.POST, request.FILES)
        # pform = forms.Postform(request.POST or None)        
        if form.is_valid():
            user= auth.authenticate(User=User)
            messages.info(request,"sign in wth your name")
            if request.user.is_authenticated:
                instance=form.save(user)
                instance.save()
                messages.info(request, "Picture saved")
                return redirect(profile)
        else:
            messages.info(request, "Form saving Failed")
            return redirect(profile)

    context= {
            'form':form,
            'obj':obj
    }
    return render(request, 'profile.html', context)

def register(request):
    if request.method=='POST':
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is already taken")

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is already taken, Try to login")
            else:
                user= User.objects.create_user(username=username, email=email, password=password)
                messages.info(request, "Your account has been created successfully")
                return redirect(login)
        else:
            messages.info(request, "Passwords DO NOT match")
    
    return render(request, 'register.html')



def login(request):
     if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, "Login success")
            return redirect('/')
        
        else:
            messages.info(request, "Either Username/Password is not correct Try again")
            return redirect(login)
     
     return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return redirect('/')

def test(request):
     if request.method=="POST":
         pform= forms.Postform(request.POST or None)
         if pform.is_valid():
             messages.info(request, "You post has been sent")
             pform.save()


     return render(request, 'test.html', {'pform':pform})