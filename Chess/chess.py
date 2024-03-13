class Board:
    def __init__(self):
        self.board = {}
        self.empty()
    def empty(self):
        for col in 'abcdefgh':
            for row in '12345678':
                self.board[col+row] = ' '
    def set(self, pos, piece):   # pos is a square label (a1, a2, ..., h8)
        if pos in self.board.keys():
            self.board[pos] = piece
    def get_keys(self):
        return  self.board.keys()
    def draw(self):
        print("   a   b   c   d   e   f   g   h")
        print(" +---+---+---+---+---+---+---+---+")
        for row in '87654321':
            row_str = row + "|"
            for col in 'abcdefgh':
                row_str += " " + self.board[col + row] + " |"
            print(row_str + row)
            print(" +---+---+---+---+---+---+---+---+")
        print("   a   b   c   d   e   f   g   h")


class Chess_Piece:
    def __init__(self, board, pos, color='white'):
        self.position = self.get_index(pos)
        self.color = color
        board.set(pos, self.get_name())
    def get_index(self, pos):
        return ('abcdefgh'.index(pos[0]), '12345678'.index(pos[1]))
    def get_name(self):
        pass
    def moves(self, board):
        pass


class King(Chess_Piece):
    def get_name(self):
        return 'K'

    def moves(self, board):
        for row in range(self.position[1] - 1, self.position[1] + 2):
            for col in range(self.position[0] - 1, self.position[0] + 2):
                if 0 <= row < 8 and 0 <= col < 8 and (col, row) != self.position:
                    board.set('abcdefgh'[col] + '12345678'[row], 'x')


class Queen(Chess_Piece):
    def get_name(self):
        return 'Q'
    
    def moves(self, board):
        #set column
        for col in range(0,8):
            if (self.position[0], col) != self.position:
                board.set('abcdefgh'[self.position[0]] + '12345678'[col], 'x')
        
        #set row
        for row in range(0,8):
            if (row, self.position[1]) != self.position:
                board.set('abcdefgh'[row] + '12345678'[self.position[1]], 'x')
        
        #set diagonals
        row = self.position[0] - 1
        col = self.position[1] - 1
        while row < 8 and row >= 0 and col < 8 and col >= 0:
            board.set('abcdefgh'[row] + '12345678'[col], 'x')
            col -= 1
            row -= 1
        row = self.position[0] + 1
        col = self.position[1] + 1
        while row < 8 and row >= 0 and col < 8 and col >= 0:
            board.set('abcdefgh'[row] + '12345678'[col], 'x')
            col += 1
            row += 1
        row = self.position[0] - 1
        col = self.position[1] + 1
        while row < 8 and row >= 0 and col < 8 and col >= 0:
            board.set('abcdefgh'[row] + '12345678'[col], 'x')
            col += 1
            row -= 1
        row = self.position[0] + 1
        col = self.position[1] - 1
        while row < 8 and row >= 0 and col < 8 and col >= 0:
            board.set('abcdefgh'[row] + '12345678'[col], 'x')
            col -= 1
            row += 1

class Bishop(Chess_Piece):
    def get_name(self):
        return 'B'
    
    def moves(self,board):
        row = self.position[0] - 1
        col = self.position[1] - 1
        while row < 8 and row >= 0 and col < 8 and col >= 0:
            board.set('abcdefgh'[row] + '12345678'[col], 'x')
            col -= 1
            row -= 1
        row = self.position[0] + 1
        col = self.position[1] + 1
        while row < 8 and row >= 0 and col < 8 and col >= 0:
            board.set('abcdefgh'[row] + '12345678'[col], 'x')
            col += 1
            row += 1
        row = self.position[0] - 1
        col = self.position[1] + 1
        while row < 8 and row >= 0 and col < 8 and col >= 0:
            board.set('abcdefgh'[row] + '12345678'[col], 'x')
            col += 1
            row -= 1
        row = self.position[0] + 1
        col = self.position[1] - 1
        while row < 8 and row >= 0 and col < 8 and col >= 0:
            board.set('abcdefgh'[row] + '12345678'[col], 'x')
            col -= 1
            row += 1

class Knight(Chess_Piece):
    def get_name(self):
        return 'N'
    
    def moves(self,board):
        col = self.position[1] + 1
        row = self.position[0] + 2
        if row < 8 and row >= 0 and col < 8 and col >= 0:
            board.set('abcdefgh'[row] + '12345678'[col], 'x')
        col = self.position[1] + 2
        row = self.position[0] + 1
        if row < 8 and row >= 0 and col < 8 and col >= 0:
            board.set('abcdefgh'[row] + '12345678'[col], 'x')
        col = self.position[1] - 1
        row = self.position[0] - 2
        if row < 8 and row >= 0 and col < 8 and col >= 0:
            board.set('abcdefgh'[row] + '12345678'[col], 'x')
        col = self.position[1] - 2
        row = self.position[0] - 1
        if row < 8 and row >= 0 and col < 8 and col >= 0:
            board.set('abcdefgh'[row] + '12345678'[col], 'x')
        col = self.position[1] + 1
        row = self.position[0] - 2
        if row < 8 and row >= 0 and col < 8 and col >= 0:
            board.set('abcdefgh'[row] + '12345678'[col], 'x')
        col = self.position[1] + 2
        row = self.position[0] - 1
        if row < 8 and row >= 0 and col < 8 and col >= 0:
            board.set('abcdefgh'[row] + '12345678'[col], 'x')
        col = self.position[1] - 1
        row = self.position[0] + 2
        if row < 8 and row >= 0 and col < 8 and col >= 0:
            board.set('abcdefgh'[row] + '12345678'[col], 'x')
        col = self.position[1] - 2
        row = self.position[0] + 1
        if row < 8 and row >= 0 and col < 8 and col >= 0:
            board.set('abcdefgh'[row] + '12345678'[col], 'x')

class Rook(Chess_Piece):
    def get_name(self):
        return 'R'
    
    def moves(self,board):
        #set column
        for col in range(0,8):
            if (self.position[0], col) != self.position:
                board.set('abcdefgh'[self.position[0]] + '12345678'[col], 'x')
        
        #set row
        for row in range(0,8):
            if (row, self.position[1]) != self.position:
                board.set('abcdefgh'[row] + '12345678'[self.position[1]], 'x')



if __name__ == '__main__':
    print("Welcome to the Chess Game!")
    userBoard = Board()
    userBoard.empty()
    userBoard.draw()

    while True:
        print("Enter a chess piece and its position or type X to exit:")
        userInput = input()
        userInput = userInput.lower()
        userBoard.empty()

        if userInput == 'x' or userInput == "X":
            print("Goodbye!")
            break
        
        validInput0 = 'kqnrb'
        validInput1 = 'abcdefgh'
        validInput2 = '12345678'
        
        if (len(userInput) == 3) and (userInput[0] in validInput0) and (userInput[1] in validInput1) and (userInput[2] in validInput2):
            userPosition = userInput[1:]

            if userInput[0] == 'k':
                king = King(userBoard, userPosition)
                king.moves(userBoard)
            elif userInput[0] == 'q':
                queen = Queen(userBoard, userPosition)
                queen.moves(userBoard)
            elif userInput[0] == 'b':
                bishop = Bishop(userBoard, userPosition)
                bishop.moves(userBoard)
            elif userInput[0] == 'n':
                knight = Knight(userBoard, userPosition)
                knight.moves(userBoard)
            elif userInput[0] == 'r':
                rook = Rook(userBoard, userPosition)
                rook.moves(userBoard)
        
            userBoard.draw()

