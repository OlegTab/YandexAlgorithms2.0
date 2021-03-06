'''
D. Вырубка леса
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Фермер Николай нанял двух лесорубов: Дмитрия и Федора, чтобы вырубить лес,
на месте которого должно быть кукурузное поле. В лесу растут X деревьев.
Дмитрий срубает по A деревьев в день, но каждый K-й день он отдыхает и не срубает ни одного дерева.
Таким образом, Дмитрий отдыхает в K-й, 2K-й, 3K-й день, и т.д.
Федор срубает по B деревьев в день, но каждый M-й день он отдыхает и не срубает ни одного дерева.
Таким образом, Федор отдыхает в M-й, 2M-й, 3M-й день, и т.д.
Лесорубы работают параллельно и, таким образом, в дни, когда никто из них не отдыхает, они срубают A + B деревьев,
в дни, когда отдыхает только Федор — A деревьев, а в дни, когда отдыхает только Дмитрий — B деревьев.
В дни, когда оба лесоруба отдыхают, ни одно дерево не срубается.
Фермер Николай хочет понять, за сколько дней лесорубы срубят все деревья, и он сможет засеять кукурузное поле.
Требуется написать программу, которая по заданным целым числам A, K, B, M и X определяет,
за сколько дней все деревья в лесу будут вырублены.

Формат ввода
Входной файл содержит пять целых чисел, разделенных пробелами: A, K, B, M и X
(1 ≤ A, B ≤ 10^9 , 2 ≤ K, M ≤ 10^18, 1 ≤ X ≤ 10^18).

Формат вывода
Выходной файл должен содержать одно целое число — искомое количество дней.

Пример 1
Ввод
1 2 1 3 10
Вывод
8

Пример 2
Ввод
1 2 1 3 11
Вывод
9

Пример 3
Ввод
19 3 14 6 113
Вывод
4

2 4 3 3 25
7

1 2 2 2 6
3
'''
def check(params, n):
    a, a_wknd, b, b_wknd, x = params
    if (a * (n - n // a_wknd) + b * (n - n // b_wknd)) >= x:
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
a, a_wknd, b, b_wknd, x = tuple(map(int, input().split()))
params = a, a_wknd, b, b_wknd, x
ans = lbinsearch(1, x, params)
print(ans)


