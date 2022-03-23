'''
A. Закраска прямой
Ограничение времени	3 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
На числовой прямой окрасили N отрезков. Известны координаты левого и правого концов
каждого отрезка (Li и Ri). Найти длину окрашенной части числовой прямой.

Формат ввода
В первой строке находится число N, в следующих N строках - пары Li и Ri.
Li и Ri - целые, -10^9 ≤ Li ≤ Ri ≤ 10^9, 1 ≤ N ≤ 15 000

Формат вывода
Вывести одно число - длину окрашенной части прямой.

Пример 1
Ввод
1
10 20
Вывод
10
Пример 2
Ввод
1
10 10
Вывод
0
Пример 3
Ввод
5
1 4
10 15
7 12
14 16
3 5
Вывод
13
'''
n = int(input())
points = []
for i in range(n):
    pair = tuple(map(int, input().split()))
    points.append((pair[0], 1))
    points.append((pair[1], -1))
points.sort()
sgmnts = 0
shaded = 0
left = points[0][0]
right = points[0][0]
for point in points:
    if point[1] == 1:
        if sgmnts == 0:
            left = point[0]
        sgmnts += 1
    if point[1] == -1:
        if sgmnts == 1:
            right = point[0]
            shaded += right - left
        sgmnts -= 1
print(shaded)
