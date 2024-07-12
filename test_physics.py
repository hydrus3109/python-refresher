import unittest
import physics


class testbank(unittest.TestCase):
    def test_buoyancy(self):
        self.assertRaises(physics.calc_buoyancy(0, 1), ValueError)
        self.assertAlmostEqual(physics.calc_buoyancy(10, 10), 9810)
        self.assertAlmostEqual(physics.calc_buoyancy(1, 1), 9.81)
        self.assertRaises(physics.calc_buoyancy(0, 1), ValueError)

    def test_float(self):
        self.assertRaises(physics.will_float(0, 0), ValueError)
        self.assertEqual(physics.will_float(1000, 1), True)

    def test(self):
        self.assertEqual

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
