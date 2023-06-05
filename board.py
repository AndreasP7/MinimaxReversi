from move import Move
class Board:
    
    def __init__(self,rows :int = 8,cols :int = 8, copy_board  = None):
        if(copy_board == None):    
            self._rows = rows
            self._cols = cols
            self._board = [[0 for i in range(cols)] for j in range(rows)]
            #Set the 4 center pieces
            self._board [3][3]= 1
            self._board [3][4]= -1
            self._board [4][3]= -1
            self._board [4][4]= 1
            self._moves = [] # Moves that led to this board
            

        else:
            
            #In case we want to copy another board
            self._rows = copy_board._rows
            self._cols = copy_board._cols
            self._board = [[0 for i in range(8)] for j in range(8)]
            for i in range(self._rows):
                for j in range(self._cols):
                    self._board[i][j] = copy_board._board[i][j]
            
            self._moves = (copy_board._moves).copy()

        self._last_move = None
        self._directions = [(0, 1),(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        self._children = []
    

        


    def get_cell(self,row,col):
        
        return self._board[row][col]


    def is_on_board(self,row,col):
        return((row in range(self._rows)) and (col in range(self._cols)) )   

    def cell_is_empty(self, row:int, col:int):
        #Check if cell is empty
        return (self.get_cell(row, col) == 0)

    def opposite_value(self,row, col, value):
        return self._board[row][col] * value == -1
    def same_value(self,row,col, value):
        return self._board[row][col] * value == 1

    def pieces_to_flip(self, move, color):
        _pieces =[]
        
        found = False
        start_row = move.getRow()
        start_col = move.getCol()
        value = color
        
        
        
        self._board[start_row][start_col] = value #Temporarily place piece 

        for rowdir,coldir in self._directions:
            row = start_row + rowdir
            col = start_col + coldir
            
            while (self.is_on_board(row,col) and self.opposite_value(row, col, value)): 
                #While we are moving on board and we keep finding enemy pieces
                row += rowdir
                col += coldir
                found = True
                
                
                
                  
                   
            if ( not self.is_on_board(row,col)):
                continue
            if (self.same_value(row, col, value)):
                row += -rowdir
                col += -coldir
                while ((row != start_row or col != start_col) and found):
                    _pieces.append([row, col])
                    row += -rowdir
                    col += -coldir
                    
                    
        self._board[start_row][start_col] = 0
        return _pieces            




    def print_board(self):
        print("-------------------------------------")

        #Print the info
        title = "OTHELLO"
        print(title.center(25) + "\n")

        print("WHITE -> X\n")
        print("BLACK -> O\n")

        
        #Print the board
        print("  A  B  C  D  E  F  G  H ")
        counter = 1
        for row in self._board:
            row_string = str(counter) + ""
            
            for block in row:
                if block == 0:
                    row_string += " - "
                elif block == -1:
                    row_string += " X "
                elif block == 1:
                    row_string += " O "
            counter += 1        
            print(row_string)

        print("-------------------------------------")       
            


    def move_is_valid(self, move : Move, color):
        
        
        
        #Check if coords out of bounds
        if (not self.is_on_board(move.getRow(), move.getCol())) :
            print("Invalid Move. Those coordinates are out of bounds. Please try again")
            return False
        #Check if the chosen cell is not empty
        if (not self.cell_is_empty(move.getRow(),move.getCol())):
            return False
        #Check if there is a piece to flip
        pieces_to_flip = self.pieces_to_flip(move, color)
        
        if(len(pieces_to_flip) == 0):
            return False
        return True


    def evaluate(self):
        #Based on black
        
        
        valid_moves_b = 0
        valid_moves_w = 0
        pieces_diff = 0
        corners_diff = 0
        

        corner_list = [(0,0),(0,7),(7,0),(7,7)]

        for row in range(self._rows):
            for col in range(self._cols):
                if (self.move_is_valid(Move(row, col),1)):
                    valid_moves_b += 1
                if (self.move_is_valid(Move(row, col),-1)):
                    valid_moves_w -= 1    
                if ( (row,col) in corner_list ):
                    corners_diff += self._board[row][col] #If current tile is a corner
                pieces_diff += self._board[row][col]  #Find the "player's number of pieces vs opponents number of pieces" difference

        value =   pieces_diff + valid_moves_b*10 + valid_moves_w*10 + corners_diff*100 
        if (pieces_diff > 0 ):
           value += self.terminal_state() * 1000  #Win
        if (pieces_diff < 0 ):
           value -= self.terminal_state() * 1000  #Loss
            
        return (value)           




    def add_children(self, color):
        #Get children, based on possible moves
        for row in range(self._rows):
            for col in range(self._cols):
                
                if self.move_is_valid(Move(row, col), color) :
                    
                    
                    child = Board(copy_board=self)
                    
                    child.make_move(Move(row, col),color)
                    
                    self._children.append(child)
        return self._children



    def make_move(self, move:Move, color):
        #Find pieces to  flip
        self.pieces = self.pieces_to_flip(move,color)
        if self.move_is_valid(move, color):
            move.setColor(color)
            self._moves.append(move)
            self._last_move = move
            
            
            self._board[move.getRow()][move.getCol()] = color
            
            for piece_cords in self.pieces:
                
                self._board[piece_cords[0]][piece_cords[1]] *= -1
                
        else:
            
            print("Not valid move")
         



    def terminal_state(self):
        #Check if the current board is a terminal state
        for row in range(self._rows):
            for col in range(self._cols):
                if (self.move_is_valid(Move(row,col),1)):
                    return False
                if (self.move_is_valid(Move(row,col),-1)):
                    return False        
        
        
        return True


    def get_last_move(self, color):
        #Get last move of the same color
        i = -1
        while self._moves[i].getColor() != color:
            i = i-1
        return self._moves[i]    