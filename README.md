# tic-tac-toe
This is a project from JetBrains Academy, which is a tic-tac-toe game for two users

About my program:

1) Reads a string of 9 symbols from the input and displays them to the user in a 3x3 grid. The grid can contain only X, O and _ symbols.
2) Outputs a line of dashes --------- above and below the grid, adds a pipe | symbol to the beginning and end of each line of the grid, and adds a space between all characters in the grid.
3) Take a string entered by the user and print the game grid as in the previous stage.
4) Analyze the game state and print the result. Possible states:
-"Game not finished" when neither side has three in a row but the grid still has empty cells.
-"Draw" when no side has a three in a row and the grid has no empty cells.
-"X wins" when the grid has three X’s in a row.
-"O wins" when the grid has three O’s in a row.
-"Impossible" when the grid has three X’s in a row as well as three O’s in a row, or there are a lot more X's than O's or vice versa (the difference should be 1 or 0; if the difference is 2 or more, then the game state is impossible).
5) Prompt the user to make a move.
6) The user should input 2 numbers that represent the cell where they want to place their X. (the 9 symbols representing the field will be the first line of input, and the 2 coordinate numbers will be the second line of input)
7) Analyze user input and show messages in the following situations:
-"This cell is occupied! Choose another one!" if the cell is not empty.
-"You should enter numbers!" if the user enters non-numeric symbols in the coordinates input.
-"Coordinates should be from 1 to 3!" if the user enters coordinates outside the game grid.
8) Update the grid to include the user's move and print the updated grid to the console.
9) Creates a game loop where the program asks the user to enter the cell coordinates, analyzes the move for correctness and shows a grid with the changes if everything is okay.
10) Ends the game when someone wins or there is a draw.
