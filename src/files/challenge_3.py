
def min_change(list):
    list.sort()
    min_value = 1
    if len(list) > 0:
        for coin in list:
            if coin <= min_value:
                min_value += coin
            else:
                break
        return min_value
    else:
        return min_value


def main():
    print('----------Pruebas Desafio 3')
    coins1 = [5, 7, 1, 1, 2, 3, 22]
    coins2 = [1, 1, 1, 1, 1]
    coins3 = [1, 5, 1, 1, 1, 10, 15, 20, 100]
    coins4 = [2, 4, 5]
    coins5 = [1, 2, 6]
    print(min_change(coins1))
    print(min_change(coins2))
    print(min_change(coins3))
    print(min_change(coins4))
    print(min_change(coins5))

if __name__ == "__main__":
    main()

