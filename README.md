# ultimate-tic-tac-toe
Ultimate Tic Tac Toe :: Tic Tac Toe inside of Tic Tac Toe.

1. X goes first and chooses any square.
2. Whichever square X chooses in the small grid. O has to choose the corresponding square in the big grid and choose a square in that small grid.
3. Now X has to choose the corresponding square in the big grid and choose a square in that small grid.
4. Whoever connects 3 squares (horizontally, vertically, diagonally) in the small grid WINS that corresponding square of the big grid.
5. Whoever WINS a square in the big grid repeats a turn and chooses any square in both grids.
6. Whoever has to choose a square from the small grid of an already WON square in the big grid they choose any square in both grids.
7. Whoever connects 3 squares (horizontally, vertically, diagonally) in the big grid WINS.

```
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
```
