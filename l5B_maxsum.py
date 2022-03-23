'''
B. Максимальная сумма
Ограничение времени	3 секунды
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В этой задаче вам требуется найти непустой отрезок массива с максимальной суммой.
Формат ввода
В первой строке входных данных записано единственное число
n  (1≤n≤3⋅10^5) -  размер массива.
Во второй строке записано n целых чисел ai (−10^9≤ai≤10^9) - сам массив.

Формат вывода
Выведите одно число - максимальную сумму на отрезке в данном массиве.
Пример 1
    Ввод
4
1 2 3 4
	Вывод
10
'''
n = int(input())
a = list(map(int, input().split()))
prefixsum = [0] * (n + 1)
maxsum = min(a)
cursum = maxsum
l = 0
for i in range(1, n + 1):
    prefixsum[i] += prefixsum[i - 1] + a[i - 1]
    if prefixsum[i - 1] < prefixsum[l]:
        l = i - 1
    cursum = prefixsum[i] - prefixsum[l]
    maxsum = max(cursum, maxsum)
print(maxsum)
print(prefixsum)
'''
13
20 30 -51 10 8 -1 6 1 3 -20 35 7 5

13
20 20 -40 10 8 -1 6 1 3 -20 30 7 5
'''