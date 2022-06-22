import unittest
import main

class BubbleSortTest(unittest.TestCase):
    def test1(self):
        expected = [10, 11, 22, 77]
        x = main.Array([77, 22, 10, 11]).BubbleSort()
        self.assertEqual(expected, x)
    def test2(self):
        expected = [1, 1, 1, 1, 1, 1, 1]
        x = main.Array([1, 1, 1, 1, 1, 1, 1]).BubbleSort()
        self.assertEqual(expected, x)
    def test3(self):
        with self.assertRaises(TypeError):
            x = main.Array(["adasc", 0, 5, "100", 9]).BubbleSort()
    def test4(self):
        expected = [-5, -0.01, 0.2857142857142857, 0.999, 5, 800, 800]
        x = main.Array([2/7, 100*8, 6-11, 0.999, 5, 800, -0.3/30]).BubbleSort()
        self.assertEqual(expected, x)
    def test5(self):
        expected = []
        x = main.Array([]).BubbleSort()
        self.assertEqual(expected, x)



