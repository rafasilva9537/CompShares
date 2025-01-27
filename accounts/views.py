from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def profile(request):
    return render(request, "accounts/pages/profile-page.html")

def login(request):
    return render(request, "accounts/pages/login.html")