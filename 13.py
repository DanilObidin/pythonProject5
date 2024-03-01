x, y = map(int, input("Введите значения:").split())
print(x%y+1 or y%x+1)
