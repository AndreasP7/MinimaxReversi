class Move:

    def __init__(self,row:int, col:int, color:str = None, value = 0 ):
        self._row = row
        self._col = col
        self._color =color
        self.value = value
        return 

    def getRow(self):
        return self._row   
    
    def getCol(self):
        return self._col
    
    def getColor(self):
        if (self._color == "Black"):
            return 1
        elif (self._color == "White"):
            return -1
        else:
            return 0 


    def getValue(self):
        return self.value

    def setRow(self,row):
        self._row = row
    
    def setCol(self,col):
        self._col = col

    def setColor(self,color):
        if color == 1:
            self._color = "Black"
        elif color == -1:
            self._color = "White"

    def setValue(self,value):
        self.value = value


        