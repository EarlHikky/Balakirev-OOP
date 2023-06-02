import random


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self):
        self.pole = tuple(tuple(Cell() for j in range(3)) for i in range(3))

    def show(self):
        for i in range(3):
            for j in range(3):
                print(self.pole[i][j].value, end=' ')
            print()
        print()

    def human_go(self):
        while True:
            i, j = map(int, input("Введите координаты клетки (через пробел): ").split())
            if not self.pole[i][j]:
                self.pole[i][j].value = TicTacToe.HUMAN_X
                break
            else:
                print("Клетка занята! Попробуйте еще раз.")

    def computer_go(self):
        free_cells = [(i, j) for i in range(3) for j in range(3) if not self.pole[i][j]]
        if free_cells:
            i, j = random.choice(free_cells)
            self.pole[i][j].value = TicTacToe.COMPUTER_O

    @property
    def is_human_win(self):
        for i in range(3):
            if self.pole[i][0].value == self.pole[i][1].value == self.pole[i][2].value == TicTacToe.HUMAN_X:
                return True
            if self.pole[0][i].value == self.pole[1][i].value == self.pole[2][i].value == TicTacToe.HUMAN_X:
                return True
        if self.pole[0][0].value == self.pole[1][1].value == self.pole[2][2].value == TicTacToe.HUMAN_X:
            return True
        if self.pole[2][0].value == self.pole[1][1].value == self.pole[0][2].value == TicTacToe.HUMAN_X:
            return True
        return False

    @property
    def is_computer_win(self):
        for i in range(3):
            if self.pole[i][0].value == self.pole[i][1].value == self.pole[i][2].value == TicTacToe.COMPUTER_O:
                return True
            if self.pole[0][i].value == self.pole[1][i].value == self.pole[2][i].value == TicTacToe.COMPUTER_O:
                return True
        if self.pole[0][0].value == self.pole[1][1].value == self.pole[2][2].value == TicTacToe.COMPUTER_O:
            return True
        if self.pole[2][0].value == self.pole[1][1].value == self.pole[0][2].value == TicTacToe.COMPUTER_O:
            return True
        return False

game = TicTacToe()
# game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")