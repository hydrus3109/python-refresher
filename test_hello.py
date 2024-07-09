import unittest
import hello

"""
class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")

    # def test_sin(self):
    #     self.assertEqual(hello.sin(0), 0)
    #     self.assertEqual(hello.sin(1), 0.8414709848078965)

    # def test_cos(self):
    #     self.assertEqual(hello.cos(0), 1)
    #     self.assertEqual(hello.cos(1), 0.5403023058681398)

    # def test_tan(self):
    #     self.assertEqual(hello.tan(0), 0)
    #     self.assertEqual(hello.tan(1), 1.5574077246549023)

    # def test_cot(self):
    #     self.assertEqual(hello.cot(0), float("inf"))
    #     self.assertEqual(hello.cot(1), 0.6420926159343306)
"""
class testbank(unittest.TestCase):
    def test_deposit(self):
        bank = hello.bank(10, 'aidan',123)
        self.assertEqual(bank.deposit(10), 20)
        self.assertEqual(bank.deposit(-5), 'can\'t deposite negative money')
    def test_withdraW(self):
        bank = hello.bank(10, 'aidan',123)
        self.assertEqual(bank.withdraw(-5), 'can\'t withdraw negative money')
        self.assertEqual(bank.withdraw(1000), 'too little money in account')
        self.assertEqual(bank.withdraw(3),7)
    def test_bal(self):
        bank = hello.bank(10, 'aidan',123)
        self.assertEqual(bank.printbal(), 10)

if __name__ == "__main__":
    unittest.main()
