att, cmp, yds, td, int = map(int, input("Введите значения:").split())
a = (cmp/att - 0.3)*5
b = (yds/att - 3)*0.25
c = (td/att)*20
d = 2.375 - (int/att*25)
pr = ((a+b+c+d)/6)*100
print(pr)
