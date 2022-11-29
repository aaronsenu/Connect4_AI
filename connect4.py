from copy import deepcopy
import random
random.seed(108)

def make_board():
    new_game = []
    for x in range(7):
        new_game.append([' '] * 6)
    return new_game


def print_board(board):
    
    print()
    print(' ', end='')
    for x in range(1, len(board) + 1):
        print(' %s  ' % x, end='')
    print()

    print('+---+' + ('---+' * (len(board) - 1)))

    for y in range(len(board[0])):
        print('|   |' + ('   |' * (len(board) - 1)))

        print('|', end='')
        for x in range(len(board)):
            print(' %s |' % board[x][y], end='')
        print()

        print('|   |' + ('   |' * (len(board) - 1)))

        print('+---+' + ('---+' * (len(board) - 1)))

        
def move_is_valid(board, move):
    if move < 1 or move > (len(board)):
        return False
    if board[move-1][0] != ' ':
        return False
    return True


def available_moves(board):
    moves=[]
    for i in range(len(board)):
        if board[i][0]==' ':
            moves.append(i+1)
    return moves


def board_is_full(board):
    if len(available_moves(board))==0:
        return True
    else:
        return False


def select_space(board, column, player):
    if player!="X" and player!="O":
        return False
    elif not move_is_valid(board, column):
        return False
    fall_count=-1
    for i in range(len(board[column-1])):
        if board[column-1][fall_count]==' ':
            board[column-1][fall_count]=player
            return True
        else:
            fall_count-=1
    return False
    

def has_won(board, symbol):
    #horizontal win
    for y in range(len(board[0])): #6: 0,1,2,3,4,5
        for x in range(len(board)-3): #7-3=4: 0,1,2,3
            if board[x][y]==symbol and board[x+1][y]==symbol and board[x+2][y]==symbol and board[x+3][y]==symbol:
                return True

    #vertical win
    for y in range(len(board[0])-3): #6-3=3: 0,1,2
        for x in range(len(board)): #7: 0,1,2,3,4,5,6
            if board[x][y]==symbol and board[x][y+1]==symbol and board[x][y+2]==symbol and board[x][y+3]==symbol:
                return True

    #/ win
    for x in range(len(board)-3):
        for y in range(3,len(board[0])):
            if board[x][y]==symbol and board[x+1][y-1]==symbol and board[x+2][y-2]==symbol and board[x+3][y-3]==symbol:
                return True
      
    #\ win
    for y in range(len(board[0])-3):
        for x in range(len(board)-3):
            if board[x][y]==symbol and board[x+1][y+1]==symbol and board[x+2][y+2]==symbol and board[x+3][y+3]==symbol:
                return True
      
    return False

    '''
    #horizontal win
    for y in range(len(board[0])): #6: 0,1,2,3,4,5
        for x in range(len(board)-3): #7-3=4: 0,1,2,3
            if board[x][y]==symbol and board[x+1][y]==symbol and board[x+2][y]==symbol and board[x+3][y]==symbol:
                return True
            

    #vertical win
    for x in range(len(board)): #6-3=3: 0,1,2
        for y in range(len(board[0])-3): #7: 0,1,2,3,4,5,6
            if board[x][y]==symbol and board[x][y+1]==symbol and board[x][y+2]==symbol and board[x][y+3]==symbol:
                return True

    #/ win 
    for x in range(len(board) -3):
        for y in range(3, len(board[0])):
            if board[x][y] == symbol and board[x+1][y-1] == symbol and board[x+2][y-2] == symbol and board[x+3][y-3]==symbol:
                return True
    
    #\ win
    for x in range(len(board)-3):
        for y in range(len(board[0])-3):
            if board[x][y]==symbol and board[x+1][y+1]==symbol and board[x+2][y+2] == symbol and board[x+3][y+3]==symbol:
                return True
    
    return False
    '''

def game_is_over(board):
    return has_won(board, 'X') or has_won(board, 'O') or len(available_moves(board))==0

