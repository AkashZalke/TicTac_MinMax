board = {1:' ' , 2:' ' , 3:' ',
        4:' ' , 5:' ' , 6:' ',
        7:' ' , 8:' ' , 9:' '
    }

player = '*'
bot  = '0'


def check_posi_valid(board,posi):
    if board[posi] != ' ':
        print("Enter a new Position")
        new_posi = int(input("Enter the new position"))
        return check_posi_valid(board,new_posi)
    return posi

def print_board(board):
    print(board[1] + '|' + board[2]  + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5]  + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8]  + '|' + board[9])

def check_draw(board):
    for i in board.keys():
        if board[i] == ' ':
            return False
    return True

def check_win(board):
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        return True
    if board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        return True
    if board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        return True
    if board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        return True
    if board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        return True
    if board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        return True
    if board[1] == board[5] and board[5] == board[9] and board[1] != ' ':
        return True
    if board[3] == board[5] and board[5] == board[7] and board[3] != ' ':
        return True
    return False

def move_p1(board,posi):
    board[posi] = player
    print_board(board)
    return check_win(board)

def move_p2(board,posi):
    board[posi] = bot
    print_board(board)
    return check_win(board)

def minmax():
    max_score()

    min_score()
def max_score():


def min_score():
def compute(board):
    score = -1000
    for key in board.keys():    
        board[key] = bot    
        score = max(minmax(board),score)


if __name__ == "__main__":
    print_board(board)
    while True:
        posi1 = int(input("Position for p1"))
        posi1 = check_posi_valid(board,posi1)

        if move_p1(board,posi1):
            print("Player1 winned the game")
            break

        if check_draw(board):
            print("GAME IS DRAW")
            break

        posi2 = int(input("Position for p2"))
        posi2 = check_posi_valid(board,posi2)
        if move_p2(board,posi2):
            print("Player2 winned the game")
            break

    print("GAME OVER")
            

    
    