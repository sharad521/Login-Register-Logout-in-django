from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
from .models import Feature1
from .models import Feature2


# Create your views here.
def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password== password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already exist')
                return redirect('register')
            elif User.objects.filter(username= username).exists():
                messages.info(request,'username already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect ('login')
        else:
            messages.info(request,'both password are not same')
            return redirect('register')
    else:
        return render(request,'register.html')

def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid info')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def chinese(request):
    features = Feature.objects.all()
    return render(request,'chinese.html',{'features':features})
def indian(request):
    feature2= Feature2.objects.all()
    return render(request,'indian.html', {'feature2': feature2})
def italian(request):
    feature1= Feature1.objects.all()
    return render(request,'italian.html',{'feature1': feature1})

