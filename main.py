from board import Board
from move import Move
from player import Player
import time

play = True
while play == True: 

    game = Board()

    print("Would you like to play first?(y/n)")
    ans = input()

    print("Enter your preffered mini-max max depth")
    max_depth = int(input())

    while type(max_depth) != int:
        print("Wrong input. Enter your preffered mini-max max depth")
        max_depth = int(input())



    #Black starts always, if the player wants to play first then he gets the black pieces
        
    if (ans =='y' or ans == 'Y') :
        while not game.terminal_state():
            ai_player = Player(max_depth,"White")
            
            
            print ("It's your turn!(Black)")
            

            game.print_board()

            print ("Enter row")
            row = int(input()) - 1
            
            print ("Enter column")
            col = ord(input()) - 65 # Turn letter to number 
            while(not game.is_on_board(row, col) or not game.move_is_valid(Move(row,col),1)):
                print("Coordinates out of bounds or invalid move. Try again")
                
                print ("Enter row")
                row = int(input()) - 1 
            
                print ("Enter column")
                col = ord(input()) - 65 

            next_move = Move(row, col)
            game.make_move(next_move,1)
            game.print_board()

            print ("It's the opponent's turn!(White)")
            time.sleep(3)
            next_move = ai_player.mini_max(game)
        

            game.make_move(next_move,-1)
            game.print_board()

    elif (ans =='n' or ans == 'N') :
        while not game.terminal_state():
            ai_player = Player(max_depth,"Black")
            
            print ("It's the opponent's turn!(Black)")
            next_move = ai_player.mini_max(game)
            game.make_move(next_move,1)
            game.print_board()


            print ("It's your turn!(White)")
            

            game.print_board()

            print ("Enter row")
            row = int(input()) - 1
            
            print ("Enter column")
            col = ord(input()) - 65  
            while(not game.is_on_board(row, col) or not game.move_is_valid(Move(row,col, -1))):
                print("Coordinates out of bounds or invalid move. Try again")
                
                print ("Enter row")
                row = int(input()) - 1 
            
                print ("Enter column")
                col = ord(input()) - 65
            next_move = Move(row, col)
            game.make_move(next_move,-1)
            game.print_board()     

    if game.terminal_state(): # Find winner
        count_white=0
        count_black=0
        for row in game._board:
            for cell in row:
                if cell == -1:
                    count_white +=1
                if cell == 1:
                    count_black +=1


        if count_black > count_white:
            print("------------------")
            print("Black wins")
            print("------------------")
        elif count_black < count_white:
            print("------------------")
            print("White wins")
            print("------------------")
        else:
            print("------------------")
            print("Tie")
            print("------------------")    

        print("Would you like to play again?(y/n)")
        ans2 = input()
        if ans2 == 'n' or ans2 == 'N':
            play = False
            




    













