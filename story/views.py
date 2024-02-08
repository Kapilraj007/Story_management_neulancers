from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .forms import StoryForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    story = Story_Management.objects.all()
    context ={
        'story' : story,
       }
    return render(request, 'home.html',context)

@login_required(login_url="/accounts/login")
def storyform(request):
    form = StoryForm()
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.user = request.user
            story.save()
            messages.success(request,"story created successfully")
            return redirect('/')
    else:

        return render(request, 'story_form.html',{'form':form})

@login_required(login_url="/accounts/login")
def updatestory(request,id):
    story = Story_Management.objects.get(id = id)
    form = StoryForm(instance=story)
    if request.method=='POST':
        form = StoryForm(request.POST, instance=story)
        if form.is_valid():
            form.save()
            messages.success(request,"Story updated Successfully")
            return redirect("/")
    else:

        return render(request,'update_story.html',{'form':form})

@login_required(login_url="/accounts/login")
def deletestory(request,id):
    form = Story_Management.objects.get(id = id)
    if request.method == 'POST':
        form.delete()
        messages.info(request,"Story deleted successfully")
        return redirect('/')
    return render(request, 'delete.html',{'obj':form})

@login_required(login_url="/accounts/login")
def userstory(request,id):
    user = User.objects.get(id=id)
    form = user.story_management_set.all()
    context = {
        'user':user,
        'form':form,
    }
    return render(request, 'user_story.html',context)

def story(request,id):
    form = Story_Management.objects.get(id=id)
    return render(request,'story.html',{'form':form})