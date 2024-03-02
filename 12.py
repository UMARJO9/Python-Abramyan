import math

a = float(input("A : "))
b = float(input("B : "))
c = math.sqrt((a ** 2) + (b ** 2))
p = a + b + c
print(f"Гипотенуза = {c}\nПериметр = {p}")
