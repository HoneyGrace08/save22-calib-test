def add (x, y):
        return x + y

def subract (x, y):
        return x - y

def multiply (x, y):
        return x * y

def divide (x, y):
        x = float(x)
        y = float(y)
        return x / y

def inputOne(num1):
        return num1

def inputTwo (num2):
        return num2

def operator (ope, num1 , num2):
          
        if ope == '+':
            print "Output:",num1,"+",num2,"=", add(num1,num2)
        elif ope == '-':
            print "Output:",num1,"-",num2,"=", subtract(num1,num2)
        elif ope == '*':
            print "Output:",num1,"*",num2,"=", multiply(num1,num2)
        elif ope == '/':
            print "Output:",num1,"/",num2,"=", divide(num1,num2)
        else:
            print ("Invalid input")

def main():
        print "---CALCULATOR----"

        num1 = input ("First number: ")
        ope = raw_input("Operand:")
        num2 = input ("Second number: ")
        inputOne(num1)
        inputOne(num2)
        operator(ope, num1, num2)

if __name__ == '__main__':
  main()
