from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('satish/',views.satish_home,name='satish_home'),
    path('contact',views.contact,name='contact'),
    path('projects',views.projects,name="projects"),
    path('signup',views.signup,name="signup"),
    path('login',views.Login,name='login'),
    path('logout',views.Logout,name='logout'),

]

