#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output # Remember, this only works in jupyter!

def display(board):
    #clear_output()
        
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    


# In[ ]:





# In[ ]:





# In[2]:


def player_input():
    choise1 = ''
    choise2 = ''
       
    while choise1 == '' or len(choise1) > 1:
        choise1 = input("Player1 choose your marker").upper()
        
        
    while choise2 == ''or len(choise2) > 1:
        choise2 = input("Player2 choose your marker").upper()
        
    marker = [choise1, choise2]
    if choise1 != ''and choise1 != '':
        return (marker)


# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:


def place_marker(board, marker, position):
    board[position] = marker


# In[ ]:





# In[ ]:





# In[4]:


def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# In[ ]:





# In[ ]:





# In[20]:


import random

def choose_first():
    luck = ''
    if random.randint(0, 1) == 0:
        luck = ('Player 2','Player 1')
        return luck
    else:
        luck = ('Player 1','Player 2')
        return luck


# In[24]:


choose_first()[0]


# In[7]:


def space_check(board, position):
    
    return board[position] == ' '


# In[ ]:





# In[8]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# In[ ]:





# In[9]:


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


# In[ ]:





# In[10]:


def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# In[ ]:





# In[27]:


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10

    player1_marker, player2_marker = player_input()
    turn = choose_first()[0]
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display(theBoard)
            print('Plsyer1 it`s your turn')
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display(theBoard)
                print('Player 1 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display(theBoard)
            print('Plsyer2 it`s your turn')
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


# In[ ]:





# In[ ]:




