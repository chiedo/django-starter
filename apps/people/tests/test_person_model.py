from django.test import TestCase
from expects import *
from apps.people.factories import PersonFactory
from apps.people.models import Person


class TestPersonModel(TestCase):
    def test_john_doe_is_created_successfully(self):
        PersonFactory.create(name="John Doe")
        person = Person.objects.first()
        expect(person.name).to(equal("John Doe"))
