def user_choice():
    choice = ' '
    flag = False
    while not choice.isdigit() or not flag:
        choice = input('Please input a number (0-10): ')
        if choice.isdigit() and int(choice) in range(0, 10):
            flag = True
            return int(choice)
        else:
            print('Enter number between 0 and 10')
            flag = False


def display_board(board):
    print('\n')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_symbol(board, symbol, position):
    if board[position] in ('X', 'O'):
        print('Position already marked')
    board[position] = symbol


def check_marked_position(board, position):
    if board[position] in ('X', 'O'):
        print('Position already marked')
        return False
    return True


def select_player_position(board, player):
    position = 0
    while position not in range(1, 10) or not check_marked_position(board, position):
        position = int(input(player + ' Choose your next position: (1-9) '))
    return position


def is_winner(board, symbol):
    return ((board[1] == symbol and board[2] == symbol and board[3] == symbol) or
            (board[4] == symbol and board[5] == symbol and board[6] == symbol) or
            (board[7] == symbol and board[8] == symbol and board[9] == symbol) or
            (board[1] == symbol and board[4] == symbol and board[7] == symbol) or
            (board[2] == symbol and board[5] == symbol and board[8] == symbol) or
            (board[3] == symbol and board[6] == symbol and board[9] == symbol) or
            (board[1] == symbol and board[5] == symbol and board[9] == symbol) or
            (board[3] == symbol and board[5] == symbol and board[7] == symbol))


def is_board_full(board):
    full_flag = True
    for i in range(1, 10):
        if board[i] not in ('X', 'O'):
            full_flag = False
    return full_flag


def start_play():
    while True:
        player1_symbol, player2_symbol = player_input()
        tictac_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        turn = 'Player1'
        play_again_flag = 'Y'
        symbol = ''
        display_board(tictac_board)
        while True:
            if turn == 'Player1':
                symbol = player1_symbol
            else:
                symbol = player2_symbol

            position = select_player_position(tictac_board, turn)
            place_symbol(tictac_board, symbol, position)
            display_board(tictac_board)
            if is_winner(tictac_board, symbol):
                print('Yeey! ' + turn + ' won!')
                break
            if is_board_full(tictac_board):
                print('It''s a draw!')
                break
            else:
                turn = 'Player2' if turn is 'Player1' else 'Player1'


        play_again_flag = input('Do you want to play again? Enter Y or N: ')
        print(play_again_flag.lower())
        if play_again_flag.lower() != 'y':
            break

start_play()
