from django.test import TestCase
from expects import *
from apps.people.factories import PersonFactory
from django.db import IntegrityError
from apps.people.models import Person


class TestPersonModel(TestCase):
    def test_has_a_valid_factory(self):
        PersonFactory.create()
        person_count = Person.objects.count()
        expect(person_count).to(equal(1))

    def test_is_invalid_with_null_name(self):
        try:
            PersonFactory.create(name=None)
            self.fail()  # Should not arrive here as the above should trigger the Integrity error
        except IntegrityError:
            pass

    def test_is_invalid_with_null_email(self):
        try:
            PersonFactory.create(email=None)
            self.fail()
        except IntegrityError:
            pass

    def test_is_invalid_with_null_age(self):
        try:
            PersonFactory.create(age=None)
            self.fail()
        except IntegrityError:
            pass
