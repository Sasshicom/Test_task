import numpy as np

if __name__ == '__main__':
    def main_function(n):
        main_list = []
        for j in range(n):
            internal_list = []
            k = np.random.randint(1, 10)
            for i in range(k):
                internal_list.append(np.random.randint(1, 100))
            main_list.append(internal_list)

        #print("First generate:", main_list)
        #print()
        d3 = [len(i) for i in main_list]
        print('Список длинн:', d3)
        for i in range(n):
            for j in range(i, n-1):
                if d3[i] == d3[j+1]:
                    print('Есть одинаковые длины, введите число снова')
                    quit()

        for i in range(n):
            if i % 2 == 0:
                main_list[i].sort(key=None, reverse=False)

            elif i % 2 != 0:
                main_list[i].sort(key=None, reverse=True)

        return main_list

sorted_massive = main_function(int(input("Введите число: ")))
print(sorted_massive)
