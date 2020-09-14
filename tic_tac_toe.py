#!/usr/bin/env python
# coding: utf-8

# In[9]:


from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[1] + "|" + board[2] + "|" + board[3])
test_board = ["#", "X", "O", "X", "O", "X", "O", "X", "O", "X"]
display_board(test_board)


# In[5]:


def player_input():
    """
    OUTPUT = (Player1_marker , Player2_marker)
    """
    marker = " "
    while marker != "X" and marker != "O":
        marker  = input("Player1 , choose between X or O: ").upper()
    if marker == "X":
        
        return("X", "O")
    else:
        return ("O", "X")

player_input()
   


# In[6]:


#test 
player_input()


# In[10]:


def place_marker(board, marker, position):
    board[position] = marker
place_marker(test_board, "$", 8)   
display_board(test_board)


# In[15]:


def win_check(board, mark):
    #all rows share the same marker
    return((board[1] == board[2] == board[3] == mark)or
    (board[4] == board[5] == board[6] == mark)or
    (board[7] == board[8] == board[9] == mark)or
    #all coluns share the same marker
    (board[1] == board[4] == board[7] == mark)or
    (board[2] == board[5] == board[8] == mark)or
    (board[3] == board[6] == board[9] == mark)or
    #both diagonals share the same marker
    (board[1] == board[5] == board[9] == mark)or
    (board[3] == board[5] == board[7] == mark))


# In[17]:


display_board(test_board)
win_check(test_board,"X")


# In[25]:


import random
def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return "Player1 will go first"
    else:
        return "Player2 will go first"


# In[19]:


def space_check(board, position):
    return board[position] == " "


# In[20]:


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board,i):
            return False
    return True    


# In[21]:


def player_choice(board):
    position = 0
    
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose a position (1-9):"))
    
    return position


# In[22]:


def replay():
    choice = input("Play Again? Yes or No")
    
    return choice == "Yes"


# In[27]:


#here comes the hardest part
print("Welcome to another episode of Tic Tac Toe with your friend!!")
#while loop
while True:
    #play game
    
    #firstly set everything up
    the_board = [" "]*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn)
    
    play_game = input("are you ready?y or n? ")
    if play_game == "y":
        game_on = True
    else:
        game_on = False
    #game play
    while game_on:
        if turn == "Player 1":
            #display board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player1_marker,position)
        
            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Player 1 wins !!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("its a tie !!")
                    game_on = False
                else:
                    turn = "Player 2"
        else:
            #display board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player2_marker,position)
        
            #check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("Player 2 wins !!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("its a tie !!")
                    game_on = False
                else:
                    turn = "Player 1"

if not replay():
    break
                
                
        


# In[ ]:




