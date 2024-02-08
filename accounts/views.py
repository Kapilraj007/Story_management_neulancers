from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
     form=RegisterForm()
     if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Regirations successfully')
            return redirect('login')
     return render(request,"register.html",{'form':form})

def login_page(request):
    page = 'login'
    if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Login successfully")
                return redirect('home')
            else:
                messages.error(request,"Invaild username or password")
                return redirect('login')
    context = {'page':page}
    return render(request, 'register.html', context)

def logoutUser(request):
    logout(request)
    messages.warning(request, "Logged Out!")
    return redirect('/')

@login_required(login_url="/login")
def profile(request,id):
    user = User.objects.get(id=id)
    
    return render(request,'profile.html',{'form':user})


def updateProfile(request, id):
    user = get_object_or_404(User, id=id)

    if request.user != user:
        return HttpResponse("You are not allowed here !!")
    
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Update successful")
            return redirect('/')
    else:
        form = RegisterForm(instance=user)

    return render(request, 'updateprofile.html', {'form': form})
