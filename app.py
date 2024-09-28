# module app

'''
Ultimate Tic Tac Toe :: Tic Tac Toe inside of Tic Tac Toe.

1. X goes first and chooses any square.
2. Whichever square X chooses in the small grid. O has to choose the corresponding square in the big grid and choose a square in that small grid.
3. Now X has to choose the corresponding square in the big grid and choose a square in that small grid.
4. Whoever connects 3 squares (horizontally, vertically, diagonally) in the small grid WINS that corresponding square of the big grid.
5. Whoever WINS a square in the big grid repeats a turn and chooses any square in both grids.
6. Whoever has to choose a square from the small grid of an already WON square in the big grid they choose any square in both grids.
7. Whoever connects 3 squares (horizontally, vertically, diagonally) in the big grid WINS.

     `draw_grid`
1 2 3 | 1 2 3 | 1 2 3 
4 5 6 | 4 5 6 | 4 5 6
7 8 9 | 7 8 9 | 7 8 9
---------------------
1 2 3 | 1 2 3 | 1 2 3
4 5 6 | 4 5 6 | 4 5 6
7 8 9 | 7 8 9 | 7 8 9
---------------------
1 2 3 | 1 2 3 | 1 2 3
4 5 6 | 4 5 6 | 4 5 6
7 8 9 | 7 8 9 | 7 8 9

'''

from game import Game

def horizontal_win(grid: list[str]) -> str:
    for i in range(0, 9, 3):
        if grid[i] == grid[i + 1] == grid[i + 2] and grid[i] != "_":
            return grid[i]
    return ""

def vertical_win(grid: list[str]) -> str:
    for i in range(3):
        if grid[i] == grid[i + 3] == grid[i + 6] and grid[i] != "_":
            return grid[i]
    return ""

def diagonal_win(grid: list[str]) -> str:
    if (grid[0] == grid[4] == grid[8] and grid[0] != "_"):
        return grid[0]
    if (grid[2] == grid[4] == grid[6] and grid[2] != "_"):
        return grid[2]
    return ""

def main():
    game = Game()
    quit = False
    while(not quit and not game.ended()):
        try:
            game.update()
        except KeyboardInterrupt:
            quit = True

    if quit:
        print('\nQUIT')
    else:
        print(f'\n!!! [[{game.winner} WON the GAME]] !!!')

if __name__ == "__main__":
    main()
