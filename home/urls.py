from django.urls import path
from .views import  login_view
from . import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path('login/', login_view, name='login'),
    path("private/", views.private, name="private"),
    
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup, name="signup"),
    
    
]