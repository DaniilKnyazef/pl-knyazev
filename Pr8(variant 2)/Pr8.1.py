N = int(input('Введите размер матрицы: '))
arr = [] 
res_column = []
res_line = []
line = 0
column = 0

for i in range(N):
    b = []
    for j in range(N):
        b.append(int(input())) #ввод массива
    arr.append(b)        

print()

for i in range(N):
    for j in range(N):         #вывод массива
        print(arr[i][j], end = ' ')
    print() 


for i in range(N):
    for j in range(N): #счет cтрок
        line += arr[i][j]
    res_line.append(line)
    line = 0

for j in range(N):
    for i in range(N): #счет столбцов
        column += arr[i][j]
    res_column.append(column)
    column = 0


flag = True
for i in res_column:
    for j in res_column:
        if i != j:
            flag = False        # проверка равенства столбцов между собой
            break
    if flag == False:
        print('Нет равенства столбцов')
        break   
if flag == True:
    print('Столбцы равны')    


flag1 = True
for i in res_line:
    for j in res_line:
        if i != j:
            flag1 = False        # проверка равенства строк между собой
            break
    if flag1 == False:
        print('Нет равенства строк')
        break   
if flag1 == True:
    print('Строки равны') 

if flag == True and flag1 == True:
    print('Матрица является магическим квадратом')   
else:
    print('Матрица не является магическим квадратом')         
               
           
           