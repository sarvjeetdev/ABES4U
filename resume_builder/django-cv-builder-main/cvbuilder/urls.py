from django.urls import path
from . import views

app_name = 'cvbuilder'

urlpatterns = [
    path('', views.MainPage.as_view(), name='MainPage'),
    path('preview/', views.ResumePreview.as_view(), name='ResumePreview'),

    path('create_experience/', views.CreateExperience.as_view(), name='CreateExperience'),
    path('update_experience/<str:pk>', views.UpdateExperience.as_view(), name='UpdateExperience'),
    path('delete_experience/<str:pk>', views.DeleteExperience.as_view(), name='DeleteExperience'),
    path('save_experience_order/', views.SaveExperienceOrdering.as_view(), name='SaveExperienceOrdering'),

    path('create_skill/', views.CreateSkill.as_view(), name='CreateSkill'),
    path('delete_skill/<str:pk>', views.DeleteSkill.as_view(), name='DeleteSkill'),
    path('save_skill_order/', views.SaveSkillsOrder.as_view(), name='SaveSkillsOrder'),

    path('create_education/', views.CreateEducation.as_view(), name='CreateEducation'),
    path('update_education/<str:pk>/', views.UpdateEducation.as_view(), name='UpdateEducation'),
    path('delete_education/<str:pk>/', views.DeleteEducation.as_view(), name='DeleteEducation'),
    path('save_education_order/', views.SaveEducationOrder.as_view(), name='SaveEducationOrder'),

    path('create_language/', views.CreateLanguage.as_view(), name='CreateLanguage'),
    path('update_language/<str:pk>/', views.UpdateLanguage.as_view(), name='UpdateLanguage'),
    path('delete_language/<str:pk>/', views.DeleteLanguage.as_view(), name='DeleteLanguage'),
    path('save_language_order/', views.SaveLanguageOrder.as_view(), name='SaveLanguageOrder'),

    path('create_achievement/', views.CreateAchievement.as_view(), name='CreateAchievement'),
    path('update_achivement/<str:pk>/', views.UpdateAchievement.as_view(), name='UpdateAchievement'),
    path('delete_achievement/<str:pk>/', views.DeleteAchievement.as_view(), name='DeleteAchievement'),
    path('save_achievement_order/', views.SaveAchievementOrder.as_view(), name='SaveAchievementOrder'),

    path('create_publication/', views.CreatePublication.as_view(), name='CreatePublication'),
    path('update_publication/<str:pk>/', views.UpdatePublication.as_view(), name='UpdatePublication'),
    path('delete_publication/<str:pk>/', views.DeletePublication.as_view(), name='DeletePublication'),
    path('save_publication_order/', views.SavePublicationOrder.as_view(), name='SavePublicationOrder'),

    path('share/<str:code>', views.SharedResumePreview.as_view(), name='SharedResumePreview'),
    path('download_pdf/', views.PDFView.as_view(), name='pdf')
]