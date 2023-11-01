
import math
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
operator = input("Введите операцию: ")
if operator == "+":
    print(num1+num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
elif operator == "-":
    print(num1-num2)
elif operator == "**":
    print(num1**num2)
elif operator == "sqrt":
    print(round(math.sqrt(num1), 4), round(math.sqrt(num2), 4))
elif operator == "pow4":
    print(round((num1**1/4), 4), round((num2**1/4), 4))
