arr = []
n = int(input())
pl = []
ot = []
for i in range(n):
    arr.append(int(input()))
for i in arr:
    if i < 0:
        ot.append(i)
for i in arr:
    if i > 0:
        pl.append(i)
print("Массив с положительными элементами: ", pl)
print()
print("Массив с отрицательными элементами: ", ot)        