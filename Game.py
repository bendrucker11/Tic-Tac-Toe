import random


def cpu_row_contains_2(lst):
    for i in range(3):
        if (lst[i][0] == "o" and lst[i][1] == "o" and lst[i][2] != "x") or (
                lst[i][0] == "o" and lst[i][2] == "o" and lst[i][1] != "x") or (
                lst[i][2] == "o" and lst[i][1] == "o" and lst[i][0] != "x"):
            return i, True
    return -1, False


def user_row_contains_2(lst):
    if (lst[0] == "x" and lst[1] == "x" and lst[2] != "o") or (lst[0] == "x" and lst[2] == "x" and lst[1] != "o") or (
            lst[2] == "x" and lst[1] == "x" and lst[0] != "o"):
        return True
    return False


def cpu_col_contains_2(lst):
    # col 1
    if (lst[0][0] == "o" and lst[1][0] == "o" and lst[2][0] != "x") or (lst[0][0] == "o" and lst[2][0] == "o" and lst[1][0] != "x") or (lst[2][0] == "o" and lst[1][0] == "o" and lst[0][0] != "x"):
        return 0, True
    if (lst[0][1] == "o" and lst[1][1] == "o" and lst[2][1] != "x") or (lst[0][1] == "o" and lst[2][1] == "o" and lst[1][1] != "x") or (lst[2][1] == "o" and lst[1][1] == "o" and lst[0][1] != "x"):
        return 1, True
    if (lst[0][2] == "o" and lst[1][2] == "o" and lst[2][2] != "x") or (lst[0][2] == "o" and lst[2][2] == "o" and lst[1][2] != "x") or (lst[2][2] == "o" and lst[1][2] == "o" and lst[0][2] != "x"):
        return 2, True
    return -1, False


def user_col_contains_2(lst):
    for i in range(3):
        x_count = 0
        non_o_count = 0
        for j in range(3):
            if lst[j][i] == "x":
                x_count += 1
            elif lst[j][i] != "o":
                non_o_count += 1
        if x_count == 2 and non_o_count == 1:
            return i, True
    return -1, False


def cpu_diag_contains_2(lst):
    if (lst[0][0] == "o" and lst[1][1] == "o" and lst[2][2] != "x") or (
            lst[0][0] == "o" and lst[2][2] == "o" and lst[1][1] != "x") or (
            lst[2][2] == "o" and lst[1][1] == "o" and lst[0][0] != "x"):
        return "l_r", True
    if (lst[0][2] == "o" and lst[1][1] == "o" and lst[2][0] != "x") or (
            lst[0][2] == "o" and lst[2][0] == "o" and lst[1][1] != "x") or (
            lst[2][0] == "o" and lst[1][1] == "o" and lst[0][2] != "x"):
        return "r_l", True
    return "", False


def user_diag_contains_2(lst):
    if (lst[0][0] == "x" and lst[1][1] == "x" and lst[2][2] != "o") or (
            lst[0][0] == "x" and lst[2][2] == "x" and lst[1][1] != "o") or (
            lst[2][2] == "x" and lst[1][1] == "x" and lst[0][0] != "o"):
        return "l_r", True
    if (lst[0][2] == "x" and lst[1][1] == "x" and lst[2][0] != "o") or (
            lst[0][2] == "x" and lst[2][0] == "x" and lst[1][1] != "o") or (
            lst[2][0] == "x" and lst[1][1] == "x" and lst[0][2] != "o"):
        return "r_l", True
    return "", False


