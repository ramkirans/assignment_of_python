import sys 

def addition(num1, num2):
    add = num1 + num2
    return add

def subtraction(num1, num2):
    subtraction = num1 - num2
    return subtraction

def multiplication(num1, num2):
    multiplication = num1 * num2
    return multiplication

num1 = int( sys.argv[1] )
operation = sys.argv[2]
num2 = int( sys.argv[3] )

if operation == "addition":
    output = addition(num1, num2)
    print(output)

if operation == "subtraction":
    output = subtraction(num1, num2)
    print(output)

if operation == "multiplication":
    output = multiplication(num1, num2)
    print(output)

