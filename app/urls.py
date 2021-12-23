from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('questions/', views.questions, name='questions'),
    path('questions/resultsQuestion/', views.result_question, name='result_question'),
    path('questions/resultsConvert/', views.result_convert, name='result_convert'),


    #path('questions/', views.handle_questions, name='questions'),
]