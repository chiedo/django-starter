"""
**************************
Views
**************************

The views
"""
from django.shortcuts import render


def index(request):
    return render(request, 'people/index.html')
