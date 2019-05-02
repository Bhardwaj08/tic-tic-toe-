#!/usr/bin/env python3
import sys 
import os

#credits
def display():
    print("*" * 40)
    print("*                                      *")
    print("*             Tic Tac Toe              *")
    print("*            by Bhardwaj_08            *")
    print("*" * 40)
#player options 
def player_choice():
    p_choice = ' '
    while not (p_choice == 'X' or p_choice == 'O'):
        print("Do you want to be X or O? ")
        p_choice = input().upper()
    if p_choice == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
#check empty spots on the board
def empty_indicies(board):
    p= len(board)
    indicies = []
    for i in range(p):
        if board[i] != "X" and board[i] != "O":
            indicies.append(i)
    return indicies

#print board on terminal
def draw_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("__|___|__")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("__|___|__")
    print(board[6] + " | " + board[7] + " | " + board[8])

#winning condition 
def winning(board, player):
    if (
 (board[0] == player and board[1] == player and board[2] == player) or
 (board[3] == player and board[4] == player and board[5] == player) or
 (board[6] == player and board[7] == player and board[8] == player) or
 (board[0] == player and board[3] == player and board[6] == player) or
 (board[1] == player and board[4] == player and board[7] == player) or
 (board[2] == player and board[5] == player and board[8] == player) or
 (board[0] == player and board[4] == player and board[8] == player) or
 (board[2] == player and board[4] == player and board[6] == player)):
        return True
    else:
        return False

            
#minmax algorithm for ai_mode
def minmax(new_board, player):
    #Recursive function 
    available_spots = empty_indicies(new_board)
    if(winning(new_board, hu_player)):
        return {'score': -10}
    elif(winning(new_board, ai_player)):
        return {'score': 10}
    elif(len(available_spots) == 0):
        return {'score': 0}
    else:
        #an array to collect all the dictionaries
        moves= []
        #loop through all the available empty spots in the board
        for i in range(len(available_spots)):
            #create a dictionary for each empty spot and store the index of that
            #spot
            move = {}
            move['index'] = new_board[available_spots[i]]
            #set the empty spot to the current player
            new_board[available_spots[i]] = player

            #collect the score resulted from calling the minmax function on the
            #opponent of the current player
            if (player == ai_player):
                result = minmax(new_board, hu_player)
                move['score'] = result['score']
            else:
                result = minmax(new_board, ai_player)
                move['score'] = result['score']

            #reset the spot to empty
            new_board[available_spots[i]] = move['index']

            #push the object to the array
            moves.append(move)

    best_move = None
    if(player == ai_player):
        best_score = -10000
        for i in range(len(moves)):
            if(moves[i]['score'] > best_score):
                best_score = moves[i]['score']
                best_move = i
    else:
        best_score = 10000
        for i in range(len(moves)):
            if(moves[i]['score'] < best_score):
                best_score = moves[i]['score']
                best_move = i

    return moves[best_move]

#clear board
def clear_board(board):
    for i in range(len(board)):
        if board[i] in [0,1,2,3,4,5,6,7,8]:
            board[i] = ' '
        else:
            pass

#create a duplicate board
def copy_board(board):
    new_board = []
    for i in range(len(board)):
        new_board.append(board[i])
    return new_board


#game starts here
display()
pc = player_choice()
print("\n")
os.system('clear')
hu_player, ai_player = pc[0], pc[1]

original_board = [0,1,2,3,4,5,6,7,8]

playing = True

while playing:
    j = int(input("Your turn:"))
    ei = empty_indicies(original_board)
    if j in ei:
        original_board[j] = hu_player
        try:
            i = minmax(original_board, ai_player)['index']
            original_board[i] = ai_player
            board = copy_board(original_board)
            clear_board(board)
            print("\n")
            os.system('clear')
            draw_board(board)
            
            if(winning(original_board, ai_player)):
                print("\nYou've lost")
                playing = False
            elif(winning(original_board, hu_player)):
                print("\nYou've won")
                playing = False
        except:
            board = copy_board(original_board)
            clear_board(board)
            print("\n")
            os.system('clear')
            draw_board(board)
            print("\nIt is a tie")
            playing = False

    else:
        print("Invalid option")
        sys.exit(0)

