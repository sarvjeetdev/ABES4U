from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView,DetailView,CreateView
from .models import Interview,Resource
# Create your views here.



def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect("/")

    else:
        return render(request, 'authenticate/login.html',{})

def home(request):
    return render(request,'home.html',{})


def logout_view(request):
    logout(request)
    return redirect('login')



class InterviewListView(ListView):
    model = Interview
    context_object_name = 'myblog'
    template_name = 'interview.html'
    ordering = ['-id']


class InterviewDetailView(DetailView):
    model = Interview
    template_name = 'details.html'



class ResourceListView(ListView):
    model = Resource
    context_object_name = 'myblog'
    template_name = 'resource.html'
    ordering = ['-id']


class ResourceDetailView(DetailView):
    model = Resource
    template_name = 'details.html'
