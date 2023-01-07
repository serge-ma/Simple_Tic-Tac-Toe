def print_state():
    print(9 * '-')
    for i in range(0, len(state), 3):
        print(f'| {state[i]} {state[i + 1]} {state[i + 2]} |')
    print(9 * '-')


def check_coordinate(position):
    if position in range(1, 4):
        return True
    else:
        print('Coordinates should be from 1 to 3!')
        return False


def check_occupation(row, column):
    if state[(row - 1) * 3 + column - 1] == ' ':
        return True
    else:
        print('This cell is occupied! Choose another one!')
        return False


def check_finished_status():
    rows = [state[0:3], state[3:6], state[6:9]]
    columns = [state[0::3], state[1::3], state[2::3]]
    diags = [state[0::4], state[2:7:2]]
    lines = rows + columns + diags

    if 'XXX' in lines:
        print('X wins')
        return True
    elif 'OOO' in lines:
        print('O wins')
        return True
    elif state.count(' ') == 0:
        print('Draw')
        return True
    else:
        return False


state = ' ' * 9
print_state()

while True:
    try:
        x, y = map(int, input('> ').split())
    except (ValueError, TypeError):
        print('You should enter numbers!')
    else:
        if check_coordinate(x) and check_coordinate(y):
            if check_occupation(x, y):
                turn = 'X' if state.count('X') == state.count('O') else 'O'
                state = state[:(x - 1) * 3 + y - 1] + turn + state[(x - 1) * 3 + y:]
                print_state()

                if check_finished_status():
                    break
