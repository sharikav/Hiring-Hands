from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from .models import User, Customer, Labourer, Interface
from .forms import CustomerSignUpForm, LabourerSignUpForm
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    return render(request,'register.html')        

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'customer_register.html' 

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')  

class labourer_register(CreateView):
    model = User
    form_class = LabourerSignUpForm
    template_name = 'labourer_register.html'  

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')    

@csrf_protect
def login_request_l(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('profile')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'loginl.html',context={'form':AuthenticationForm()})


def login_request_c(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                
                return redirect('index')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'loginc.html',context={'form':AuthenticationForm()})    

def logout_view(request):
    logout(request)
    return redirect('register')        


def index(request):
    return render(request, 'index.html')
@csrf_protect
def profile(request ):   
    labourer= User.objects.filter(user=request.labourer)
    return render(request, 'profile.html',{'labourer':labourer}) 
    #return render(request, 'profile.html')    

   