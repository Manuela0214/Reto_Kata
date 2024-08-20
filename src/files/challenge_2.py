def get_squares(list, s):
    final_array = []
    max_range = s * 10 + s
    if len(list) > 0:
        for num in list:
            square = num ** 2
            if 0 <= square <= max_range:
                final_array.append(square)
        return bubble_sort(final_array)
    else:
        return 'la lista esta vacía'


def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def main():
    print('----------Pruebas Desafio 2')
    # name = 'Manuela Arcila Cruz'
    # md5_hash = '8be80bd961c26a4191fac0afc8948cea'
    s = 8
    array1 = [1, 2, 3, 5, 6, 8, 9]
    array2 = [-2, -1]
    array3 = [-6, -5, 0, 5, 6]
    array4 = [-10, 10]
    array5 = [7, 10, 9, 5, 2]
    print(get_squares(array1, s))
    print(get_squares(array2, s))
    print(get_squares(array3, s))
    print(get_squares(array4, s))
    print(get_squares(array5, s))
    print(get_squares([], s))

if __name__ == "__main__":
    main()
