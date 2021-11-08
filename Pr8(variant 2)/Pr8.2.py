n = int(input('Введите размер матрицы: '))
arr = [] 
for i in range(n):
    b = []
    for j in range(n):
        b.append(int(input())) #Ввод массива
    arr.append(b)        

print()

for i in range(n):
    for j in range(n):         #Вывод исходного массива
        print(arr[i][j], end = ' ')
    print() 

for i in range(len(arr)):
    arr[i][-1], arr[i][0] = arr[i][0], arr[i][-1] #Замена столбцов

print()

for i in range(n):
    for j in range(n):         #Вывод изменненого массива
        print(arr[i][j], end = ' ')
    print() 