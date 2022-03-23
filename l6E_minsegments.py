'''
E. Покрытие K отрезками
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Даны n точек на прямой, нужно покрыть их k отрезками одинаковой длины ℓ.
Найдите минимальное ℓ.

Формат ввода
На первой строке
n (1 ≤ n ≤ 10^5) и k (1 ≤ k ≤ n). На второй
n чисел xi ( |xi| ≤ 10^9).
Формат вывода
Минимальное такое ℓ, что точки можно покрыть k отрезками длины ℓ.
Пример
Ввод
6 2
1 2 3 9 8 7
Вывод
2
'''
def check(params, m):
    n, k, x = params
    count = 0
    right = x[0] - 1
    for i in range(n):
        if x[i] > right:
            right = x[i] + m
            count += 1
    if count <= k:
        return True
    else:
        return False
def lbinsearch(l, r, params):
    while (l < r):
        m = (l + r) // 2
        if check(params, m):
            r = m
        else:
            l = m + 1
    return l
n, k = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
maxlen = ((x[n - 1] - x[0]) // k) + 1
params = n, k, x
ans = lbinsearch(0, maxlen, params)
print(ans)
