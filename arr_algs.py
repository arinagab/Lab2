mas = [4, 17, 2, 3, 1040, 256, 90, 18]


def poisk_min(mas):
    i = 0
    min = mas[0]
    while i < len(mas):
        if mas[i] < min:
            min = i
            min = mas[i]
        i = i + 1
    return min


def sred_mas(mas):
    s = 0
    for z in mas:
        s = s + z
    s = s / len(mas)
    return s


print ("1) Минимум в массиве:", (poisk_min(mas)))
print ("2) Среднее арифметическое в массиве:", (sred_mas(mas)))