from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request,"login.html")

def register_view(request):
    return render(request,"register.html")

def forget(request):
    return render(request,"forgot.html")