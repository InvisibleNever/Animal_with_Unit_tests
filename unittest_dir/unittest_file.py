from unittest import TestCase
from unittest import expectedFailure
from main import Animal


class TestCases(TestCase):

    def test_cats_phrase(self):
        self.assertEqual(Animal("cat").phrase(), "Meow")
        self.assertEqual(Animal("dog").phrase(), "Woof")
        self.assertEqual(Animal("lion").phrase(), "Roar")

    def test_paws_true(self):
        self.assertTrue(Animal("cat").paws())

    def test_paws_false(self):
        self.assertFalse(Animal("fish").paws())

    def test_speed(self):
        self.assertEqual(Animal("fish").speed(), 56)
        self.assertNotEqual(Animal("dog").speed(), 70)
        self.assertEqual(Animal("cheetah").speed(), 110)

    def test_speed_integer(self):
        self.assertIsInstance(Animal("dog").speed(), int)

    @expectedFailure
    def test_unknown_type(self):
        self.assertEqual(Animal("fish").phrase(), "Silence")

    @expectedFailure
    def test_wrong_phrase(self):
        self.assertEqual(Animal("dog").phrase(), "Meow")

    @expectedFailure
    def test_paws_fail(self):
        self.assertFalse(Animal("dog").paws())

    @expectedFailure
    def test_wrong_speed(self):
        self.assertEqual(Animal("cheetah").speed(), 56)
