n = int(input()) # длина массива
arr = []
mn = 999999999999
for i in range(n):
    arr.append(int(input()))    #заполнили массив
for i in arr:  # поиск минимального элемента списка
    if mn > i:
        mn = i
print("Индекс минимального элемента: ", arr.index(mn)) # вывод индекса минимального элемента    
