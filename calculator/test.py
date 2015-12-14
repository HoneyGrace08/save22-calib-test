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
        
        
    def test_output(self):
        self.assertEqual(calculator.output('+', 13,11,24), "13 + 11 = 24")
        

    def test_op(self):
         self.assertEqual(calculator.input_operator(self.mock_input),1)

    def test_inputOne(self):
         self.assertEqual(calculator.inputOne(self.mock_input),1)

    def test_inputTwo(self):
         self.assertEqual(calculator.inputTwo(self.mock_input),1)
        
    def mock_input(self,prompt):
        return 1

    def mock_ope(self,prompt):
        return '+'

    def mock_input_zero(self,prompt):
        return 0

    def mock_input_string(self,prompt):
        return 'A'

        
    def test_success(self):
        num1 = calculator.inputOne(self.mock_input)
        ope = calculator.input_operator(self.mock_ope)        
        num2 = calculator.inputTwo(self.mock_input)
        ans = calculator.operator(ope, num1, num2)
        final = calculator.output(ope, num1, num2, ans)
        self.assertEqual(final, "1 + 1 = 2")


    def test_DividedByZero (self):
       
        input1 =calculator.inputOne(self.mock_input)
        input2 = calculator.inputTwo(self.mock_input_zero)
        
        try:
               self.assertEqual(calculator.divide(input1,input2),None)
               #self.assertEqual((input1 / input2), None )
        except ZeroDivisionError:
                pass
                #print 'Cant divide by zero'
        else:
                self.fail('Did not see ZeroDivisionError')
        
    
    def test_StringInputs (self):
         try:
               self.assertEqual(calculator.inputOne(self.mock_input_string),1)
               self.assertEqual(calculator.input_operator(self.mock_ope),'+')
               self.assertEqual(calculator.inputTwo(self.mock_input_string), 1) 
                
         except ValueError:
                pass
                #print "Invalid Input"
         else:
                self.fail('Did not see StringInputs')


    def test_IntAndString(self):
        
         try:
               self.assertEqual(calculator.inputOne(self.mock_input_string),1)
               self.assertEqual(calculator.input_operator(self.mock_ope),'+')
               self.assertEqual(calculator.inputTwo(self.mock_input), 1) 
                
         except ValueError:
                pass
                #print "Invalid Input"
         else:
                self.fail('Did not see Integer and Strings')
   


if __name__ == '__main__':
    unittest.main()
