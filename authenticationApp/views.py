from django.shortcuts import render
from django.http import HttpResponse
from .forms import calorieForm, calorieModel
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, "authenticationApp/index.html")


def newApplicant(request):
    calform = calorieForm(request.POST or None)
    context = {
        "calform": calform
    }

    return render(request, "authenticationApp/newApplicant.html", context)


def calories(request):
    calform = calorieForm(request.POST or None)
    context = {
        "calform": calform
    }

    if request.method == "POST":
        print(request.POST)
        User.objects.create_user(request.POST["username"], "", request.POST["password"])
        return render(request, "authenticationApp/calInfo.html")
