def rools():
    print("Добро пожаловать в игру")
    print("Введите через пробел коордиты поля")
    print("где первая координата это строка")
    print("а втроря столбец")

field = [["-" for _ in range(3)] for _ in range(3)]

def show_field():
    print("   0   1   2")
    for i, row in enumerate(field):
        print(f"{i}  {'   '.join(row)}")

def input_coord():
    while True:
        coords = input("Введите координаты: ").split()

        if len(coords) !=2:
            print("Введите 2 координаты")
            continue

        a, b = coords

        if not (a.isdigit()) or not (b.isdigit()):
            print("Введите числа")
            continue

        a, b = int(a), int(b)

        if 0 > a or 2 < a or 0 > b or 2 < b:
            print("Числа в не диапозона")
            continue

        if field[a][b] != "-":
            print("Клетка занята")
            continue
        return a, b


def check_win():
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coord in win_coord:
        symbols = []
        for c in coord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


def game():
    rools()
    step = 0
    while True:
        step += 1
        if step == 1:
            print("Первые ходят Х")
        show_field()
        if step % 2 == 0:
            print("Ход 0")
        if step % 2 == 1 and step > 2:
            print("Ход X")

        a, b = input_coord()

        if step % 2 == 0:
            field[a][b] = "0"
        if step % 2 == 1:
            field[a][b] = "X"
        if step == 9:
            print("Ничья")
            break
        if check_win():
            break
    return show_field()
game()

