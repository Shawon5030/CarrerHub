
from django.urls import path 
from app.views import  *
urlpatterns = [

    path("login/",login_view,name='login'),
    path("register/",register_view,name='register'),
    path("forget/",forget,name='forget'),
]
