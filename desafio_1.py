def delete_digits(list, s):
    final_list = []
    for number in list[::-1]:
        temporal = ''
        if number <= 100:
            for digit_str in str(number):
                digit = int(digit_str)
                if digit < s:
                    temporal += digit_str
            if not temporal == '':
                final_list.append(int(temporal))
    return final_list


def main():
    print('----------Pruebas Desafio 1')
    name = 'Manuela Arcila Cruz'
    md5_hash = '90f950c7d82232b3e35dc63532d3a7267a3b93fb'
    s = 9
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [10, 20, 30, 40]
    list3 = [6]
    list4 = [66]
    list5 = [65]
    list6 = [6, 2, 1]
    list7 = [60, 6, 5, 4, 3, 2, 7, 7, 29, 1]
    print(delete_digits(list1, s))
    print(delete_digits(list2, s))
    print(delete_digits(list3, s))
    print(delete_digits(list4, s))
    print(delete_digits(list5, s))
    print(delete_digits(list6, s))
    print(delete_digits(list7, s))


if __name__ == "__main__":
    main()
