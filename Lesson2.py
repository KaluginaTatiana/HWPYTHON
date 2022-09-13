# Task1 Монетки

n = int(input('Введите число монет от 1 до 100 включительно: '))
num_orel, num_reshka = 0, 0 
for i in range(n):
    k = int(input('Если монета лежит решкой вверх - введите 1, если монета лежит орлом вверх - введите 0: '))
    if k == 0:
        num_orel += 1
    elif k == 1:
        num_reshka += 1
    else:
        print('Ошибка. Вводим только 0 или 1.') 
        break
if num_orel <= num_reshka:
    print(num_orel)
else:
    print(num_reshka)


# # Task2 Сумма
n = int(input('Введите число от 1 до 10000: '))
sum = 0
for i in range(1, n + 1):
    sum += i
print(f'Сумма чисел от 1 до {n} = {sum}.')

# Task3 Минимальный делитель
n = int(input('Введите число от 2 до 1000000: '))
min_delitel = 0
if n % 2 == 0:
    min_delitel = 2
else:
    i = 3
    while i ** 2 <= n:
        if n % i == 0:
            min_delitel = i
        i += 2
if min_delitel == 0:
    min_delitel = n
print('Минимальный делитель = ', min_delitel)  

# Task4 Шеренга

num = 10
spisok = [155, 154, 154, 152, 150, 148, 148, 146, 146, 145]
rost_Petya = int(input('Введите рост Пети в сантиметрах: '))
print('Рост детей в порядке убывания.')
print(spisok)
if rost_Petya <= spisok[num - 1]:
    mesto = num + 1
elif rost_Petya > spisok[0]:
    mesto = 1
else:
    for i in range(num):
        if rost_Petya <= spisok[i] and rost_Petya > spisok[i + 1]:
            mesto = i + 2
print('Петино место в шеренге: ', mesto)

# Task5 Сбор черники
num = 10
k = [45, 8, 7, 9, 15, 1, 19, 32, 11, 22]
max = 0
print('Урожайность кустов черники')
print(k)
for i in range(num):
    if k[i - 2] + k[i - 1] + k[i] > max:
        max = k[i - 2] + k[i - 1] + k[i]
print('Максимальное число ягод черники ', max)
