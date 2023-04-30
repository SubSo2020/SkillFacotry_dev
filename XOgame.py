name_first = input('Введите свое имя, если будешь играть за "Х"')
name_twice = input('Введите свое имя, если будешь играть за "О"')
#1размер поля для игры
cells = [1,2,3,4,5,6,7,8,9]

#1.1обрисовка поля в терминале с помощью цикла for
def painted_cells(cells):
    for i in range(3):
        print (cells[0+i*3], cells[1+i*3], cells[2+i*3])

# функция проверки выигрышной комбинации
def check_win(cells):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if cells[each[0]] == cells[each[1]] == cells[each[2]]:
            return cells[each[0]]
    return False



#функция для ввода крестика или нолика на игровом поле
def take_input(player_choise):
    valid = False
    while not valid:
        player_answer = input("Выбери цифру куда поставить " + player_choise + "?")
        try:               #если число, игра продолжается
            player_answer = int(player_answer)
        except:             #если введена буква или символ выводится надпись и все по новой
            print ("Ты точно ввел число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(cells[player_answer-1]) not in "XO"):        #Если числа попадают в промежуток от 1 до 9
                cells[player_answer-1] = player_choise           #происходит запись Х или О в игровом поле
                valid = True
            else:
                print ("Сюда нельзя, клетка уже занята")         #если цифра попадает на занятую позицию
        else:
            print ("Ошибка. Введи число от 1 до 9 чтобы сходить.")     #если число не попадает в промежуток от 1 до 9


def start_game(cells):
    step = 0
    win = False
    while not win:
        painted_cells(cells)
        if step % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        step += 1
        if step > 4:
            tmp = check_win(cells)
            if tmp == 'X':
                print (name_first + ", выиграл!")
            elif tmp == 'O':
                print (name_twice + ", выиграл!")
            win = True
            break
        if step == 9:
            print ("Ничья!")
            break

print('Начнем игру!')
start_game(cells)
