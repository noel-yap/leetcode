import unittest

import decode_string


class TestDecodeStrExpr(unittest.TestCase):
    def test_decode_str_expr(self):
        decoder = decode_string.Decoder()

        expected = ("aoeu", "")

        actual = decoder.decode_str_expr("aoeu")

        self.assertEqual(expected, actual)


class TestDecodeNumExpr(unittest.TestCase):
    def test_decode_num_expr(self):
        decoder = decode_string.Decoder()

        expected = ("aoeu" * 23, "")

        actual = decoder.decode_num_expr("23[aoeu]")

        self.assertEqual(actual, expected)


class TestDecode(unittest.TestCase):
    def setUp(self):
        self.decoder = decode_string.Decoder()

    def test_decode_string(self):
        expected = "aoeu"

        actual = self.decoder.decode("aoeu")

        self.assertEqual(expected, actual)

    def test_num_expr(self):
        expected = "aoeu" * 2

        actual = self.decoder.decode("2[aoeu]")

        self.assertEqual(expected, actual)

    def test_bracket_expr(self):
        expected = "aoeu"

        actual = self.decoder.decode("[aoeu]")

        self.assertEqual(expected, actual)

    def test_abcdefg(self):
        expected = "abcdefg"

        actual = self.decoder.decode("abcdefg")

        self.assertEqual(expected, actual)

    def test_aaaaaaaa(self):
        expected = "aaaaaaaa"

        actual = self.decoder.decode("2[2[2[a]]]")

        self.assertEqual(expected, actual)

    def test_abccdeffffdeffffdeffff(self):
        expected = "abccdeffffdeffffdeffff"

        actual = self.decoder.decode("ab2[c]3[de4[f]]")

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
