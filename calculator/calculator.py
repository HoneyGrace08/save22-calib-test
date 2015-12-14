def add (num1, num2):
##        if not isinstance(num1, int): #checking #value datatype
##                return None
        return num1 + num2

def subtract (num1, num2):
        return num1 - num2

def multiply (num1, num2):
        return num1 * num2

def divide (num1, num2):
        num1 = float(num1)
        num2 = float(num2)
        return num1 / num2

def inputOne(input = raw_input):
        return int(input ("First number: "))

def inputTwo (input = raw_input):
        return int(input ("Second number: "))

def input_operator (input=raw_input):
        return input ("Operator: ")
    

def operator (ope, num1 , num2):
      
##        if ope == '+':
##            return add(num1,num2)
##        elif ope == '-':
##            return subtract(num1,num2)
##        elif ope == '*':
##            return multiply(num1,num2)
##        elif ope == '/':
##            return divide(num1,num2)
##        else:
##            #print ("Invalid input")
##            return None
        functions = {'+':add,
                  '-':subtract,
                  '*':multiply,
                  '/':divide }
        
        funcs = functions.get(ope, None)

        if funcs:
                return funcs(num1, num2)
        return None
            
def output(ope, num1, num2, ans):
    
        return '{} {} {} = {}'.format(num1, ope, num2, ans)


def main():
        print "---CALCULATOR----"
##        input1 = inputOne()
##        ope = input_operator()
##        input2 = inputTwo()
##        ans = operator(ope, input1, input2)
##        print output(ope, input1, input2, ans)

        while True:
                try:
                    input1 = int(inputOne())
                    break
                except ValueError:
                    pass                        
                    #print "Invalid Input"

        while True:
                try:
                    ope = input_operator()
                    break
                except ValueError:
                    pass  
                    #print "Invalid Input"

        while True:
                try:
                    input2 = int(inputTwo())
                    break
                except ValueError:
                     pass
                    #print "Invalid Input"

        try:
                ans = operator(ope, input1, input2)
                print output(ope, input1, input2, ans)
        except ZeroDivisionError:
                print 'Cant divide by zero'

        
if __name__ == '__main__':
  main()
