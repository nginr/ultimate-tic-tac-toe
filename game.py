# module game.py

class Game:
    def __init__(self):
        self.tgrid: list[list[str]] = [["_" for _ in range(9)] for _ in range(9)]
        self.bgrid: list[str] = ["_" for _ in range(9)]
        self.previous_move = (-1, -1)
        self.current_move = (-1, -1)
        self.move = "_"
        self.occupier = "X"
        self.turn = 1
        self.place_any = True
        self.winner = ""

    def __repr__(self):
        return f"Game(turn={self.turn}, prev_m={self.previous_move}, curr_m={self.current_move}, place_any={self.place_any})"

    def extract_indices(self):
        big_idx, small_idx = -1, -1
        if self.turn == 1 and len(self.move) != 2:
            self.current_move = (-1, -1)
        elif self.turn == 1 and len(self.move) == 2:
            try:
                big_idx = int(self.move[0]) - 1
                small_idx = int(self.move[1]) - 1
                self.current_move = (big_idx, small_idx)
            except ValueError:
                self.current_move = (-1, -1)
        elif self.turn > 1 and len(self.move) == 1:
            try:
                big_idx = self.previous_move[1]
                small_idx = int(self.move[0]) - 1
                self.current_move = (big_idx, small_idx)
            except ValueError:
                self.current_move = (-1, -1)
        else:
            self.current_move = (-1, -1)

    def ioccupier(self):
        if self.turn%2 == 0:
            self.occupier = "O"
        else:
            self.occupier = "X"

    def valid_move(self) -> bool:
        big_idx, small_idx = self.current_move
        if big_idx == -1 or small_idx == -1 or not (0 <= big_idx <= 8) or not (0 <= small_idx <= 8):
            print("  [Move] has to be <1-9>")
            return False
        if self.bgrid[big_idx] != "_":
            self.place_any = True
            print("  [Move] choose any unoccupied square <1-9><1-9>")
            return False
        if self.tgrid[big_idx][small_idx] != "_":
            print("  [Move] choose an unoccupied square")
            return False
        return True

    def update_grid(self):
        self.tgrid[self.current_move[0]][self.current_move[1]] = self.occupier
        self.previous_move = self.current_move
        winner = vertical_win(self.tgrid[self.current_move[0]]) or \
                 horizontal_win(self.tgrid[self.current_move[0]]) or \
                 diagonal_win(self.tgrid[self.current_move[0]])

        if winner != "":
            self.bgrid[self.current_move[0]] = winner

    def ended(self):
        winner = vertical_win(self.bgrid) or \
                 horizontal_win(self.bgrid) or \
                 diagonal_win(self.bgrid)
        if winner != "":
            self.winner = winner
            return True
        return False

    def draw_grid(self):
        print(f"""{self.tgrid[0][0]} {self.tgrid[0][1]} {self.tgrid[0][2]} | {self.tgrid[1][0]} {self.tgrid[1][1]} {self.tgrid[1][2]} | {self.tgrid[2][0]} {self.tgrid[2][1]} {self.tgrid[2][2]} 
{self.tgrid[0][3]} {self.tgrid[0][4]} {self.tgrid[0][5]} | {self.tgrid[1][3]} {self.tgrid[1][4]} {self.tgrid[1][5]} | {self.tgrid[2][3]} {self.tgrid[2][4]} {self.tgrid[2][5]} 
{self.tgrid[0][6]} {self.tgrid[0][7]} {self.tgrid[0][8]} | {self.tgrid[1][6]} {self.tgrid[1][7]} {self.tgrid[1][8]} | {self.tgrid[2][6]} {self.tgrid[2][7]} {self.tgrid[2][8]} 
{'-'*21}
{self.tgrid[3][0]} {self.tgrid[3][1]} {self.tgrid[3][2]} | {self.tgrid[4][0]} {self.tgrid[4][1]} {self.tgrid[4][2]} | {self.tgrid[5][0]} {self.tgrid[5][1]} {self.tgrid[5][2]} 
{self.tgrid[3][3]} {self.tgrid[3][4]} {self.tgrid[3][5]} | {self.tgrid[4][3]} {self.tgrid[4][4]} {self.tgrid[4][5]} | {self.tgrid[5][3]} {self.tgrid[5][4]} {self.tgrid[5][5]} 
{self.tgrid[3][6]} {self.tgrid[3][7]} {self.tgrid[3][8]} | {self.tgrid[4][6]} {self.tgrid[4][7]} {self.tgrid[4][8]} | {self.tgrid[5][6]} {self.tgrid[5][7]} {self.tgrid[5][8]} 
{'-'*21}
{self.tgrid[6][0]} {self.tgrid[6][1]} {self.tgrid[6][2]} | {self.tgrid[7][0]} {self.tgrid[7][1]} {self.tgrid[7][2]} | {self.tgrid[8][0]} {self.tgrid[8][1]} {self.tgrid[8][2]} 
{self.tgrid[6][3]} {self.tgrid[6][4]} {self.tgrid[6][5]} | {self.tgrid[7][3]} {self.tgrid[7][4]} {self.tgrid[7][5]} | {self.tgrid[8][3]} {self.tgrid[8][4]} {self.tgrid[8][5]} 
{self.tgrid[6][6]} {self.tgrid[6][7]} {self.tgrid[6][8]} | {self.tgrid[7][6]} {self.tgrid[7][7]} {self.tgrid[7][8]} | {self.tgrid[8][6]} {self.tgrid[8][7]} {self.tgrid[8][8]}""")

    def get_user_input(self):
        move = ""
        self.ioccupier()
        print(f'[Turn {self.turn}]{tuple(x + 1 for x in self.previous_move)} :: Player {self.occupier}',end=' ')
        if self.turn == 1 or self.place_any == True:
            move = input("Choose 2 digits between 1-9: ")
        else:
            move = input("Choose 1 digit between 1-9: ")
        self.move = move

    def toggle_false_place_any(self):
        if self.place_any == True: 
           self.place_any = False

    def update(self):
        self.draw_grid()
        # print(self.__repr__())
        self.get_user_input()
        self.extract_indices()
        self.ioccupier()

        if not self.valid_move():
            print('[[ [Error] Invalid Move ]]')
            return

        self.update_grid()
        self.toggle_false_place_any()
        self.turn += 1

