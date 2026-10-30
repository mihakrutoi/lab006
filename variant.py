#Вариант 12
list = []
for part in input("Введите числа через пробел: ").split():
    list.append(part)

result = []
for num in list:
    if int(num) % 2 == 0 and int(num) > 0:
        result.append(num)

kolvo = 0
for num in result:
    kolvo += 1

sum = 0
for num in result:
    sum += int(num)

copy_result = sorted(result.copy())
print(f"Изначальный список: {result}, количество: {kolvo}, сумма: {sum}, по возрастанию: {copy_result}")