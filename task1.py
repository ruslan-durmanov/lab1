numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
average = 0
# TODO заменить значение пропущенного элемента средним арифметическим
for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = 0;
        index_none = i
        break
average = sum(numbers)/len(numbers)
numbers[index_none] = average
print("Измененный список:", numbers)
