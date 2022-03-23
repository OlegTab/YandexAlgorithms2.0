'''
C. Частотный анализ
Ограничение времени	2 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
Слова должны быть отсортированы по убыванию их количества появления в тексте,
а при одинаковой частоте появления — в лексикографическом порядке.

Формат ввода
Вводится текст.

Формат вывода
Выведите ответ на задачу.

Пример 1
    Ввод
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme
	Вывод
damme
is
name
van
bond
claude
hi
my
james
jean
what
your
'''
dic = {}
s = input().strip()
while True:
    try:
        s = list(s.split())
        for word in s:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
        s = input().strip()
    except: break
words = list((-dic[k], k) for k in dic)
for word in sorted(words):
    print(word[1])