class Board:
    board = []
    move_count = 0
    defensive_game = ""
    offensive_game = ""

    def __init__(self):
        count = 1
        for i in range(3):
            self.board.append([])
            for j in range(3):
                self.board[i].append(str(count))
                count += 1

    def to_string(self):
        s = ""
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                s += "  " + self.board[i][j] + " "
                if j <= 1:
                    s += "|"
            if i <= 1:
                s += "\n" + "____|____|_____\n"

        return s

    def enter_move(self, move, x_or_o):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == move:
                    self.board[i][j] = x_or_o
        self.move_count += 1

    def cpu_brink_of_win(self):
        i, flag = cpu_row_contains_2(self.board)
        if flag:
            if self.board[i][0] != "o":
                self.board[i][0] = "o"
            elif self.board[i][1] != "o":
                self.board[i][1] = "o"
            else:
                self.board[i][2] = "o"
            return True
        col, flag = cpu_col_contains_2(self.board)
        if flag:
            if self.board[0][col] != "o":
                self.board[0][col] = "o"
            elif self.board[1][col] != "o":
                self.board[1][col] = "o"
            else:
                self.board[2][col] = "o"
            return True
        diag, flag2 = cpu_diag_contains_2(self.board)
        if flag2:
            if diag == "l_r":
                if self.board[0][0] != "o":
                    self.board[0][0] = "o"
                elif self.board[1][1] != "o":
                    self.board[0][0] = "o"
                else:
                    self.board[2][2] = "o"
            else:
                if self.board[0][2] != "o":
                    self.board[0][2] = "o"
                elif self.board[1][1] != "o":
                    self.board[1][1] = "o"
                else:
                    self.board[2][0] = "o"
            return True
        return False

    def user_brink_of_win(self):
        for i in range(3):
            if user_row_contains_2(self.board[i]):
                if self.board[i][0] != "x":
                    self.board[i][0] = "o"
                elif self.board[i][1] != "x":
                    self.board[i][1] = "o"
                else:
                    self.board[i][2] = "o"
                return True
        col, flag = user_col_contains_2(self.board)
        if flag:
            if self.board[0][col] != "x":
                self.board[0][col] = "o"
            elif self.board[1][col] != "x":
                self.board[1][col] = "o"
            else:
                self.board[2][col] = "o"
            return True
        diag, flag2 = user_diag_contains_2(self.board)
        if flag2:
            if diag == "l_r":
                if self.board[0][0] != "x":
                    self.board[0][0] = "o"
                elif self.board[1][1] != "x":
                    self.board[0][0] = "o"
                else:
                    self.board[2][2] = "o"
            else:
                if self.board[0][2] != "x":
                    self.board[0][2] = "o"
                elif self.board[1][1] != "x":
                    self.board[1][1] = "o"
                else:
                    self.board[2][0] = "o"
            return True
        return False

    def cpu_move(self):
        if self.move_count == 0:
            r = random.randint(0, 2)
            if r == 0:
                self.offensive_game = "center game"
                self.board[1][1] = "o"
            elif r == 1:
                self.offensive_game = "corner game"
                self.board[0][0] = "o"
            else:
                self.offensive_game = "edge game"
                self.board[0][1] = "o"
            self.move_count += 1

        elif self.move_count == 1:
            if self.board[1][1] == "x":
                self.board[0][0] = "o"
                self.defensive_game = "cpu: top left corner; user: center"
            elif self.board[0][0] == "x":
                self.board[1][1] = "o"
                self.defensive_game = "cpu: center; user: top left corner"
            elif self.board[0][2] == "x":
                self.board[1][1] = "o"
                self.defensive_game = "cpu: center; user: top right corner"
            elif self.board[2][0] == "x":
                self.board[1][1] = "o"
                self.defensive_game = "cpu: center; user: bottom left corner"
            elif self.board[2][2] == "x":
                self.board[1][1] = "o"
                self.defensive_game = "cpu: center; user: bottom right corner"
            elif self.board[0][1] == "x":
                self.board[1][1] = "o"
                self.defensive_game = "cpu: center; user: top edge"
            elif self.board[1][0] == "x":
                self.board[1][1] = "o"
                self.defensive_game = "cpu: center; user: left edge"
            elif self.board[0][2] == "x":
                self.board[1][1] = "o"
                self.defensive_game = "cpu: center; user: right edge"
            elif self.board[2][1] == "x":
                self.board[1][1] = "o"
                self.defensive_game = "cpu: center; user: bottom edge"
            self.move_count += 1

        elif self.move_count == 2:
            if self.offensive_game == "center game":
                if self.board[0][0] == "x":
                    self.board[2][2] = "o"
                    self.offensive_game = "cpu: center, bottom right corner; user: top left corner"
                elif self.board[0][2] == "x":
                    self.board[2][0] = "o"
                    self.offensive_game = "cpu: center, bottom left corner; user: top right corner"
                elif self.board[2][0] == "x":
                    self.board[0][2] = "o"
                    self.offensive_game = "cpu: center, top right corner; user: bottom left corner"
                elif self.board[2][2] == "x":
                    self.board[0][0] = "o"
                    self.offensive_game = "cpu: center, top left corner; user: bottom right corner"
                elif self.board[0][1] == "x":
                    self.board[0][2] = "o"
                    self.offensive_game = "cpu: center, top right corner; user: top edge"
                elif self.board[1][0] == "x":
                    self.board[0][2] = "o"
                    self.offensive_game = "cpu: center, top right corner; user: left edge"
                elif self.board[1][2] == "x":
                    self.board[0][2] = "o"
                    self.offensive_game = "cpu: center, top right corner; user: right edge"
                elif self.board[2][1] == "x":
                    self.board[0][2] = "o"
                    self.offensive_game = "cpu: center, top right corner; user: bottom edge"

            elif self.offensive_game == "corner game":
                if self.board[1][1] == "x":
                    self.board[2][2] = "o"
                    self.offensive_game = "cpu: top left corner, bottom right corner; user: center"
                elif self.board[0][2] == "x":
                    self.board[2][2] = "o"
                    self.offensive_game = "cpu: top left corner, bottom right corner; user: top right corner"
                elif self.board[2][0] == "x":
                    self.board[2][2] = "o"
                    self.offensive_game = "cpu: top left corner, bottom right corner; user: bottom left corner"
                elif self.board[2][2] == "x":
                    self.board[0][2] = "o"
                    self.offensive_game = "cpu: top left corner, top right corner; user: bottom right corner"
                elif self.board[0][1] == "x":
                    self.board[2][0] = "o"
                    self.offensive_game = "cpu: top left corner, bottom left corner; user: top edge"
                elif self.board[1][0] == "x":
                    self.board[0][2] = "o"
                    self.offensive_game = "cpu: top left corner, top right corner; user: left edge"
                elif self.board[2][1] == "x":
                    self.board[2][0] = "o"
                    self.offensive_game = "cpu: top left corner, bottom left corner; user: bottom edge"
                elif self.board[1][2] == "x":
                    self.board[2][0] = "o"
                    self.offensive_game = "cpu: top left corner, bottom left corner; user: right edge"
            else:
                if self.board[1][1] == "x":
                    self.board[2][0] = "o"
                    self.offensive_game = "cpu: top edge, bottom left corner; user: center"
                elif self.board[0][0] == "x":
                    self.board[2][0] = "o"
                    self.offensive_game = "cpu: top edge, bottom left corner; user: top left corner"
                elif self.board[0][2] == "x":
                    self.board[2][2] = "o"
                    self.offensive_game = "cpu: top edge, bottom right corner; user: top right corner"
                elif self.board[2][0] == "x":
                    self.board[0][0] = "o"
                    self.offensive_game = "cpu: top edge, top left corner; user: bottom left corner"
                elif self.board[2][2] == "x":
                    self.board[0][2] = "o"
                    self.offensive_game = "cpu: top edge, top right corner; user: bottom right corner"
                elif self.board[1][0] == "x":
                    self.board[1][1] = "o"
                    self.offensive_game = "cpu: top edge, center; user: left edge"
                elif self.board[1][2] == "x":
                    self.board[1][1] = "o"
                    self.offensive_game = "cpu: top edge, center; user: right edge"
                elif self.board[2][1] == "x":
                    self.board[0][2] = "o"
                    self.offensive_game = "cpu: top edge, bottom left corner; user: bottom edge"
            self.move_count += 1

        elif self.move_count == 3:
            if self.user_brink_of_win():
                pass
            else:
                if self.defensive_game == "cpu: top left corner; user: center":
                    self.board[0][2] = "o"
                    self.defensive_game = "cpu: top left corner, top right corner; user: center, bottom right corner"
                elif self.defensive_game == "cpu: center; user: top left corner":
                    if self.board[2][2] == "x":
                        self.board[0][1] = "o"
                        self.defensive_game = "cpu: center, top edge; user: top left corner, bottom right corner"
                    elif self.board[2][1] == "x":
                        self.board[1][2] = "o"
                        self.defensive_game = "cpu: center, right edge; user: top left corner, bottom edge"
                    elif self.board[1][2] == "x":
                        self.board[2][1] = "o"
                        self.defensive_game = "cpu: center, bottom edge; user: top left corner, right edge"
                elif self.defensive_game == "cpu: center; user: top right corner":
                    if self.board[2][0] == "x":
                        self.board[0][1] = "o"
                        self.defensive_game = "cpu: center, top edge; user: top right corner, bottom left corner"
                    elif self.board[2][1] == "x":
                        self.board[1][0] = "o"
                        self.defensive_game = "cpu: center, left edge; user: top right corner, bottom edge"
                    elif self.board[1][0] == "x":
                        self.board[2][1] = "o"
                        self.defensive_game = "cpu: center, bottom edge; user: top right corner, left edge"
                elif self.defensive_game == "cpu: center; user: bottom left corner":
                    if self.board[0][2] == "x":
                        self.board[1][2] = "o"
                        self.defensive_game = "cpu: center, right edge; user: bottom left corner, top right corner"
                    elif self.board[0][1] == "x":
                        self.board[1][2] = "o"
                        self.defensive_game = "cpu: center, right edge; user: bottom left corner, top edge"
                    elif self.board[1][2] == "x":
                        self.board[0][1] = "o"
                        self.defensive_game = "cpu: center, top edge; user: bottom left corner, right edge"
                elif self.defensive_game == "cpu: center; user: bottom right corner":
                    if self.board[0][0] == "x":
                        self.board[1][2] = "o"
                        self.defensive_game = "cpu: center, right edge; user: bottom right corner, top left corner"
                    elif self.board[0][1] == "x":
                        self.board[1][0] = "o"
                        self.defensive_game = "cpu: center, left edge; user: bottom right corner, top edge"
                    elif self.board[1][0] == "x":
                        self.board[0][1] = "o"
                        self.defensive_game = "cpu: center, top edge; user: bottom right corner, left edge"
                elif self.defensive_game == "cpu: center; user: top edge":
                    if self.board[1][0] == "x":
                        self.board[0][2] = "o"
                        self.defensive_game = "cpu: center, top right corner; user: top edge, left edge"
                    elif self.board[1][2] == "x":
                        self.board[0][0] = "o"
                        self.defensive_game = "cpu: center, top left corner; user: top edge, right edge"
                    elif self.board[2][0] == "x":
                        self.board[1][2] = "o"
                        self.defensive_game = "cpu: center, right edge; user: top edge, bottom left corner"
                    elif self.board[2][1] == "x":
                        self.board[2][2] = "o"
                        self.defensive_game = "cpu: center, bottom right corner; user: top edge, bottom edge"
                    elif self.board[2][2] == "x":
                        self.board[1][0] = "o"
                        self.defensive_game = "cpu: center, left edge; user: top edge, bottom right corner"
                elif self.defensive_game == "cpu: center; user: left edge":
                    if self.board[0][1] == "x":
                        self.board[0][2] = "o"
                        self.defensive_game = "cpu: center, top right corner; user: left edge, top edge"
                    elif self.board[0][2] == "x":
                        self.board[2][1] = "o"
                        self.defensive_game = "cpu: center, bottom edge; user: left edge, top right corner"
                    elif self.board[1][2] == "x":
                        self.board[2][2] = "o"
                        self.defensive_game = "cpu: center, bottom right corner; user: left edge, right edge"
                    elif self.board[2][2] == "x":
                        self.board[0][1] = "o"
                        self.defensive_game = "cpu: center, top edge; user: left edge, bottom right corner"
                    elif self.board[2][1] == "x":
                        self.board[0][0] = "o"
                        self.defensive_game = "cpu: center, top left corner; user: left edge, bottom edge"
                elif self.defensive_game == "cpu: center; user: right edge":
                    if self.board[0][1] == "x":
                        self.board[0][0] = "o"
                        self.defensive_game = "cpu: center, top left corner; user: right edge, top edge"
                    elif self.board[0][0] == "x":
                        self.board[2][1] = "o"
                        self.defensive_game = "cpu: center, bottom edge; user: right edge, top left corner"
                    elif self.board[1][0] == "x":
                        self.board[2][1] = "o"
                        self.defensive_game = "cpu: center, bottom edge; user: right edge, left edge"
                    elif self.board[2][10] == "x":
                        self.board[0][1] = "o"
                        self.defensive_game = "cpu: center, top edge; user: right edge, bottom left corner"
                    elif self.board[2][1] == "x":
                        self.board[0][2] = "o"
                        self.defensive_game = "cpu: center, top right corner; user: right edge, bottom edge"
                elif self.defensive_game == "cpu: center; user: bottom edge":
                    if self.board[1][0] == "x":
                        self.board[0][0] = "o"
                        self.defensive_game = "cpu: center, top left corner; user: bottom edge, left edge"
                    elif self.board[0][0] == "x":
                        self.board[1][2] = "o"
                        self.defensive_game = "cpu: center, right edge; user: bottom edge, top left corner"
                    elif self.board[0][1] == "x":
                        self.board[1][2] = "o"
                        self.defensive_game = "cpu: center, right edge; user: bottom edge, top edge"
                    elif self.board[0][2] == "x":
                        self.board[1][0] = "o"
                        self.defensive_game = "cpu: center, left edge; user: bottom edge, top right corner"
                    elif self.board[1][2] == "x":
                        self.board[2][0] = "o"
                        self.defensive_game = "cpu: center, bottom left corner; user: bottom edge, right edge"
            self.move_count += 1

        elif self.move_count == 4:
            if self.cpu_brink_of_win():
                pass
            elif self.user_brink_of_win():
                pass
            else:
                if self.offensive_game == "cpu: center, bottom right corner; user: top left corner":
                    if self.board[1][2] == "x":
                        self.board[2][1] = "o"
                        self.offensive_game = "cpu: center, bottom right corner, bottom edge; user: top left corner, right edge"
                    elif self.board[2][1] == "x":
                        self.board[1][2] = "o"
                        self.offensive_game = "cpu: center, bottom right corner, right edge; user: top left corner, bottom edge"
                elif self.offensive_game == "cpu: center, bottom left corner; user: top right corner":
                    if self.board[2][1] == "x":
                        self.board[1][0] = "o"
                        self.offensive_game = "cpu: center, bottom right corner, left edge; user: top left corner, bottom edge"
                    elif self.board[1][0] == "x":
                        self.board[2][1] = "o"
                        self.offensive_game = "cpu: center, bottom right corner, bottom edge; user: top left corner, left edge"
                elif self.offensive_game == "cpu: center, top right corner; user: bottom left corner":
                    if self.board[1][2] == "x":
                        self.board[0][1] = "o"
                        self.offensive_game = "cpu: center, bottom right corner, top edge; user: top left corner, right edge"
                    elif self.board[0][1] == "x":
                        self.board[1][2] = "o"
                        self.offensive_game = "cpu: center, bottom right corner, right edge; user: top left corner, top edge"
                elif self.offensive_game == "cpu: center, top left corner; user: bottom right corner":
                    if self.board[0][1] == "x":
                        self.board[1][0] = "o"
                        self.offensive_game = "cpu: center, bottom right corner, left edge; user: top left corner, top edge"
                    elif self.board[1][0] == "x":
                        self.board[0][1] = "o"
                        self.offensive_game = "cpu: center, bottom right corner, top edge; user: top left corner, left edge"
                elif self.offensive_game == "cpu: center, top right corner; user: top edge":
                    self.board[2][2] = "o"
                    self.offensive_game = "cpu: center, top right corner, bottom right corner; user: top edge, bottom left corner"
                elif self.offensive_game == "cpu: top edge, bottom left corner; user: center":
                    if self.board[0][2] == "x":
                        self.board[0][0] = "o"
                        self.offensive_game = "cpu: top edge, bottom left corner, top left corner; user: center, top right corner"
                    elif self.board[2][1] == "x":
                        self.board[0][0] = "o"
                        self.offensive_game = "cpu: top edge, bottom left corner, top left corner; user: center, bottom edge"
                elif self.offensive_game == "cpu: top edge, bottom left corner; user: top left corner":
                    if self.board[1][0] == "x":
                        self.board[1][1] = "o"
                        self.offensive_game = "cpu: top edge, bottom left corner, center; user: top left corner, left edge"
                    elif self.board[2][1] == "x":
                        self.board[1][1] = "o"
                        self.offensive_game = "cpu: top edge, bottom left corner, center; user: top left corner, bottom edge"
                    elif self.board[1][2] == "x":
                        self.board[1][1] = "o"
                        self.offensive_game = "cpu: top edge, bottom left corner, center; user: top left corner, right edge"
                    elif self.board[0][2] == "x":
                        self.board[2][1] = "o"
                        self.offensive_game = "cpu: top edge, bottom left corner, bottom edge; user: top left corner, top right corner"
                elif self.offensive_game == "cpu: top edge, bottom right corner; user: top right corner":
                    if self.board[1][2] == "x":
                        self.board[1][1] = "o"
                        self.offensive_game = "cpu: top edge, bottom right corner, center; user: top right corner, right edge"
                    elif self.board[2][1] == "x":
                        self.board[0][2] = "o"
                        self.offensive_game = "cpu: top edge, bottom right corner, top left corner; user: top right corner, bottom edge"
                    elif self.board[1][0] == "x":
                        self.board[1][1] = "o"
                        self.offensive_game = "cpu: top edge, bottom right corner, center; user: top right corner, left edge"
                    elif self.board[0][0] == "x":
                        self.board[2][1] = "o"
                        self.offensive_game = "cpu: top edge, bottom right corner, bottom edge; user: top right corner, top left corner"
                elif self.offensive_game == "cpu: top edge, center; user: left edge":
                    if self.board[2][1] == "x":
                        self.board[0][2] = "o"
                        self.offensive_game = "cpu: top edge, center, top right corner; user: left edge, bottom edge"
                elif self.offensive_game == "cpu: top edge, center; user: right edge":
                    if self.board[2][1] == "x":
                        self.board[0][2] = "o"
                        self.offensive_game = "cpu: top edge, center, top right corner; user: right edge, bottom edge"
                elif self.offensive_game == "cpu: top edge, bottom left corner; user: bottom edge":
                    if self.board[0][0] == "x":
                        self.board[0][2] = "o"
                        self.offensive_game = "cpu: top edge, bottom left corner, top right corner; user: bottom edge, top left corner"
                    elif self.board[0][2] == "x":
                        self.board[1][0] = "o"
                        self.offensive_game = "cpu: top edge, bottom left corner, left edge; user: bottom edge, top right corner"
                    elif self.board[1][0] == "x":
                        self.board[0][2] = "o"
                        self.offensive_game = "cpu: top edge, bottom left corner, top right corner; user: bottom edge, left edge"
                    elif self.board[1][1] == "x":
                        self.board[0][0] = "o"
                        self.offensive_game = "cpu: top edge, bottom left corner, top left corner; user: bottom edge, center"
                    elif self.board[0][0] == "x":
                        self.board[0][0] = "o"
                        self.offensive_game = "cpu: top edge, bottom left corner, top left corner; user: bottom edge, right edge"
                    elif self.board[2][2] == "x":
                        self.board[0][0] = "o"
                        self.offensive_game = "cpu: top edge, bottom left corner, top left corner; user: bottom edge, bottom right corner"
            self.move_count += 1

        elif self.move_count == 5:
            if self.cpu_brink_of_win():
                pass
            elif self.user_brink_of_win():
                pass
            else:
                flag = True
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j] != "o" and self.board[i][j] != "x":
                            self.board[i][j] = "o"
                            flag = False
                            break
                    if not flag:
                        break
            self.move_count += 1

        elif self.move_count == 6:
            if self.cpu_brink_of_win():
                pass
            elif self.user_brink_of_win():
                pass
            else:
                flag = True
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j] != "o" and self.board[i][j] != "x":
                            self.board[i][j] = "o"
                            flag = False
                            break
                    if not flag:
                        break
            self.move_count += 1

        elif self.move_count == 7:
            if self.cpu_brink_of_win():
                pass
            elif self.user_brink_of_win():
                pass
            else:
                flag = True
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j] != "o" and self.board[i][j] != "x":
                            self.board[i][j] = "o"
                            flag = False
                            break
                    if not flag:
                        break
            self.move_count += 1

        elif self.move_count == 8:
            if self.cpu_brink_of_win():
                pass
            elif self.user_brink_of_win():
                pass
            else:
                flag = True
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j] != "o" and self.board[i][j] != "x":
                            self.board[i][j] = "o"
                            flag = False
                            break
                    if not flag:
                        break
            self.move_count += 1

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == "x" and self.board[i][1] == "x" and self.board[i][2] == "x":
                return True, "user"
            if self.board[i][0] == "o" and self.board[i][1] == "o" and self.board[i][2] == "o":
                return True, "cpu"
        if (self.board[0][0] == "x" and self.board[1][0] == "x" and self.board[2][0] == "x") or (
                self.board[0][1] == "x" and self.board[1][1] == "x" and self.board[2][1] == "x") or (
                self.board[0][2] == "x" and self.board[1][2] == "x" and self.board[2][2] == "x"):
            return True, "user"
        if (self.board[0][0] == "o" and self.board[1][0] == "o" and self.board[2][0] == "o") or (
                self.board[0][1] == "o" and self.board[1][1] == "o" and self.board[2][1] == "o") or (
                self.board[0][2] == "o" and self.board[1][2] == "o" and self.board[2][2] == "o"):
            return True, "cpu"
        if (self.board[0][0] == "x" and self.board[1][1] == "x" and self.board[2][2] == "x") or (
                self.board[0][2] == "x" and self.board[1][1] == "x" and self.board[2][0] == "x"):
            return True, "user"
        if (self.board[0][0] == "o" and self.board[1][1] == "o" and self.board[2][2] == "o") or (
                self.board[0][2] == "o" and self.board[1][1] == "o" and self.board[2][0] == "o"):
            return True, "cpu"
        return False, ""


def play():
    b = Board()
    move_count = 0

    who_goes_first = input("Would you like to go first or second? ")
    while who_goes_first != "first" and who_goes_first != "second":
        print("Please type either first or second")
        who_goes_first = input("Would you like to go first or second? ")
    tie = True
    player_turn = True
    if who_goes_first == "second":
        player_turn = False
    moves_avail = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while move_count < 9:
        if player_turn:
            print(b.to_string())
            move = input("Enter your move: ")
            while int(move) not in moves_avail:
                print("Enter a valid move")
                move = input("Enter your move: ")
            moves_avail.remove(int(move))
            b.enter_move(move, "x")
            move_count += 1
            player_turn = False
        else:
            b.cpu_move()
            move_count += 1
            player_turn = True

        flag, winner = b.check_win()
        if flag:
            print(b.to_string())
            if winner == "user":
                print("Congratulations! You won")
                tie = False
            else:
                print("Yikes! You lost to Ben")
                tie = False
            break
    if tie:
        print("It's a tie!")


play()
