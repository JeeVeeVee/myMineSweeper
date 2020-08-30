class Place:
    def __init__(self, row, column):
        self.row = row
        self.column = column
    
    def get_left(self):
        if self.column - 1 >= 0:
            return Place(self.row, self.column - 1)
        else:
            return None
    
    def get_right(self):
        return Place(self.row, self.column + 1)