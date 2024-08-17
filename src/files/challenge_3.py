
def min_change(list):
    list.sort()
    min_change = 1
    if len(list) > 0:
        for coin in list:
            if coin <= min_change:
                min_change += coin
            else:
                break
        return min_change
    else:
        return min_change


def main():
    print('----------Pruebas Desafio 3')
    coins1 = [5, 7, 1, 1, 2, 3, 22]
    coins2 = [1, 1, 1, 1, 1]
    coins3 = [1, 5, 1, 1, 1, 10, 15, 20, 100]
    print(min_change(coins1))
    print(min_change(coins2))
    print(min_change(coins3))

if __name__ == "__main__":
    main()