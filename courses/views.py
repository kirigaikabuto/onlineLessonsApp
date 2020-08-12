from django.shortcuts import render, redirect
from .models import *


# связка с фронтом отсюда передают данные на html
def index_page(request):
    courses = Course.objects.all()
    numbers = [1, 2, 3, 4]
    example = 11232
    word = "Hello world"
    context = {
        "courses": courses,
        "message": word,
        "numbers": numbers,
        "example": example,
    }
    return render(request, "courses/index.html", context=context)


def about_page(request):
    return render(request, "courses/about.html")


def contacts_page(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        feedBack = FeedBack(name=name, phone=phone)
        feedBack.save()
        return redirect("index_page_url")
    return render(request, "courses/contacts.html")