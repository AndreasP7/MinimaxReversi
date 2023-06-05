from move import Move
from board import Board
import math

class Player:
    def __init__(self, max_depth, color):
        self.color = color
        self.max_depth = max_depth

        if self.color == "Black":
            self.opp_color = "White"
            self.color_v = 1
        if self.color == "White":
            self.opp_color = "Black"
            self.color_v = -1    
        

        
    def maximize(self, board:Board, depth, alpha, beta):
        #If board is terminal or depth is maximum, return the last move of the same color that led to this board, with the board's value
        if (board.terminal_state() or depth == self.max_depth):
            return Move(board.get_last_move(self.color_v).getRow(), board.get_last_move(self.color_v).getCol(),value = board.evaluate())

        children = board.add_children(1)
        max_move = Move(8,8, value= - math.inf)

        for child in children :
           
            move = self.minimize(child,depth+1,alpha,beta)
            if (move.getValue() >= max_move.getValue()) :
                max_move.setRow(child.get_last_move(self.color_v).getRow())
                max_move.setCol(child.get_last_move(self.color_v).getCol())
                max_move.setValue(move.getValue())
                if max_move.getValue() >= beta: #If max_move is more valuable than beta, cut the rest
                    return max_move 

                alpha = max(max_move.getValue(),alpha)
            
            

        return max_move


    def minimize(self, board:Board, depth, alpha, beta):
        #Same as maximize
        if (board.terminal_state() or depth == self.max_depth):
            
            return Move(board.get_last_move(self.color_v).getRow(), board.get_last_move(self.color_v).getCol(),value = board.evaluate())

        children = board.add_children(-1)
        min_move = Move(8, 8, value= math.inf)

        for child in children :
            
            move = self.maximize(child,depth+1,alpha,beta)
            if (move.getValue() <= min_move.getValue()) :
                min_move.setRow(child.get_last_move(self.color_v).getRow())
                min_move.setCol(child.get_last_move(self.color_v).getCol())
                min_move.setValue(move.getValue())
                if min_move.getValue() <= alpha:
                    return min_move     

                beta = min(min_move.getValue(),beta)    
                 

        return min_move    

            
    def mini_max(self,board:Board, depth = 0 ):
        alpha = -math.inf
        beta = math.inf
        
        
        if self.color == "Black":

            return self.maximize(board, depth,alpha,beta)
        if self.color == "White":
            return self.minimize(board,depth,alpha,beta)


