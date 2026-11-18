import unittest

from greeting import greet


class GreetingTests(unittest.TestCase):
    def test_greets_named_person(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_greets_blank_name(self):
        for name in ("", "  "):
            with self.subTest(name=name):
                self.assertEqual(greet(name), "Hello, stranger!")
