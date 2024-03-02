import math

x1 = float(input("X1 : "))
y1 = float(input("Y1 : "))
x2 = float(input("X2 : "))
y2 = float(input("Y2 : "))
x3 = float(input("X3 : "))
y3 = float(input("Y3 : "))
a = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
b = math.sqrt(((x1 - x3) ** 2) + ((y1 - y3) ** 2))
c = math.sqrt(((x2 - x3) ** 2) + ((y2 - y3) ** 2))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Периметр : {p}\nПлошад : {s}")
