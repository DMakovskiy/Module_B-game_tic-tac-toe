# Функция печати игрового поля
def print_field(f):
    print('   0  1  2')
    for i in range(len(f)):
        print(str(i), *f[i])


# Функция принимает координаты хода крестика или нолика и модифицирует игровое поле
def user_input(x, f):
    while True:
        if x == 'X':
            turn = input('Введите координаты крестика через пробел: ').split()
        else:
            turn = input('Введите координаты нолика через пробел: ').split()
        # Проверка количества координат
        if len(turn) != 2:
            print('Координат должно быть двое')
        # Проверка, являются ли координаты числами
        elif not (turn[0].isdigit() and turn[1].isdigit()):
            print('Координаты должны быть числами')
        # Проверка диапазона координат
        else:
            turn = list(map(int,turn))
            if turn[0] not in [0,1,2] or turn[1] not in [0,1,2]:
                print('Неправильные координаты')
            # Проверка того, что ход приходится на незанятую клетку
            elif f[turn[0]][turn[1]] != ' -':
                print('Эта клетка уже занята')
            else:
                break
    if x == 'X':
        f[turn[0]][turn[1]] = ' X'
    else:
        f[turn[0]][turn[1]] = ' O'


# Функция проверки победы
def check_win(f):
    # Печать стандартных фраз в случае победы
    def motivator():
        print('Но не отчаивайтесь! Решение есть!')
        print('Программирование на Python повышает IQ примерно на 2 единицы в день!')

    # Проверка диагоналей
    if f[0][0] == f[1][1] == f[2][2] == ' X' or f[0][2] == f[1][1] == f[2][0] == ' X':
        print('Крестики победили!')
        print('IQ ноликов оставляет желать лучшего :(')
        motivator()
        return True
    elif f[0][0] == f[1][1] == f[2][2] == ' O' or f[0][2] == f[1][1] == f[2][0] == ' O':
        print('Нолики победили!')
        print('IQ крестиков оставляет желать лучшего :(')
        motivator()
        return True
    # Проверка вертикалей и горизонталей
    else:
        # Создание транспонированной матрицы из исходного поля
        transposed = [[row[_] for row in f] for _ in range(3)]
        for i in range(3):
            if f[i].count(' X') == 3 or transposed[i].count(' X') == 3:
                print('Крестики победили!')
                print('IQ ноликов оставляет желать лучшего :(')
                motivator()
                return True
            elif f[i].count(' O') == 3 or transposed[i].count(' O') == 3:
                print('Нолики победили!')
                print('IQ крестиков оставляет желать лучшего :(')
                motivator()
                return True
    return False

field = [[' -']*3, [' -']*3, [' -']*3]
count = 0
print('ПРОВЕРЬ СВОЙ IQ - СЫГРАЙ В КРЕСТИКИ-НОЛИКИ!')
print_field(field)
while True:
    if count % 2 == 0:
        user = 'X'
    else:
        user = 'O'
    user_input(user, field)
    print_field(field)
    if check_win(field):
        break
    count += 1
    if count == 9:
        print('Ничья')
        break




