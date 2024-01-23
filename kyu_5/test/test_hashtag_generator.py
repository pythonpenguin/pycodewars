import unittest
import the_hashtag_generator


class MyTestCase(unittest.TestCase):

    def test_codewars(self):
        self.assertEqual("#Codewars", the_hashtag_generator.generate_hashtag("Codewars"))

    def test_codewars_space(self):
        self.assertEqual("#Codewars", the_hashtag_generator.generate_hashtag("Codewars       "))

    def test_codewars_start_with_space(self):
        self.assertEqual("#Codewars", the_hashtag_generator.generate_hashtag("      Codewars       "))

    def test_single_letter(self):
        self.assertEqual("#G", the_hashtag_generator.generate_hashtag("      g      "))

    def test_empty(self):
        self.assertFalse(the_hashtag_generator.generate_hashtag("             "))
        self.assertFalse(the_hashtag_generator.generate_hashtag(""))

    def test_too_long(self):
        self.assertFalse(the_hashtag_generator.generate_hashtag(" e" * 200))
        self.assertFalse(the_hashtag_generator.generate_hashtag(" e" * 140))

    def test_100_e(self):
        self.assertEqual("#"+("E"*100), the_hashtag_generator.generate_hashtag("      e"*100))

    def test_result_140(self):
        self.assertEqual("#" + ("E" * 139), the_hashtag_generator.generate_hashtag("      e" * 139))