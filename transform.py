list = []
for part in input("Введите числа через пробел: ").split():
    list.append(part)

list2 = []

for num in list:
    if int(num) < 0:
        list2.append(int(num) * -1)
    else:
        list2.append(num)

print(f"1 список: {list}, 2 список: {list2}")