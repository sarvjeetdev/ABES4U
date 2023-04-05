from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView,DetailView,CreateView
from .models import Interview,Resource
from .forms import ModelForm
# Create your views here.



def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            user_sess = {'user_name':user.username,'user_email':user.email}
            request.session['user'] = user_sess
            login(request, user)
            return redirect('home')
        else:
            return redirect("/")

    else:
        return render(request, 'authenticate/login.html',{})

def home(request):
    return render(request,'home.html',{})


def logout_view(request):
    if (request.session.get('user') != None):
        request.session.delete()
        logout(request)
        return redirect('login')
    
    return redirect('login')



class InterviewListView(ListView):
    model = Interview
    context_object_name = 'myblog'
    template_name = 'interview.html'
    ordering = ['-id']


class InterviewDetailView(DetailView):
    model = Interview
    context_object_name = 'blog'
    template_name = 'Interviewdetails.html'



class ResourceListView(ListView):
    model = Resource
    context_object_name = 'myblog'
    template_name = 'resource.html'
    ordering = ['-id']


class ResourceDetailView(DetailView):
    model = Resource
    context_object_name = 'blog'
    template_name = 'Resourcedetails.html'

def Placement(request):
    return  render(request,'placement.html',{})

def friendsai(request):
    if request.method=="POST":
        form = ModelForm(request.POST)
        #Model
        return HttpResponse("Submitting data")
    else:
        form = ModelForm()
        return render(request,'model.html',{'form': form})