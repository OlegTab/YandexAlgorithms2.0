'''
E. Форум
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Клуб Юных Хакеров организовал на своем сайте форум. Форум имеет следующую структуру: каждое сообщение
либо начинает новую тему, либо является ответом на какое-либо предыдущее сообщение и принадлежит той же теме.

После нескольких месяцев использования своего форума юных хакеров заинтересовал вопрос - какая тема на их форуме
наиболее популярна. Помогите им выяснить это.

Формат ввода
В первой строке вводится целое число N - количество сообщений в форуме (1 <= N <= 1000). Следующие строки
содержат описание сообщений в хронологическом порядке.
Описание сообщения, которое представляет собой начало новой темы, состоит из трех строк. Первая строка содержит число 0.
Вторая строка содержит название темы. Длина названия не превышает 30 символов. Третья строка содержит текст сообщения.

Описание сообщения, которое является ответом на другое сообщение, состоит из двух строк. Первая строка содержит
целое число - номер сообщения, ответом на которое оно является. Сообщения нумеруются, начиная с единицы.
Ответ всегда появляется позже, чем сообщение, ответом на которое он является. Вторая строка содержит текст сообщения.

Длина каждого из сообщений не превышает 100 символов.

Формат вывода
Выведите название темы, к которой относится наибольшее количество сообщений. Если таких тем несколько,
то выведите первую в хронологическом порядке

Пример 1
    Ввод
7
0
Олимпиада по информатике
Скоро третья командная олимпиада?
0
Новая компьютерная игра
Вышла новая крутая игра!
1
Она пройдет 24 ноября
1
В Санкт-Петербурге и Барнауле
2
Где найти?
4
Примет участие более 50 команд
6
Интересно, какие будут задачи
	Вывод
Олимпиада по информатике
'''
mescount = int(input())
thems = {}
msg = ''
for i in range(mescount):
    head = int(input())
    if head == 0:
        them = input()
        thems[them] = []
        thems[them].append(i + 1)
        msg = input()
    else:
        for t in thems.keys():
            if head in thems[t]:
                thems[t].append(i + 1)
        msg = input()
max_mes = 0
max_them = ''
for t in thems.keys():
    if len(thems[t]) > max_mes:
        max_mes = len(thems[t])
        max_them = t
print(max_them)
