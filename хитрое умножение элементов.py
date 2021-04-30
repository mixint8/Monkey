def mk_new_arr(arr):
	new_arr = list()
	first_zero = -1
	count_zero = 0
	mul = 1
# проходим по массиву
# с подсчетом общего произведения
# и общего числа нулей
	for i in range(len(arr)):
		if arr[i] ==0 and count_zero < 2:
			 first_zero = i
			 count_zero += 1
		else:
			mul *= arr[i]
# если ноль встречается более 1 раза
# то произведение будет равно 0 
# в любом случае
		if count_zero == 2:
			break
# заполняем новый массив
	for i in range(len(arr)):
# если есть нули в массиве
# то стоит обработать два случая
# когда он один - то везде будет ноль
# кромн позиции 0
# и когда более двух нулей
# тогда везде будут нули
		if count_zero >0:
			if count_zero == 2 or first_zero != i:
				new_arr.append(0)
			else:
				new_arr.append(mul)
# в ином случае просто делим общее 
# произв на элемент массива
		else:
				new_arr.append(mul//arr[i])
	return new_arr


s = list(map(int, input().split()))
print(mk_new_arr(s))