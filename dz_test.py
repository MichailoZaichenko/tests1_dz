import unittest
import program

class MyTestClass(unittest.TestCase):
    def test_sum(self):
        summ = program.Numbers(1,2,3,4,5)
        result = summ.Sum()
        self.assertEqual(15, result)
        summ = program.Numbers(3,6,9,35,345,234)
        result = summ.Sum()
        self.assertEqual(632, result)

    def test_average(self):
        test_average = program.Numbers(1,2,3)
        result = test_average.Average()
        self.assertEqual(2, result)
        test_average = program.Numbers(43,643,13246)
        result = test_average.Average()
        self.assertEqual(4644, result)

    def test_min(self):
        test_min = program.Numbers(1,2,3,234,24,1235,221,0)
        result = test_min.Min()
        self.assertEqual(0, result)
        test_min = program.Numbers(34234,234,43,324,243,12,13)
        result = test_min.Min()
        self.assertEqual(12, result)

    def test_max(self):
        test_max = program.Numbers(1,2,3,435,1321,34)
        result = test_max.Max()
        self.assertEqual(1321, result)
        test_max = program.Numbers(234234,4352,5,34,0,0)
        result = test_max.Max()
        self.assertEqual(234234, result)