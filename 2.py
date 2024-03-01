s = int(input("Введите число:"))
hours = s//3600
minutes = (s%3600)//60
seconds = s%60
print(f"{seconds} секунд, {minutes} минут, {hours} часов")

