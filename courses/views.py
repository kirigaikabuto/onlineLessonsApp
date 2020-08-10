from django.shortcuts import render
from .models import *


def index_page(request):
    courses = Course.objects.all()
    context = {
        "courses": courses,
    }
    return render(request, "courses/index.html", context=context)