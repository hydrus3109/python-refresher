import unittest
import hello
import math


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)
        self.assertAlmostEqual(hello.sin(1 + 2 * math.pi), 0.8414709848078965, 5)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)
        self.assertAlmostEqual(hello.cos(1 + 2 * math.pi), 0.5403023058681398, 5)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)
        self.assertAlmostEqual(hello.tan(1 + 2 * math.pi), 1.5574077246549023, 5)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)
        self.assertAlmostEqual(hello.cot(1 + 2 * math.pi), 0.6420926159343306, 5)

    def test_sum(self):
        self.assertEqual(hello.add(2, 2), 4)
        self.assertEqual(hello.add(-1, 10), 9)

    def test_sub(self):
        self.assertEqual(hello.sub(2, 2), 0)
        self.assertEqual(hello.sub(-1, 10), -11)

    def test_mul(self):
        self.assertEqual(hello.mul(2, 2), 4)
        self.assertEqual(hello.mul(-1, 10), -10)

    def test_div(self):
        self.assertRaises(hello.div(4, 0), ValueError)
        self.assertEqual(hello.div(9,3), 3)
    def test_pow(self):
        self.assertEqual(hello.power(1,3),1)
        self.assertEqual(hello.power(2,3),8)


if __name__ == "__main__":
    unittest.main()
