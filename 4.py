x, y, n = map(int, input("Введите значения:").split())
r = int(x*n+y/100*n)
k = y*n%100
print(f"{r} руб, {k} коп")