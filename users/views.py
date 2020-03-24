from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def Login(request):
    return render(request, "login.html")

def Login_User(request):
    if request.method == "POST":
        uname = request.POST['username']
        psw = request.POST['password']
        user = authenticate(username = uname, password = psw)
        if user is not None:
            login(request, user)
            response = redirect('/')
        else:
            response = HttpResponse('Wrong details')
    return response

            

