import unittest
import hello
import bank


class testbank(unittest.TestCase):
    def test_init(self):
        bank1 = bank.bank("aidan", 123)
        self.assertEqual(bank1.getaccountnum(), 123)
        self.assertEqual(bank1.printname(), "aidan")
        bank2 = bank.bank("notaidan", 987)
        self.assertEqual(bank2.getaccountnum(), 987)
        self.assertEqual(bank2.printname(), "notaidan")
        self.assertEqual(bank1.printbal(), 0)
        self.assertEqual(bank2.printbal(), 0)

    def test_deposit(self):
        bank1 = bank.bank("aidan", 123)
        bank1.deposit(10)
        self.assertEqual(bank1.deposit(10), 20)
        self.assertRaises(bank1.deposit(-5), ValueError)

    def test_withdraW(self):
        bank1 = bank.bank("aidan", 123)
        bank1.deposit(10)
        self.assertRaises(bank1.withdraw(-5), ValueError)
        self.assertEqual(bank1.withdraw(1000), -1)
        self.assertEqual(bank1.withdraw(3), 7)

    def test_bal(self):
        bank1 = bank.bank("aidan", 123)
        bank1.deposit(10)
        self.assertEqual(bank1.printbal(), 10)


if __name__ == "__main__":
    unittest.main()
