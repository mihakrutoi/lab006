list = []
for part in input("Введите числа через пробел: ").split():
    list.append(part)

if list == []:
    print("Нет данных")

else:
    max = list[0]
    for num in list:
        if int(num) > int(max):
            max = num
    list_index = []
    for index, num in enumerate(list):
        if num == max:
            list_index.append(index)
    print(list_index)