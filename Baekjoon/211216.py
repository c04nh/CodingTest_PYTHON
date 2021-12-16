# 곱셈

num1 = int(input())
num2 = int(input())
units = num2 % 10
tens = num2 // 10 % 10
hundreds = num2 // 100
print(num1 * units)
print(num1 * tens)
print(num1 * hundreds)
print(num1 * num2)