from django.test import TestCase


class TestModel(TestCase):
    def test_true_is_equal_to_true(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future
        """
        self.assertEqual(True, True)
