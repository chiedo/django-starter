from django.test import TestCase
from expects import *
from apps.people.models import Person


class TestPeopleApi(TestCase):
    def test_blank(self):
        expect(True).to(be_true)
