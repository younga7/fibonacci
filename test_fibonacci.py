# CS362 test_fibonacci
# Alex Young
# 2/25/2021
# Run this file using python3 test_fibonacci.py
# This program holds funtions to unit test for the fibonacci sequence

import unittest
import fibonacci

class TestFibo(unittest.TestCase):
    def test_add(self):
        self.assertEqual(fibonacci.series(0), 0)
        self.assertEqual(fibonacci.series(1), 1)
        self.assertEqual(fibonacci.series(5), 5)
        self.assertEqual(fibonacci.series(8), 21)
        self.assertEqual(fibonacci.series(-1), "Negative Input")
        self.assertEqual(fibonacci.series("0"), "Type Error")

class TestFactorial(unittest.TestCase):
    def test_add(self):
        self.assertEqual(fibonacci.factorial(0), 1)
        self.assertEqual(fibonacci.factorial(1), 1)
        self.assertEqual(fibonacci.factorial(5), 120)
        self.assertEqual(fibonacci.factorial(8), 40320)
        self.assertEqual(fibonacci.factorial(-1), "Negative Input")
        self.assertEqual(fibonacci.factorial("0"), "Type Error")

def test_fibo():
    assert fibonacci.series(9) == 34
    assert fibonacci.series(14) == 377
    assert fibonacci.series(2) == 1
    assert fibonacci.series(-1) == "Negative Input"
    assert fibonacci.series("9") == "Type Error"

def test_factorial():
    assert fibonacci.factorial(9) == 362880
    assert fibonacci.factorial(14) == 87178291200
    assert fibonacci.factorial(2) == 2
    assert fibonacci.factorial(-1) == "Negative Input"
    assert fibonacci.factorial("9") == "Type Error"    

if __name__ == '__main__':
    unittest.main(verbosity=2)