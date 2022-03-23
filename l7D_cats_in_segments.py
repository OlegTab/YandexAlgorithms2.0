'''
D. Наполненность котятами
Ограничение времени	2 секунды
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
На прямой в точках a1,a2,…,an (возможно, совпадающих) сидят n котят.
На той же прямой лежат m отрезков [l1,r1],[l2,r2],…,[lm,rm].
Нужно для каждого отрезка узнать его наполненность котятами —
сколько котят сидит на отрезке.
Формат ввода
На первой строке n и m (1≤n,m≤10^5).
На второй строке n целых чисел ai (0≤ai≤10^9).
Следующие m строк содержат пары целых чисел li,ri (0≤li≤ri≤10^9).
Формат вывода
Выведите m целых чисел. i-е число — наполненность котятами i-го отрезка
Примеры входных данных ниже кода.
'''
n, m = map(int, input().split())
eos_cats = []
cats = list(map(int, input().split()))
for i in range(m):
    l, r = map(int, input().split())
    eos_cats.append((l, -1, i))
    eos_cats.append((r, 1, i))
for cat in cats:
    eos_cats.append((cat, 0))
eos_cats.sort()
cats_in_sgmnts = [0] * m
cnt_cats = 0
for i in range(len(eos_cats)):
    if eos_cats[i][1] == -1: cats_in_sgmnts[eos_cats[i][2]] = cnt_cats
    elif eos_cats[i][1] == 0: cnt_cats += 1
    elif eos_cats[i][1] == 1: cats_in_sgmnts[eos_cats[i][2]] = cnt_cats - cats_in_sgmnts[eos_cats[i][2]]
print(*cats_in_sgmnts)

'''
4 3
10 5 7 2
11 15
1 3
5 7
ответ: 0 1 2

3 4
3 4 2
11 15
2 7
1 5
6 9
ответ: 0 3 3 0

8 6
5 10 15 20 25 30 40 45
11 21
27 42
3 17
12 20
1 7
50 52
ответ: 2 2 3 2 1 0
'''