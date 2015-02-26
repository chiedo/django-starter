"""
**************************
Views
**************************

The views
"""
from django.shortcuts import render


def index(request):
    return render(request, 'people/index.html')

from apps.people.models import Person
from rest_framework import viewsets
from apps.people.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
