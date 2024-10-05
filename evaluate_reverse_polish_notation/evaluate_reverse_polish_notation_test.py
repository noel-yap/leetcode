import unittest

import evaluate_reverse_polish_notation


class TestOps(unittest.TestCase):
    def test_div_neg(self):
        expected = -2

        actual = evaluate_reverse_polish_notation.RpnEvaluator.ops['/'](-5, 2)

        self.assertEqual(expected, actual)

    def test_div_pos(self):
        expected = 2

        actual = evaluate_reverse_polish_notation.RpnEvaluator.ops['/'](5, 2)

        self.assertEqual(expected, actual)


class TestEvaluateReversePolishNotation(unittest.TestCase):
    def test_1(self):
        expected = 9

        actual = evaluate_reverse_polish_notation.RpnEvaluator().eval(["2", "1", "+", "3", "*"])

        self.assertEqual(expected, actual)

    def test_2(self):
        expected = 6

        actual = evaluate_reverse_polish_notation.RpnEvaluator().eval(["4","13","5","/","+"])

        self.assertEqual(expected, actual)

    def test_3(self):
        expected = 22

        actual = evaluate_reverse_polish_notation.RpnEvaluator().eval(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
