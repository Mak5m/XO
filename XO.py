def greeting_():
    print("  Приветствуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


def show():
    print(f'   0 1 2')
    for i in range(3):
        print(f' {i} {' '.join(field[i])}')
    print()


def check_win():
    for i in range(3):
        sym = []
        for j in range(3):
            sym.append(field[i][j])
        if sym == ['X'] * 3:
            print(' Выиграл X ')
            return True
        if sym == ['O'] * 3:
            print(' Выиграл O ')
            return True
    for i in range(3):
        sym = []
        for j in range(3):
            sym.append(field[j][i])
        if sym == ['X'] * 3:
            print(' Выиграл X ')
            return True
        if sym == ['O'] * 3:
            print(' Выиграл O ')
            return True
    for i in range(3):
        sym = []
        sym.append(field[i][i])
        if sym == ['X'] * 3:
            print(' Выиграл X ')
            return True
        if sym == ['O'] * 3:
            print(' Выиграл O ')
            return True
    for i in range(3):
        sym = []
        sym.append(field[i][2 - i])
        if sym == ['X'] * 3:
            print(' Выиграл X ')
            return True
        if sym == ['O'] * 3:
            print(' Выиграл O ')
            return True
    return False


def ask():
    while True:
        x_y = input(' Введите координаты ячейки ').split()
        if len(x_y) != 2:
            print(' Введите 2 координаты! ')
            continue

        x, y = x_y[0], x_y[1]

        if not (x.isdigit()) or not (y.isdigit()):
            print(' Введите числа!')
            continue

        x, y = int(x), int(y)

        if not 0 <= x <= 2 or not 0 <= y <= 2:
            print(' Координаты вне диапазона! ')
            continue

        if field[x][y] != '-':
            print(' Поле занято! ')
            continue

        return x, y


greeting_()
field = [['-'] * 3 for _ in range(3)]


def game():
    count = 0
    while True:
        count += 1
        show()
        if count % 2 != 0:
            print(' Ходит  X ')
        else:
            print(' Ходит 0 ')

        x, y = ask()

        if count % 2 != 0:
            field[x][y] = 'X'
        else:
            field[x][y] = 'O'

        if check_win():
            break

        if count == 9:
            print(' Ничья ')
            break


game()
replay = input(' Ещё разок? ')
if replay == 'да':
    field = [['-'] * 3 for _ in range(3)]
    game()
else:
    print(' Увидимся в следующий раз. ')