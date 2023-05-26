from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView,DetailView,CreateView
from .models import Interview,Resource
from .forms import ModelForm
from keras.models import load_model
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.optimizers import Adam 
import numpy as np
from django.template import Template, Context

model = keras.Sequential([
                          keras.layers.Dense(300,activation = tf.nn.relu),
                          keras.layers.Dense(200,activation = tf.nn.relu),
                          keras.layers.Dense(150,activation = tf.nn.relu),
                          keras.layers.Dense(150,activation = tf.nn.relu),
                          keras.layers.Dense(100,activation = tf.nn.relu),
                         keras.layers.Dense(100,activation = tf.nn.relu),
                         keras.layers.Dense(50,activation = tf.nn.relu),
                        keras.layers.Dense(30,activation = tf.nn.relu),
                        keras.layers.Dense(20,activation = tf.nn.relu),
                         keras.layers.Dense(20, activation= tf.nn.softmax)])
model.compile(optimizer ='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.build(input_shape = (395,5))
model.load_weights("abes\modelweights.h5")
# model = load_model("abes\sarv.h5",compile=False)
output= ["Frontend using HTML, CSS and JavaScript.","Frontend using React.","Backend using JavaScript frameworks.","Backend using Python Framework.",
 "Backend using Java Frameworks.", "Competitive Programming using C++","Competitive Programming using Python","Competitive Programming using Java",
 "Full Stack (JavaScript Based Tech Stack).","Full Stack (Python Based Tech Stack).","Full Stack (Java Based Tech Stack).","Data Science / AI / ML",
 "Blockchain","Cyber Security","Application Development using Kotlin","Application Development using Java","Application Development using Swift",
 "Application Development using Flutter"]

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
def Personality(a):
    classes=["ESTJ","ENTJ","ESFJ","ENFJ","ISTJ","ISFJ","INTJ","INFJ","ESTP","ESFP","ENTP","ENFP","ISTP","ISFP","INTP","INFP"]
    s=""
    if(a[0]+a[1]+a[2]>=2):
        s+='E'
    else:
        s+='I'
    if(a[3]+a[4]+a[5]>=2):
        s+='S'
    else:
        s+='N'
    if(a[6]+a[7]+a[8]>=2):
        s+='T'
    else:
        s+='F'
    if(a[9]+a[10]+a[11]>=2):
        s+='J'
    else:
        s+='P'
    return classes.index(s)+1
def friendsai(request):
    if request.method=="POST":
        form = request.POST
        #print(form)
        tenth= int(form['tenth'])
        ele =  int(form['eleventh'])
        twe = int(form['twelfth'])
        gui = 1 if 'guidance' in form else 0
        EvsI1 = 1 if "EvsI1" in form else 0
        EvsI2 = 1 if "EvsI2" in form else 0
        EvsI3 = 1 if "EvsI3" in form else 0
        SvsI1 = 1 if "SvsI1" in form else 0
        SvsI2 = 1 if "SvsI2" in form else 0
        SvsI3 = 1 if "SvsI3" in form else 0
        TvsF1 = 1 if "TvsF1" in form else 0
        TvsF2 = 1 if "TvsF2" in form else 0
        TvsF3 = 1 if "TvsF3" in form else 0
        JvsP1 = 1 if "JvsP1" in form else 0
        JvsP2 = 1 if "JvsP2" in form else 0
        JvsP3 = 1 if "JvsP3" in form else 0
        a = [EvsI1,EvsI2,EvsI3,SvsI1,SvsI2,SvsI3,TvsF1,TvsF2,TvsF3,JvsP1,JvsP2,JvsP3]
        per  = Personality(a) 
        print("The personality is ",per)
        data = [tenth,ele,twe,gui,per]
        data = np.array(data)
        data = data.reshape(-1,5)
        ans = list(model.predict(data)[0])
        #print(ans)
        ans = ans.index(max(ans))
        ans = output[ans-1]
        #print("THis is answer",ans)
        dic = {'Recommendation': ans}
        
        # return HttpResponse(int(ans))
        return render(request,'model.html',{'form': form,"Recomm":ans})
    else:
        form = ModelForm()
        return render(request,'model.html',{'form': form})





def ResumeBuilder(request):
    return render(request,'resume.html',{})