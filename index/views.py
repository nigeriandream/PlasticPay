from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, "home.html")


def recycler_portal(request):
    return render(request, "recycler.html")


def support_recycler(request):
    return render(request, "support.html")


def recycle_data(request):
    return render(request, "recycle_data.html")
