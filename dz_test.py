import unittest
import program

class MyTestClass(unittest.TestCase):
    def test_sum(self):
        summ = program.Numbers(1,2,3)
        result = summ.Sum()
        self.assertEqual(6, result)
        summ = program.Numbers(3,6,9)
        result = summ.Sum()
        self.assertEqual(18, result)

    def test_average(self):
        test_average = program.Numbers(1,2,3)
        result = test_average.Average()
        self.assertEqual(2, result)
        test_average = program.Numbers(43,643,13246)
        result = test_average.Average()
        self.assertEqual(4644, result)

    def test_min(self):
        test_min = program.Numbers(1,2,3)
        result = test_min.Min()
        self.assertEqual(1, result)
        test_min = program.Numbers(34234,234,43)
        result = test_min.Min()
        self.assertEqual(43, result)

    def test_max(self):
        test_max = program.Numbers(1,2,3)
        result = test_max.Max()
        self.assertEqual(3, result)
        test_max = program.Numbers(234234,4352,5)
        result = test_max.Max()
        self.assertEqual(234234, result)