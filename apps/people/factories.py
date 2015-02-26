from apps.people.models import Person
from random import randint
from faker import Faker
from factory.django import DjangoModelFactory
fake = Faker()


class PersonFactory(DjangoModelFactory):
    class Meta:
        model = Person

    name  = fake.name()
    email = fake.email()
    age   = randint(10, 99)
