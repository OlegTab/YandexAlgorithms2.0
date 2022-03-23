'''
A. Быстрый поиск в массиве
Ограничение времени	3 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дан массив из N целых чисел. Все числа от −10^9 до 10^9
Нужно уметь отвечать на запросы вида “Cколько чисел имеют
значения от L до R?”.

Формат ввода
Число N(1≤N≤10^5). Далее N целых чисел.
Затем число запросов K (1≤K≤10^5).
Далее K пар чисел L,R (−10^9≤L≤R≤10^9) — собственно запросы.

Формат вывода
Выведите K чисел — ответы на запросы.

Пример
Ввод
5
10 1 10 3 4
4
1 10
2 9
3 4
2 2

Вывод:
5 2 2 0
'''

def lbinsearch(l, r, params):
    a, lp = params
    while l < r:
        m = (l + r) // 2
        if a[m] >= lp:
            r = m
        else:
            l = m + 1
    return l
def rbinsearch(l, r, params):
    a, rp = params
    while l < r:
        m = (l + r + 1) // 2
        if a[m] <= rp:
            l = m
        else:
            r = m - 1
    return r
def countelemts(l, r, a):
    if (r < l) or l > a[len(a) - 1] or r < a[0]:
        return 0
    else:
        left = lbinsearch(0, len(a) - 1, (a, l))
        right = rbinsearch(0, len(a) - 1, (a, r))
        return right - left + 1

n = int(input())
a = list(map(int, input().split()))
k = int(input())
querys = []
for i in range(k):
    x1, x2 = map(int, input().split())
    querys.append((x1, x2))
asort = sorted(a)
ans = []
for q in querys:
    count = countelemts(q[0], q[1], asort)
    ans.append(count)
print(*ans)
