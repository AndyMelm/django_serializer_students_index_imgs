from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('students', views.myProducts),
    path('get-students', views.MyModelView.as_view()),
]
