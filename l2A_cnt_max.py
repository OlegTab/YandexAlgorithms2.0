'''
A. Количество равных максимальному
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Последовательность состоит из натуральных чисел и завершается числом 0. Всего вводится не более 10000 чисел
(не считая завершающего числа 0). Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
Числа, следующие за числом 0, считывать не нужно.
Формат ввода
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит).
Формат вывода
Выведите ответ на задачу.
Пример 1
    Ввод
1
7
9
0
	Вывод
1
'''
a = []
cur = int(input())
max1 = cur
cnt = 1
while (cur != 0):
    a.append(cur)
    cur = int(input())
    if cur > max1:
        max1 = cur
        cnt = 1
    elif cur == max1:
        cnt += 1
print(cnt)