st = input()
string = " "
string1 = " "
kol = 0
for i in range(len(st)):
    if st[i] != ".":
        string = string + st[i]
    else:
        kol += 1
        string1 = string.replace("."," ") #читал как заменить(удалить) символ в строке
print("Введенное слово:", st)
print("Обработанное слово:", string1)
print("Колличество '.': ", kol)
      
