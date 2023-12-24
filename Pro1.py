
# TASK : 1

def add(a, b):
  return print( "Addition of ",a ," & ",b," = ",a+b)

def sub(a,b):
  return print( "Subtraction of ",a ," & ",b," = ",a-b)

def mul(a,b):
  return print( "Multiplication of ",a ," & ",b," = ",a*b)

def div(a,b):
  return print( "Division of ",a ," & ",b," = ",a/b)

def module(a,b):
  return print( "Module of ",a ," & ",b," = ",a%b)

def exponential(a,b):
  return print( "Exponential of ",a ," & ",b," = ",a**b)

def floordivision(a,b):
  return print( "Floor Division",a ," & ",b," = ",a//b)

def default(a,b):
  return "Incorrect Choice"


switcher = {
    1: add,
    2: sub,
    3: mul,
    4: div,
    5: module,
    6: exponential,
    7: floordivision
}

def switch(operation, a, b):
  return switcher.get(operation, default)(a, b)
print('''\nEnter your Choice\n
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Module 
6. Exponential
7. Floor Division\n''')

choice = int(input("Select operation : "))
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print (switch(choice, a, b))