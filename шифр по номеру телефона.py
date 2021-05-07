# словарь для хранения значений на
# кнопках
buttons = {    
                        '2':'abc',
						'3':'def',
						'4':'ghi',
						'5':'jkl',
						'6':'mno',
						'7':'pqrs',
						'8':'tuv',
						'9':'wxyz'
				}
				
				
# рекурсионная функция 
# для перебора комбинаций
def MakeCombinationsList(str, ls, n, cur_mass):
# если длина текущего массива равно
# длине строки на входе, то одна
# комбинация найдена и ее можно
# добавить в лист ответа
	if n == len(str): ls.append(''.join(cur_mass))
# в противном случае для n-ой позиции
# перебираем все возможные
# символы и вызываем функцию для
# подбора n+1 символа
	else:
		for i in buttons[str[n]]:
			cur_mass[n] = i
			MakeCombinationsList(str, ls, n+1, cur_mass)
			
			
# обертка для рекурс. функции
def GetPasswordCombinations(input_):
# лист ответов для заполнения
	ls = list()
# создаем массив для хранения 
# текущей комбинации
	cur_mass = [i for i in range(len(input_))]
# запускаем рекурс. функция 
	MakeCombinationsList(input_, ls, 0, cur_mass)
	return ls
	
	
print(GetPasswordCombinations(input()))
