from django.test import TestCase
from expects import *
from apps.people.models import Person
from apps.people.factories import PersonFactory
import json


class TestPeopleApi(TestCase):
    def setUp(self):
        # Every test needs access to the example class
        self.scope = "/api"

    def test_get(self):
        PersonFactory.create(name="John Doe")
        response = self.client.get(self.scope + "/people/")
        json_data = json.loads(response.content)
        expect(json_data[0]['name']).to(equal("John Doe"))

    def test_post(self):
        person_attributes = PersonFactory.attributes()
        person_attributes["name"] = "Bob Nolan"

        # Set up the data for posting the person
        person_data = person_attributes

        headers = {'Content-type': 'application/json'}
        self.client.post(self.scope + "/people/", data=person_data, headers=headers)

        # Check for the person in the database
        person = Person.objects.first()
        expect(person.name).to(equal("Bob Nolan"))

    def test_put(self):
        person = PersonFactory.create()
        person_attributes = PersonFactory.attributes()
        person_attributes["name"] = "Bob updated"

        self.client.put(self.scope + "/people/%s/" % person.id, data=json.dumps(person_attributes),
                        content_type='application/json')

        # Check for the person in the database
        person = Person.objects.first()
        expect(person.name).to(equal("Bob updated"))

    def test_delete(self):
        person = PersonFactory.create()

        self.client.delete(self.scope + "/people/%s/" % person.id)

        # Make sure the person is not in the database
        person_count = Person.objects.count()
        expect(person_count).to(equal(0))
