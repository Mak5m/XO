# num = int(input())
# while num != 0:
#     d = num % 10
#     if d in [5,7,9]:
#         print('y')
#     num //= 10
# def mult_table(number):
#     st = ''
#     for x in range(1, 11):
#         z = number * x
#         st = st + f'{x} * {number} = {z}\n'
#     return st
#
#
# print(mult_table(2))
field = [
    [" ", " ", " "],
    [" ", " ", ""],
    ["", " ", "X"]
]


def check_win():
    for i in range(3):
        sym = []
        for j in range(3):
            sym.append(field[i][j])
        if sym == ['O'] * 3:
            print(' Выиграл O ')
            return True
        if sym == ['X'] * 3:
            print(' Выиграл X ')
            return True
    for i in range(3):
        sym = []
        for j in range(3):
            sym.append(field[j][i])
        if sym == ['O'] * 3:
            print(' Выиграл O ')
            return True
        if sym == ['X'] * 3:
            print(' Выиграл X ')
            return True
    for i in range(3):
        sym = []
        for j in range(3):
            sym.append(field[i][i])
        if sym == ['O'] * 3:
            print(' Выиграл O ')
            return True
        if sym == ['X'] * 3:
            print(' Выиграл X ')
            return True
    for i in range(3):
        sym = []
        for j in range(3):
            sym.append(field[i][2-i])
        if sym == ['O'] * 3:
            print(' Выиграл O ')
            return True
        if sym == ['X'] * 3:
            print(' Выиграл X ')
            return True


print(check_win())
