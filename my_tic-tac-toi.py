def draw_grid(my_grid):
    print('---------')
    print('|', my_grid[0][0], my_grid[0][1], my_grid[0][2], '|', sep=' ')
    print('|', my_grid[1][0], my_grid[1][1], my_grid[1][2], '|', sep=' ')
    print('|', my_grid[2][0], my_grid[2][1], my_grid[2][2], '|', sep=' ')
    print('---------')

def row_strike(matrix_symbols):
    k = ''
    for el in matrix_symbols:
        for s in ['X', 'O']:
            if el == [s] * 3:
                k += s
    return k

def column_strike(matrix_symbols):
    k = ''
    for s in ['X', 'O']:
        for j in range(len(matrix_symbols[0])):
            if [matrix_symbols[1][j], matrix_symbols[2][j], matrix_symbols[0][j]] == [s] * 3:
                k += s
    return k

def diagonal_strike(matrix_symbols):
    k = ''
    for s in ['X', 'O']:
        if [matrix_symbols[0][0], matrix_symbols[1][1], matrix_symbols[2][2]] == [s] * 3 or [matrix_symbols[0][2], matrix_symbols[1][1], matrix_symbols[2][0]] == [s] * 3:
            k += s
    return k

def impossible_case(matrix_symbols):
    if abs(matrix_symbols.count('X') - matrix_symbols.count('O')) >= 2:
        return 'Impossible'
    elif len(row_strike(matrix_symbols)) > 1 or len(column_strike(matrix_symbols)) > 1:
        return 'Impossible' 

def analyze_game(matrix_symbols):
    if impossible_case(matrix_symbols):
        print(impossible_case(matrix_symbols))
    elif diagonal_strike(matrix_symbols):
        print(diagonal_strike(matrix_symbols), 'wins')
    elif row_strike(matrix_symbols):  
        print(row_strike(matrix_symbols), 'wins')
    elif column_strike(matrix_symbols):
        print(column_strike(matrix_symbols), 'wins')
    elif all('_' not in el for el in matrix_symbols):
        print('Draw')
    else:
        print('Game not finished')

def analyze_end(matrix_symbols):
    if any([diagonal_strike(matrix_symbols), row_strike(matrix_symbols), column_strike(matrix_symbols)]):
        return True
    elif all('_' not in el for el in matrix_symbols):
        return True 

def analyze_input(matrix_symbols):
    try:
        row_num, col_num = input('Enter the coordinates: ').split()
        int(row_num), int(col_num)
    except ValueError: 
        print('You should enter numbers!')
        return analyze_input(matrix_symbols)
    if int(row_num) > 3 or int(col_num) > 3:
        print('Coordinates should be from 1 to 3!')
        return analyze_input(matrix_symbols)
    elif matrix_symbols[int(row_num)-1][int(col_num)-1] != '_':
        print('This cell is occupied! Choose another one!')
        return analyze_input(matrix_symbols)
    else:
        return int(row_num), int(col_num)


symbols = ['_'] * 9
matrix_symbols = [symbols[:3], symbols[3:6], symbols[6:9]]
draw_grid(matrix_symbols)
i = 0

while not analyze_end(matrix_symbols):
    if i % 2 == 0: el = 'X'
    else: el = 'O'
    r, c = analyze_input(matrix_symbols)
    matrix_symbols[r-1][c-1] = el
    draw_grid(matrix_symbols)
    i += 1
analyze_game(matrix_symbols)
