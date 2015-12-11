import calculator
import unittest


class TestCalculator(unittest.TestCase):

    def test_Add(self):
        self.assertEqual(calculator.add(1,1),2)
        with self.assertRaises(TypeError):
            calculator.add('1',1)

    def test_Subtract(self):
        self.assertEqual(calculator.subtract(1,1),0)


    def test_Multiply(self):
        self.assertEqual(calculator.multiply(1,1),1)


    def test_Divide(self):
        self.assertEqual(calculator.divide(1,1),1)

        with self.assertRaises(ZeroDivisionError):
            calculator.divide(10,0)


    def test_operator(self):
        self.assertEqual(calculator.operator('+', 13,11),24)
        self.assertEqual(calculator.operator('-', 15,-10),25)
        self.assertEqual(calculator.operator('/', 16,2),8)
        self.assertEqual(calculator.operator('*', 7,-3),-21)
        self.assertEqual(calculator.operator(1, 'AB',3), None)
        

        



if __name__ == '__main__':
    unittest.main()
