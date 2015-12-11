def add (num1, num2):
        if not isinstance(num1, int): #checking #value datatype
                return None
        return num1 + num2

def subtract (num1, num2):
        return num1 - num2

def multiply (num1, num2):
        return num1 * num2

def divide (num1, num2):
        num1 = float(num1)
        num2 = float(num2)
        return num1 / num2

def inputOne():
        return int(raw_input ("First number: "))

def inputTwo ():
        return int(raw_input ("Second number: "))

def input_operator ():
        return raw_input ("Operator: ")
    

def operator (ope, num1 , num2):
      
        if ope == '+':
            return add(num1,num2)
        elif ope == '-':
            return subtract(num1,num2)
        elif ope == '*':
            return multiply(num1,num2)
        elif ope == '/':
            return divide(num1,num2)
        else:
            print ("Invalid input")

        return None
            
def output(ope, num1, num2, ans):
    
        return '{} {} {} = {}'.format(num1, ope, num2, ans)

    
def main():
        print "---CALCULATOR----"
        num1 = inputOne()
        ope = input_operator()
        num2 = inputTwo()
        ans = operator(ope, num1, num2)
        print output(ope, num1, num2, ans)

if __name__ == '__main__':
  main()
