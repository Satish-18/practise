from django.urls import path
from . import views


urlpatterns = [
    path("", views.index,name="home"),
    path("contact/",views.contact,name="Contact"),
    path("about/",views.about,name="About"),
    path("register/",views.register,name="signup"),
    path("login/",views.Login,name="Login"),
    path("logout/",views.Logout,name="Logout"),
    path("profile/",views.profile,name="profile"),
    #path('resume/',views.resume,name='resume'),
    #path('pdf_view/', views.ViewPDF, name="pdf_view"),
    #path('pdf_download/', views.DownloadPDF, name="pdf_download"),
]