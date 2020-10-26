from django.http import request
from django.shortcuts import render

# Create your views here.
def register_user(request):
    return render(request, 'account/register.html')

def login_user(request):
    return render(request, 'account/login.html')