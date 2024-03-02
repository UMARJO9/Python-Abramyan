import math

x1 = float(input("X1 : "))
y1 = float(input("Y1 : "))
x2 = float(input("X2 : "))
y2 = float(input("Y2 : "))
ras = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Растояние : {ras}")
