import math

def s(a):
    s = 6 * (((a**2) * math.sqrt(3)) / 4)
    return s

print("Введите сторону шестиугольника: ")
print("Площадь шестиугольника: ", s(int(input())))
