'''
D. Выборы Государственной Думы
Ограничение времени	2 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Статья 83 закона “О выборах депутатов Государственной Думы Федерального Собрания Российской Федерации”
определяет следующий алгоритм пропорционального распределения мест в парламенте.
Необходимо распределить 450 мест между партиями, участвовавших в выборах. Сначала подсчитывается сумма
голосов избирателей, поданных за каждую партию и подсчитывается сумма голосов, поданных за все партии.
Эта сумма делится на 450, получается величина, называемая “первое избирательное частное”
(смысл первого избирательного частного - это количество голосов избирателей,
которое необходимо набрать для получения одного места в парламенте).

Далее каждая партия получает столько мест в парламенте, чему равна целая часть от деления
числа голосов за данную партию на первое избирательное частное.

Если после первого раунда распределения мест сумма количества мест, отданных партиям,
меньше 450, то оставшиеся места передаются по одному партиям, в порядке убывания дробной части
частного от деления числа голосов за данную партию на первое избирательное частное.
Если же для двух партий эти дробные части равны, то преимущество отдается той партии,
которая получила большее число голосов.

Формат ввода
На вход программе подается список партий, участвовавших в выборах. Каждая строка входного файла
содержит название партии (строка, возможно, содержащая пробелы), затем, через пробел, количество голосов,
полученных данной партией – число, не превосходящее 108.

Формат вывода
Программа должна вывести названия всех партий и количество голосов в парламенте, полученных данной партией.
Названия необходимо выводить в том же порядке, в котором они шли во входных данных.

Пример 1
    Ввод
Party One 100000
Party Two 200000
Party Three 400000
	Вывод
Party One 64
Party Two 129
Party Three 257
'''
voices = {}
s = input().strip()
while True:
    try:
        line = list(s.split())
        p = " ".join(line[0:(len(line) - 1)])
        v = line[len(line) - 1]
        if p not in voices:
            voices[p] = int(v)
        else:
            voices[p] += int(v)
        s = input().strip()
    except: break
summ = sum(voices.values())
feld = summ / 450
fracs = sorted(list((voices[k]/feld - voices[k]//feld, k) for k in voices), reverse = True)
places = dict((k, int(voices[k]//feld)) for k in voices)
sumplaces = sum(places.values())
if sumplaces  < 450:
    for i in range(450 - sumplaces):
        if (i != 450 - sumplaces - 1):
            if fracs[i][1] == fracs[i+1][1]:
                if (places[fracs[i][1]] > places[fracs[i+1][1]]):
                    places[fracs[i][1]] += 1
                else:
                    places[fracs[i+1][1]] += 1
            else: places[fracs[i][1]] += 1
        else:
            places[fracs[i][1]] += 1
        if summ == 450:
            break
for k in places:
    print(k, places[k])
