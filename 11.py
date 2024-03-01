import math

a, b, c = map(int, input("Введите стороны треугольника:").split())
a1 = math.acos((b**2 + c**2 - a**2)/(2*c*b))
b1 = math.acos((c**2 + a**2 - b**2)/(2*a*c))
c1 = math.acos((a**2 + b**2 - c**2)/(2*a*b))
print(math.degrees(a1), math.degrees(b1), math.degrees(c1))