('''
addition
subtraction
multiplication
division
''')
num1=int(input("enter the value of num1"))
num2=int(input("enter the value of num2"))
opr=input("enter the value of opr")
if opr == "+":
    print(num1 + num2)
elif opr == "-":
    print(num1 - num2)
elif opr == "*":
    print(num1 * num2)
elif opr == "/":
    print(num1 / num2)
else:
    print("invalid opr")
