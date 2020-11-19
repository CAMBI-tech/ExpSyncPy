import unittest

from expsyncpy.sync import place_holder


class TestSync(unittest.TestCase):

    def test_place_holder(self):
        response = place_holder(2, 3)
        expected = 5
        self.assertEqual(response, expected)
