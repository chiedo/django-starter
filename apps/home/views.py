"""
**************************
Views
**************************

The views
"""
from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html', {'page': 'index'})