def count_streaks(board, symbol):
    count = 0
    for col in range(len(board)):
        for row in range(len(board[0])):
            if board[col][row] != symbol:
                continue
            # right
            if col < len(board) - 3:
                num_in_streak = 0
                for i in range(4):
                    if board[col + i][row] == symbol:
                        num_in_streak += 1
                    elif board[col + i][row] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #left
            if col > 2:
                num_in_streak = 0
                for i in range(4):
                    if board[col - i][row] == symbol:
                        num_in_streak += 1
                    elif board[col - i][row] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #up-right
            if col < len(board) - 3 and row > 2:
                num_in_streak = 0
                for i in range(4):
                    if board[col + i][row - i] == symbol:
                        num_in_streak += 1
                    elif board[col + i][row - i] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #down-right
            if col < len(board) - 3 and row < len(board[0]) - 3:
                num_in_streak = 0
                for i in range(4):
                    if board[col + i][row + i] == symbol:
                        num_in_streak += 1
                    elif board[col + i][row + i] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #down-left
            if col > 2 and row < len(board[0]) - 3:
                num_in_streak = 0
                for i in range(4):
                    if board[col - i][row + i] == symbol:
                        num_in_streak += 1
                    elif board[col - i][row + i] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #up-left
            if col > 2 and row > 2:
                num_in_streak = 0
                for i in range(4):
                    if board[col - i][row - i] == symbol:
                       num_in_streak += 1
                    elif board[col - i][row - i] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #down-left
                
            #down
            num_in_streak = 0
            if row < len(board[0]) - 3:
                for i in range(4):
                    if row + i < len(board[0]):
                        if board[col][row + i] == symbol:
                            num_in_streak += 1
                        else:
                            break
            for i in range(4):
                if row - i > 0:
                    if board[col][row - i] == symbol:
                        num_in_streak += 1
                    elif board[col][row - i] == " ":
                        break
                    else:
                        num_in_streak == 0
            if row < 3:
                if num_in_streak + row < 4:
                    num_in_streak = 0
            count += num_in_streak
    return count


def evaluate_board(board):
    if has_won(board, 'X'):
        return float("Inf")
    elif has_won(board,'O'):
        return -float("Inf")
    else:
        return count_streaks(board, 'X') - count_streaks(board, 'O')

                          
def minimax(board, is_maximizing, depth, alpha, beta):
    
    #Base case
    if game_is_over(board) or depth==0:
        return [evaluate_board(board), ""]
    
    if is_maximizing:
        best_value=-float("Inf")
        symbol='X'
    else:
        best_value=float("Inf")
        symbol='O'
    moves=available_moves(board)
    random.shuffle(moves)
    best_move=moves[0]
    for move in moves:
        #print(move)
        new_board = deepcopy(board)
        select_space(new_board,move, symbol)
        hypothetical_value=minimax(new_board, not is_maximizing, depth-1, alpha, beta)[0]
        '''maximizing: best value = -inf
          minimizing: best value = inf
          Hypothetical value = evaluation funciton from base case
          alpha = -inf
          beta = inf'''
        if is_maximizing and hypothetical_value>best_value:
            best_value=hypothetical_value
            alpha=max(alpha,best_value)
            best_move=move
        elif is_maximizing==False and hypothetical_value<best_value:
            best_value=hypothetical_value
            beta=min(beta, best_value)
            best_move=move
        if alpha>=beta: #prunes 
            break
    return [best_value,best_move]

    """
    if game_is_over(board) or depth==0:
        return [evaluate_board(board), ""]
    if is_maximizing:
        best_value=-float("Inf")
        moves=available_moves(board)
        random.shuffle(moves)
        best_move=moves[0]
        for move in moves: 
            #print(move)
            new_board = deepcopy(board)
            select_space(new_board,move, 'X')
            hypothetical_value=minimax(new_board, not is_maximizing, depth-1, alpha, beta)[0]
            if hypothetical_value>best_value:
                best_value=hypothetical_value
                best_move=move
                alpha=max(alpha,best_value)
            #alpha=max(alpha,best_value)
            if alpha>=beta:
                break
    else:
        best_value=float("Inf")
        moves=available_moves(board)
        random.shuffle(moves)
        best_move=moves[0]
        for move in moves:
            #print(move)
            new_board = deepcopy(board)
            select_space(new_board,move, 'O')
            hypothetical_value=minimax(new_board, not is_maximizing, depth-1, alpha, beta)[0]
            if hypothetical_value<best_value:
                best_value=hypothetical_value
                best_move=move
                beta=min(beta,best_value)
            #beta=min(beta,best_value)
            if alpha>=beta:
                break
    return [best_value, best_move]
"""





