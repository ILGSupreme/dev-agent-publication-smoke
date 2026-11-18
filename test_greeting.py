import unittest

from greeting import greet


class GreetingTests(unittest.TestCase):
    def test_greets_named_person(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")
