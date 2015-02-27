from django.test import TestCase
from expects import *


class TestViews(TestCase):
    def test_index(self):
        response = self.client.get('/')
        # Make sure the page context variable was passed
        expect(response.context['page']).to(equal('index'))
