import numpy as np


def main_function(n):
    # Блок кода с генерацией массивов случайной размерности
    # *****************************************************

    main_list = []
    for j in range(n):
        internal_list = []
        for i in range(1, n+1):
            k = [np.random.randint(1, n)]
            print(k)
        for i in range(k):
            internal_list.append(np.random.randint(1, 100))

        main_list.append(internal_list)
        
    # *****************************************************
    # Раскоментив эту строку можно посмотреть сгенерированные массивы
    # print("First generate:", main_list)

    # Блок кода с просмотром длины массивов, по условию задачи не должно быть одинаковых длин
    # *****************************************************

    d3 = [len(i) for i in main_list]
    print('Список длинн:', d3)
    for i in range(n):
        for j in range(i, n - 1):
            if d3[i] == d3[j + 1]:
                print('Есть одинаковые длины, введите число снова')
                quit()

    # *****************************************************

    # Блок кода с сортировкой массивов в соответствии заданию
    # *****************************************************
    for i in range(n):
        if i % 2 == 0:
            main_list[i].sort(key=None, reverse=False)

        elif i % 2 != 0:
            main_list[i].sort(key=None, reverse=True)

    # *****************************************************

    return main_list


sorted_massive = main_function(int(input("Введите число: ")))
print(sorted_massive)
