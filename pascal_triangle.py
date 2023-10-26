def print_pascal_triangle(triangle_haight):
    list1 = []
    for i in range(triangle_haight):
        # Слой треугольника
        list1.append([])
        # Добавили первую единицу
        list1[i].append(1)
        for j in range(1, i):
            list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])
        # Добавили последнюю единицу
        if i != 0:
            list1[i].append(1)
    # Вывод треугольника
    for i in range(triangle_haight):
        for j in range(0, i + 1):
            print(list1[i][j], end="  ")
        print()


if __name__ == '__main__':
    try:
        num = int(input("Enter the height of the triangle: "))
        print_pascal_triangle(num)
    except ValueError:
        print("Incorrect number of lines entered")