def play():
    print()
    print("=============================")
    print("          CONNECT 4          ")
    print("=============================")     
    board=make_board()
    print_board(board)
    while not game_is_over(board):
        
        print("Available moves: ", available_moves(board)) 
        valid_move=False
        while not valid_move:
            move=input("X's move: ")
            try:
                p1_move=int(move)
            except ValueError:
                continue
            if p1_move in available_moves(board):
                valid_move=True
        select_space(board, (p1_move), 'X')
        print_board(board)
       
            
        if not has_won(board, 'X'):
            print("Available moves: ", available_moves(board))
            valid_move=False
            while not valid_move:
                move=input("O's move: ")
                try:
                    p2_move=int(move)
                except ValueError:
                    continue
                if p2_move in available_moves(board):
                    valid_move=True
            select_space(board, (p2_move), 'O')
            print_board(board)
       
    if has_won(board,'X'):
        print("X won!")
    elif has_won(board,'O'):
        print("O won!")
    else:
        print("Its a Tie")




def play_ai(difficulty=0):
    '''difficulty --> int
    choose an integer between 1-7'''
   
    valid=False
    while not valid:
        turn=input("Player 1 or 2: ")
        try:
            player=int(turn)
        except ValueError:
            continue
        if (player==1 or player==2):
            if player==1:
                print("You are player 1 and will be represented with an X")
            else:
                print("You are player 2 and will be represented with an O")
            valid=True
    print()
    
    if not (difficulty>=1 and difficulty<=7):
        valid=False
    while not valid:
        level=input("Choose a level of difficulty from 1-3: ")#1:3 2:4 3:5 
        try:
            difficulty=int(level)            
        except ValueError:
            continue
        if (difficulty>=1 and difficulty<=3):
            print("You chose a difficulty of level {}".format(difficulty))
            difficulty+=2
            valid=True

   
    print()
    print("LETS PLAY!!!")
    print()
    print("=============================")
    print("          CONNECT 4          ")
    print("=============================")
    board=make_board()
    print_board(board)
    while not game_is_over(board):
        
        if player==1:
            print("Available moves: ", available_moves(board)) 
            valid_move=False
            while not valid_move:
                move=input("X's move: ")
                try:
                    p1_move=int(move)
                except ValueError:
                    continue
                if p1_move in available_moves(board):
                    valid_move=True
            select_space(board, (p1_move), 'X')
       
            if not has_won(board, 'X'):
                ai=minimax(board, False, difficulty, -float("Inf"), float("Inf"))
                print("Computer chose: ", ai[1])
                select_space(board, ai[1], 'O')
            print_board(board)


        elif player==2:
            ai=minimax(board, True, difficulty, -float("Inf"), float("Inf"))
            print("Computer chose: ", ai[1])
            select_space(board, ai[1], 'X')
            print_board(board)
            
            if not has_won(board, 'X'):
                print("Available moves: ", available_moves(board)) 
                valid_move=False
                while not valid_move:
                    move=input("O's move: ")
                    try:
                        p2_move=int(move)
                    except ValueError:
                        continue
                    if p2_move in available_moves(board):
                        valid_move=True
                select_space(board, (p2_move), 'O')
       
    if has_won(board,'X'):
        print("X won!")
    elif has_won(board,'O'):
        print("O won!")
    else:
        print("Its a Tie")



 
