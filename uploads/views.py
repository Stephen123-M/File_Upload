from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Picture
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    pict = Picture.objects.filter(owner = request.user)
    context = {
        "picture": pict
        }
    return render(request, "index.html", context)

@login_required
def upload(request):
    if request.method == "POST":
        p = request.FILES['picture']
        pic = Picture(photo = p, owner = request.user)
        pic.save()
    return redirect('/')


