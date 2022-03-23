'''
B. Кольцевая линия метро
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Витя работает недалеко от одной из станций кольцевой линии Московского метро, а живет рядом с другой станцией той же линии.
Требуется выяснить, мимо какого наименьшего количества промежуточных станций необходимо проехать Вите по кольцу,
чтобы добраться с работы домой.
Формат ввода
Станции пронумерованы подряд натуральными числами 1, 2, 3, …, N (1-я станция – соседняя с N-й), N не превосходит 100.
Вводятся три числа: сначала N – общее количество станций кольцевой линии, а затем i и j – номера станции,
на которой Витя садится, и станции, на которой он должен выйти. Числа i и j не совпадают. Все числа разделены пробелом.
Формат вывода
Требуется выдать минимальное количество промежуточных станций (не считая станции посадки и высадки),
которые необходимо проехать Вите.

Пример 1
    Ввод
100 5 6
	Вывод
0
Пример 2
Ввод
10 1 9
	Вывод
1
'''
N, i, j = map(int, (input().split()))
sttns = min(abs(i - j) - 1, N - abs(i - j) - 1)
print(str(sttns))
