numbers = []

for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

if numbers == []:
    print("Нет данных")
else:
    kolvo = 0
    for num in numbers:
        kolvo += 1
    

    sum = 0
    for num in numbers:
        sum += int(num)

    min = numbers[0]
    max = numbers[0]
    for num in numbers:
        if num < min:
            min = num

    for num in numbers:
        if num > max:
            max = num
    
    average = sum/kolvo

    print(f"Количество: {kolvo}, сумма: {sum}, минимум: {min}, максимум: {max}, среднее: {average:.2f}")