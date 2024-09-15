import unittest

from polidictionary.poly_dictionary import PolyDictionary


class TestPolyDictionary(unittest.TestCase):

    def test_define(self):
        dictionary = PolyDictionary()
        self.assertEqual(
            dictionary.define("bike"),
            "a motor vehicle with two wheels and a strong frame",
        )

    def test_synonym(self):
        dictionary = PolyDictionary()
        self.assertEqual(dictionary.synonym("bike"), "motorcycle")


if __name__ == "__main__":
    unittest.main()
