from django.urls import path,include
from abes import views
from .views import InterviewListView,InterviewDetailView,ResourceListView,ResourceDetailView


urlpatterns = [
    path('',views.login_user,name='login'),
    path('home',views.home,name='home'),
    path('logout',views.home,name='logout'),
    path('interview', InterviewListView.as_view(),name="interview"),
    path('interview/<int:pk>', InterviewDetailView.as_view(),name="interviewdetail"),
    path('resource', ResourceListView.as_view(),name="resource"),
    path('resource/<int:pk>', ResourceDetailView.as_view(),name="resourcedetail"),
    path('friendsai', views.friendsai,name="friendsai"),
    path('placements', views.Placement,name="placement"),
    path('resume', views.ResumeBuilder,name="resume"),
]
