"""
**************************
Views
**************************

The views
"""
from django.shortcuts import render
from django_react.render import render_component


def index(request):
    car = render_component('/code/apps/home/react/components/Car.react.js', props={'name': 'Subaru'})
    bus = render_component('/code/apps/home/react/components/Bus.react.js', props={'name': 'School Bus'})
    return render(request, 'home/index.html', {'page': 'index', 'car': car, 'bus': bus})
