#Day - 1

print('Making Calculator')

a = int(input("Enter the value of 1st digit::"))
b = int(input("Enter the value of 2nd digit::"))

print("What you want? Use operator *, +, - , /")
operator = input('Enter Operator')

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


if (operator == '+'):
    print('Addition Operation::',add(a,b))
elif(operator == '-'):
    print('Substraction Operation::',sub(a,b))
elif(operator == '*'):
    print('Multiplication Operation::',mul(a,b))
elif(operator == '/'):
    print('Division Operation::',div(a,b))
else:
    print('Wrong Operator Used')