# подключаем нужные библиотеки
import requests
from bs4 import BeautifulSoup as BS
# задание 1
#листы куда будем складывать данные
rank=[]
fatalities=[]
magnitudes =[]
events =[]
locations=[]
date=[]
# создадим общий лист для облегчения навигации
Cammon=[rank, fatalities, magnitudes, events, locations, date]
# url сайта
url = 'https://en.m.wikipedia.org/wiki/Lists_of_20th-century_earthquakes'
# запрос на получение html страницы
r = requests.get(url)
# находим все заголовки таблицы
t_head = BS(r.content, 'html.parser').table.find_all('th')
#добовляим их в листы
k=0
for chl1 in t_head:
	Cammon[k].append( chl1.text.strip())
	k+=1
# находим все строки таблицы		
t_data = BS(r.content, 'html.parser').table.find_all('tr')
# проходим по каждой строке
for chl1 in t_data:
	k=0
# добавляем данные ячеек в соотв листы
	for i in chl1.find_all('td'):
		Cammon[k].append(i.text.strip())
		k+=1

# выводим результаты
print(events, '\n')
print(magnitudes, '\n')
print(locations, '\n')

	
# задание 2
# словарь для залания
earthquakes = dict()

# одновременно отбрасываем Ms и
# приводим все к флоту, а также
# заполняем словарь
for i in range(1,len(magnitudes)):
	g = magnitudes[i].split()
	magnitudes[i]=float(g[0])
	earthquakes[events[i]] = [locations[i], magnitudes[i]]

# тут функция по заданию
def info_even(even):
	print(f'{even} happened in {earthquakes[even][0]} with magnitude  of {earthquakes[even][1]}')

# цикл для всех событий
for i in range(1, len(events)):
	info_even(events[i])
	
# функция по подсчету стран	
def count_loc(loc):
	return locations.count(loc)

# счет для всех стран
# приводим к сету, чтобы избавиться
# от дубликатов	
for i in set(locations):
	print(i, count_loc(i))