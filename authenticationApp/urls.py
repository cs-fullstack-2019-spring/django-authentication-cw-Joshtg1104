from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('newApplicant/', views.newApplicant, name='newApplicant'),
    path('calInfo/', views.calories, name='calInfo'),

]