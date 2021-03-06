'''
A. Толя-Карп и новый набор структур, часть 2
Ограничение времени	3 секунды	5 секунд
Ограничение памяти	255Mb	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Толя-Карп запросил для себя n посылок с «Аллигатор-экспресс».

Посылка представляет из себя ящик. Внутри ящика лежит целое число ai.
Номер на ящике di указывает на цвет числа, лежащего внутри.
Толю-Карпа интересует, чему будут равны значения чисел, если сложить между собой все те,
что имеют одинаковый цвет. Напишите, пожалуйста, программу, которая выводит результат.

Формат ввода
В первой строке одно число n (0 ≤ n ≤ 2*10^5).
В следующих n строках заданы по два числа: цвет числа в ящике di и значение числа ai (-10^18 ≤ di, ai ≤ 10^18).
Гарантируется, что сумма чисел одного цвета не превышает 10^18.

Формат вывода
Выведите в порядке возрастания номера цвета пары чисел,
каждая в новой строке: номер цвета и сумму всех чисел данного цвета.

Пример 1
    Ввод
7
1 5
10 -5
1 10
4 -2
4 3
4 1
4 0
	Вывод
1 15
4 2
10 -5
'''
n = int(input())
dict = {}
for i in range(n):
    inc = list(map(int, input().split()))
    if inc[0] not in dict:
        dict[inc[0]] = inc[1]
    else:
        dict[inc[0]] += inc[1]
for key in sorted(dict.keys()):
    print(key, ' ', dict[key])
