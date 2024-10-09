
import pygame, sys
from pygame.locals import *
pygame.init()

font= pygame.font.SysFont("freesanbold.ttf",32)
spot=""
originalspot=""
black="b"
white="w"
width=400
height=400
extraboard=[]


def boardSetup():  #Creates the board that the player wants to play with
    choice = input("What board setup would you like to play with: Original (O), Handicapped (H), Chess960 (C) or Custom (N) ")
    
    if choice.lower() == "o":
        board = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
                 ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                 ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]
        
        board1 = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
                 ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                 ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]
        
        return board,board1
    
    
    
    
    elif choice.lower() == "h": 
        level = input("How strong would you like the handicap to be: Very large (V), Large (L), Moderate (M), or Small (S)?")  #Allows player to choose how hard a handicap they want fro the board they are playing
        while level.lower() != "v" and level.lower() != "l" and level.lower() != "m" and level.lower() != "s":   
            print("Invalid input")
            level = input("How strong would you like the handicap to be: Very large (V), Large (L), Moderate (M), or Small (S)?")
            
        handicapped = input("Would you like white (W) or black (B) to be handicapped?")
        while handicapped.lower() != "b" and handicapped.lower() != "w":
            print("Invalid input")
            handicapped = input("Would you like white (W) or black (B) to be handicapped?")
            
        
        if handicapped.lower() == "w":
            
            if level.lower() == "v":
                board = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
                         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                         ["wr", "", "wb", "", "wk", "", "wn", "wr"]]
                
                board1 = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
                         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                         ["wr", "", "wb", "", "wk", "", "wn", "wr"]]
                return board,board1
            
            elif level.lower() == "l":
                board = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
                         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                         ["wr", "wn", "wb", "", "wk", "wb", "wn", "wr"]]
                
                board1 = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
                         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                         ["wr", "wn", "wb", "", "wk", "wb", "wn", "wr"]]
                return board,board1
            
            elif level.lower() == "m":
                board = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
                         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                         ["wr", "", "wb", "wq", "wk", "wb", "wn", ""]]
                
                board1 = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
                         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                         ["wr", "", "wb", "wq", "wk", "wb", "wn", ""]]
                return board,board1
            
            elif level.lower() == "s":
                board = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
                         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                         ["wr", "wn", "wb", "wq", "wk", "wb", "", "wr"]]
                
                board1 = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
                         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                         ["wr", "wn", "wb", "wq", "wk", "wb", "", "wr"]]
                
                return board,board1
            
        elif handicapped.lower() == "b":
            
            if level.lower() == "v":
              board = [["br", "", "bb", "", "bk", "", "bn", "br"],
                         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                         ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]
              board1 = [["br", "", "bb", "", "bk", "", "bn", "br"],
                         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                         ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]
              return board,board1
                
            elif level.lower() == "l":
                board = [["br", "bn", "bb", "", "bk", "bb", "bn", "br"],
                         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                         ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]
                board1 = [["br", "bn", "bb", "", "bk", "bb", "bn", "br"],
                         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                         ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]
                return board,board1
                
            elif level.lower() == "m":
                board = [["br", "", "bb", "bq", "bk", "bb", "bn", ""],
                         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                         ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]
                board1 = [["br", "", "bb", "bq", "bk", "bb", "bn", ""],
                         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                         ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]
                return board,board1
                
            elif level.lower() == "s":
                board = [["br", "bn", "bb", "bq", "bk", "bb", "", "br"],
                         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                         ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]
                
                board1 = [["br", "bn", "bb", "bq", "bk", "bb", "", "br"],
                         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""],
                         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                         ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]
                return board,board1



    elif choice.lower() == "c":
        board = [["bn", "br", "bn", "bq", "bk", "br", "bb", "bb"],
                 ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                 ["wn", "wr", "wn", "wq", "wk", "wr", "wb", "wb"]]
       
        board1 = [["bn", "br", "bn", "bq", "bk", "br", "bb", "bb"],
                 ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                 ["wn", "wr", "wn", "wq", "wk", "wr", "wb", "wb"]]
        
        return board,board1



    elif choice.lower() == "n": #Allows player to create their own board (with limits)
        board = [["", "", "", "", "bk", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "wk", "", "", ""]]
        
        board1 = [["", "", "", "", "bk", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", "", ""],
                 ["", "", "", "", "wk", "", "", ""]]
        finished = False
        blackCount = 1
        whiteCount = 1
        
        while finished == False:
            
            print("The board currently is:")  
            for i in board:
                print(i)
            
            cont = input("Would you like to enter another piece, remove a piece or leave it as it is? (Y/R/N)")
            while cont.lower() != "y" and cont.lower() != "n" and cont.lower() != "r": #validates input
                print("Invalid input")
                cont = input("Would you like to enter another piece, remove a piece or leave it as it is? (Y/R/N)")
             
                
            if cont.lower() == "n": #checks if the board is valid
                if blackCount < 2 or whiteCount < 2:
                    print("Each colour must have at least one piece other than the king")
                    
                elif (board[1][4] == "br" or board[1][4] == "bq") and board[6][4] == "":
                    print("The white king is currently in check, you cannot create a board starting with a check")
                    
                elif (board[6][4] == "wr" or board[6][4] == "wq") and board[1][4] == "":
                    print("The black king is currently in check, you cannot create a board starting with a check")
                
                else:
                    finished = True
            
            
            elif cont.lower() == "r":
                removeRow = int(input("What row would you like a piece deleted from?")) #Checks which row the user wants to remove a piece from, validates input
                while removeRow < 1 or removeRow > 8: 
                    print("Value must be between 1 and 8")
                    removeRow = int(input("What row would you like a piece deleted from?"))
                    
                    
                removeColumn = int(input("What column would you like a piece deleted from?")) #Checks which column the user wants to remove a piece from, validates input
                while removeColumn < 1 or removeColumn > 8:
                    print("Value must be between 1 and 8")
                    removeColumn = int(input("What column would you like a piece deleted from?"))
                    
                
                while (removeRow == 1 and removeColumn == 5) or (removeRow == 8 and removeColumn == 5): #Makes sure the piece being removed isn't the king
                    print("You cannot remove the king")
                    removeRow = int(input("What row would you like a piece deleted from?"))
                    removeColumn = int(input("What column would you like a piece deleted from?"))
                    
                board[removeRow-1][removeColumn-1] = ""
                board1[removeRow-1][removeColumn-1] = ""
               
                
            else:
                colour = input("What colour piece would you like to add (B/W)?")  #Allows user to choose the colour of the piece they are adding, validates input
                while colour.lower() != "b" and colour.lower() != "w":
                    print("Invalid input")
                    colour = input("What colour piece would you like to add (B/W)?")
                    
                piece = input("What piece would you like to add? (P = pawn, B = bishop, R = rook, N = knight, Q = queen)") #Allows user to choose the type of piece they are adding, validates input
                while piece.lower() != "p" and piece.lower() != "b" and piece.lower() != "r" and piece.lower() != "n" and piece.lower() != "q":
                    print("Invalid input")
                    piece = input("What piece would you like to add? (P = pawn, B = bishop, R = rook, N = knight, Q = queen)")

                pieceSymbol = colour.lower() + piece.lower()
                
                #Allows user to choose which row and column to place piece in, validating the input
                rowValid = False
                while rowValid == False: 
                    row = int(input("Which row would you like to place this piece in?"))
                    if colour.lower() == "b":
                        if piece.lower() == "p":
                            if row != 2:
                                print("You can only place a black pawn on row 2")
                            else:
                                rowValid = True
                        elif row == 1 or row == 2:
                            rowValid = True
                        else:
                            print("Black pieces can only be placed on rows 1 or 2")
                            
                            
                    elif colour.lower() == "w":
                        if piece.lower() == "p":
                            if row != 7:
                                print("You can only place a white pawn on row 7")
                            else:
                                rowValid = True
                        elif row == 7 or row == 8:
                            rowValid = True
                        else:
                            print("White pieces can only be placed on rows 7 or 8")
                
                
                columnValid = False
                while columnValid == False:
                    column = int(input("Which column would you like to place this piece in?"))
                    if column >= 1 and column <= 8:
                        if (row == 1 or row == 8) and column == 5:
                            print("You cannot replace the king")
                        else:
                            columnValid = True
                
                #Places piece in the place the user wants it on the board    
                if board[row-1][column-1] == "":
                    board[row-1][column-1] = pieceSymbol
                    board1[row-1][column-1] = pieceSymbol
                    if colour.lower() == "b":
                        blackCount += 1
                    elif colour.lower() == "w":
                        whiteCount += 1
            
                
                else:
                    # checks if there is already a piece in the slot and asks the user if they want to replace it
                    if piece.lower() == "p":
                        pieceName = "pawn"
                    elif piece.lower() == "r":
                        pieceName = "rook"
                    elif piece.lower() == "n":
                        pieceName = "Knight"
                    elif piece.lower() == "b":
                        pieceName = "bishop"
                    if piece.lower() == "q":
                        pieceName = "queen"
                        
                    print("This spot is taken by a", pieceName)
                    replace = input("Would you like to replace it? (Y/N)")
                    if replace.lower() == "y":
                        board[row-1][column-1] = pieceSymbol
                        board1[row-1][column-1] = pieceSymbol
        return board,board1


board,extraboard=boardSetup()

screen = pygame.display.set_mode((width, height),0,32)


class piece():
    def __init__(self):
        self.piecetype=""
    def show(self,x,y,colour):
        text = font.render(self.piecetype, True,colour)
        screen.blit(text, (x, y))
     

class pawn(piece): #creates the class pawn 
    def __init__(self):
        self.piecetype="P"
    
    def show(self,x,y,colour): #displays the pawn on the board
        text = font.render("P", True,colour)
        screen.blit(text, (x, y))
    
    def check(self,x, y, col,board1) : #checks if there are any pawns giving the opposition king a check
        self.pcheck = False

        if (col == white):
            if x-1> 0 and x+1<8 and y-1>0:
                if (board1[y - 1][x + 1] == "bp" or board1[y - 1][x - 1] == "bp"):
                    self.pcheck = True
        
    
        elif (col == black):
            if (y+1< 8) and x+1<8 and x-1>0:
                if (board1[y + 1][x + 1] == "wp" or board1[y + 1][x - 1] == "wp"):
                    self.pcheck = True
        
    
        return self.pcheck


class knight(piece): #creates the class knight
    def __init__(self):
        self.piecetype="N"
    
    def show(self,x,y,colour): #displays the knight on the board
        text = font.render("N", True,colour)
        screen.blit(text, (x, y))
    
    def check(self,x, y, col,board1): #checks if there are any opposition knights giving the king a check
        self.ncheck = False

        if (x < 7 and y < 6) and board1[y + 2][x + 1] != "":
            if (board1[y + 2][x + 1][1] == "n" and board1[y + 2][x + 1][0] != col): #   -> v--
                self.ncheck = True                
            
        
        if (x >= 1 and y < 6) and board1[y + 2][x - 1] != "":
            if (board1[y + 2][x - 1][1] == "n" and board1[y + 2][x - 1][0] != col): #     <- v--
                self.ncheck = True
            
        
        if (x < 7 and y >= 2) and board1[y - 2][x + 1] != "":
            if (board1[y - 2][x + 1][1] == "n" and board1[y - 2][x + 1][0] != col): #  ^-- ->
                self.ncheck = True
            
        
        if (x >= 1 and y >= 2) and board1[y - 2][x - 1] != "":
            if (board1[y - 2][x - 1][1] == "n" and board1[y - 2][x - 1][0] != col): #     ^-- <-
                self.ncheck = True
            
        
        if (x < 6 and y < 7) and board1[y + 1][x + 2] != "":
            if (board1[y + 1][x + 2][1] == "n" and board1[y + 1][x + 2][0] != col):  #    v-   -->
                self.ncheck = True
            
        
        if (x < 6 and y >= 1) and board1[y - 1][x + 2] != "":
            if (board1[y - 1][x + 2][1] == "n" and board1[y - 1][x + 2][0] != col): #   ^- -->
                self.ncheck = True
            
        
        if (x >= 2 and y < 7) and board1[y + 1][x - 2] != "":
            if (board1[y + 1][x - 2][1] == "n" and board1[y + 1][x - 2][0] != col): #  v-  <--
                self.ncheck = True
            
        
        if (x >= 2 and y >= 1) and board1[y - 1][x - 2] != "":
            if (board1[y - 1][x - 2][1] == "n" and board1[y - 1][x - 2][0] != col): #   ^-  <--
                self.ncheck = True
            
        return self.ncheck
    

class rook(piece):#creates the class rook
    def __init__(self):
        self.piecetype="R"
        self.rcastle=False
    
    def show(self,x,y,colour): #displays the rook on the board
        text = font.render("R", True,colour)
        screen.blit(text, (x, y))

    
    def noObstruction(self,newXpos,newYpos,oldXpos,oldYpos,board1): #checks if there any obstructions preventing a rook from moving in the direction it is meant to move
        self.pathfree = True
        if (newYpos == oldYpos):
            if (oldXpos - newXpos > 0):
              for i in range(newXpos+1,oldXpos):
                  if (board1[newYpos][i] != ""):
                      self.pathfree = False
                      
                  
              
            elif (newXpos-oldXpos>0):
              for i in range(oldXpos+1,newXpos):
                  if (board1[newYpos][i] != ""):
                      self.pathfree = False
                            
         
      
        elif (newXpos == oldXpos):
            if (oldYpos - newYpos > 0):
              for i in range(newYpos+1,oldYpos):
                  if (board1[i][newXpos] != ""):
                      self.pathfree = False
                      
                  
              
            elif (newYpos-oldYpos>0):
              for i in range(oldYpos+1,newYpos):
                  if (board1[i][newXpos] != ""):
                      self.pathfree = False
                  
              
                          
        else:
          self.pathfree = True
      
        return self.pathfree   

    def castle(self,x,y,col): #castles the rooks 
        if (self.rcastle == True):
            if (x == 6 and col == black):
                board[7][5] = "br"
                board[7][7] = ""
                extraboard[7][5] = "br"
                extraboard[7][7] = ""
            elif (x == 6 and col == white):
                board[0][5] = "wr"
                board[0][7] = ""
                extraboard[0][5] = "wr"
                extraboard[0][7] = ""
            elif (x == 2 and col == black):
                extraboard[7][3] = "br"
                extraboard[7][0] = ""
                board[7][3] = "br"
                board[7][0] = ""
            elif (x == 2 and col == white):
                board[0][3] = "wr"
                board[0][0] = ""
                extraboard[0][3] = "wr"
                extraboard[0][0] = ""
            
        
    
    
    def check(self,x, y, col,board1): # checks if any opposition rooks are giving the king a check
        self.rcheck = False
        if (x < 7):
            for i in range(x,7):
                if board1[y][i] != "":
                    if (self.noObstruction(x, y, i, y,board1) and col != board1[y][i][0] and (board1[y][i][1] == "r" or board1[y][i][1] == "q")):
                        self.rcheck = True
            
        
    
        if (y < 7):
            for i in range(y,7):
                if board1[i][x] != "":
                    if (self.noObstruction(x, y, x, i,board1) and col != board1[i][x][0] and (board1[i][x][1] == "r" or board1[i][x][1] == "q")):
                        self.rcheck = True
            
        
    
        if (x >= 1):
            for i in range(0,x):
                if board1[y][i] != "":
                    if (self.noObstruction(x, y, i, y,board1) and col != board1[y][i][0] and (board1[y][i][1] == "r" or board1[y][i][1] == "q")):
                        self.rcheck = True
           
       
    
        if (y >= 1):
            for i in range(0,y):
                if board1[i][x] != "":
                    if (self.noObstruction(x, y, x, i,board1) and col != board1[i][x][0] and (board1[i][x][1] == "r" or board1[i][x][1] == "q")):
                        self.rcheck = True
           
       
   
        return self.rcheck

    
class bishop(piece):#creates the class bishop
    def __init__(self):
        self.piecetype="B"
    
    def show(self,x,y,colour): #displays the bishop on the board
        text = font.render("B", True,colour)
        screen.blit(text, (x, y))

    
    def noObstruction(self,newXpos,newYpos,oldXpos,oldYpos,board1): #checks if there any obstructions preventing the bishop from moving to a square
        self.pathfree = True
        if(newXpos >oldXpos and newYpos > oldYpos) :
           for i in range(1,newXpos-oldXpos) :
               if (oldYpos + i < 8 and oldXpos + i <8):
                if (board1[oldYpos + i][oldXpos + i] != ""):
                     self.pathfree = False
                  
               
           
       
        elif (oldXpos > newXpos and oldYpos > newYpos):
           for i in range(1,oldXpos-newXpos):
               if (newYpos + i < 8 and newXpos + i <8):
                if (board1[newYpos + i][newXpos + i] != ""):
                    self.pathfree = False
               
           
       
        elif (newXpos>oldXpos and oldYpos>newYpos):
           for i in range(1,newXpos-oldXpos):
               if(oldYpos - i > 0 and oldXpos < 8):
                if (board1[oldYpos - i][oldXpos + i] != ""):
                   self.pathfree = False
                   
               
           
      
       
        elif (oldXpos > newXpos  and newYpos > oldYpos ):
           for i in range(1,oldXpos - newXpos):
               if(newYpos - i > 0 and newXpos + i < 8):
                if (board1[newYpos - i][newXpos + i] != ""):
                   self.pathfree = False
               
           

       
        else:
           self.pathfree = True
       
        return self.pathfree
   
    
    def check(self,y, x, col, board1):#checks if there are any opposition bishops giving the king a check
        self.bcheck = False
        for i in range(0,7):
            if (y-i >= 0 and x-i>= 0) and board1[y - i][x - i] !="":        
                if ((self.noObstruction(x - i, y - i, x, y, board1) and col != board1[y - i][x - i][0]) and (board1[y - i][x - i][1] == "b" or board1[y - i][x - i][1] == "q")): # < ^
                    self.bcheck = True
      
           
            if (x + i <= 7 and y >= i) and board1[y - i][x + i] != "":
               if ((self.noObstruction(x + i, y - i, x, y, board1) and col != board1[y - i][x + i][0]) and (board1[y - i][x + i][1] == "b" or board1[y - i][x + i][1] == "q")):# > ^
                    self.bcheck = True
            
            if (y + i <= 7 and x >= i) and board1[y + i][x - i] != "":  
                 if ((self.noObstruction(x - i, y + i, x, y, board1) and col != board1[y + i][x - i][0]) and (board1[y + i][x - i][1] == "b" or board1[y + i][x - i][1] == "q")):# < v
        
                     self.bcheck = True
            
            if (y + i <= 7 and x + i <= 7) and board1[y + i][x + i]:    
                if ((self.noObstruction(x + i, y + i, x, y, board1) and col != board1[y + i][x + i][0]) and (board1[y + i][x + i][1] == "b" or board1[y + i][x + i][1] == "q")):# > v
                    self.bcheck = True
            
    
        return self.bcheck

    
class king(piece):#creates the class king

    def __init__(self):
        self.piecetype="K"
        self.bkingmove=False
        self.bkrook=False
        self.bqrook=False
        self.wkingmove=False
        self.wkrook=False
        self.wqrook=False

    def show(self,x,y,colour): #displays the king on the board
        text = font.render("K", True,colour)
        screen.blit(text, (x, y))
    
    def castlecheck(self): #checks if the king is still able to castle
        
        if(board[0][0]!=""):
            if (board[0][0][1] != "r"):
                self.bqrook = True 
        else:
            self.bqrook = True
         
        if(board[0][7]!=""):
            if (board[0][7][1] != "r"):
                self.bkrook = True
        else:
            self.bkrook = True

        if(board[0][4]!=""):    
            if (board[0][4][1] != "k"):
                self.bkingmove = True
        else: 
            self.bkingmove= True

        if(board[7][0]!=""):
            if (board[7][0][1] != "r"):
                self.wqrook = True
        else: 
            self.wqrook = True
        
        if(board[7][7]!=""):
            if (board[7][7][1] != "r"):
                self.wkrook = True
        else: 
            self.wqrook = True
        
        if(board[7][4]!=""):
            if (board[7][4][1] != "k"):
                self.wkingmove = True
        else:
            self.wkingmove = True
        



    def kingcastle(self,col,x,y): #castle the king on the king side for current player
        if (col == black):
            if ((self.bkrook == False and self.bkingmove == False) and ((board[0][5] == "" and board[0][6] == "") and (x == 0 and y == 6))):
                return True
                
            
        elif (col == white):
            if ((self.wkrook == False and self.wkingmove == False) and ((board[7][5] == "" and board[7][6] == "") and (x == 7 and y == 6))):
                return True
            
        else:
            return False
        
    
    def queencastle(self,col,x,y): #castles the king on the queen side for current player
        if (col == black):
            if ((self.bqrook == False and self.bkingmove == False) and ((board[0][1] == "" and board[0][2] == "" and board[0][3]) and (x == 0 and y == 2))):
                return True
                
            
        elif (col == white):
            if ((self.wqrook == False and self.wkingmove == False) and ((board[7][1] == "" and board[7][2] == "" and board[7][3]) and (x == 7 and y == 2))):
                return True
            
        else:
            return False
        
 

class queen(piece):#creates the class queen
    def __init__(self):
        self.piecetype="Q"  
    
    def show(self,x,y,colour): #displays the queen on the board
        text = font.render("Q", True,colour)
        screen.blit(text, (x, y))

    
   


def legalmoves(newXpos,newYpos,oldXpos,oldYpos,piece): #checks if the move of a piece if a legal move 
        if (piece == "wp") :
            if (board[newYpos][newXpos] == ""): 
                if ((newXpos == oldXpos and oldYpos - 2 == newYpos and oldYpos == 6 and board[oldYpos-1][oldXpos]=="") or (newXpos == oldXpos and oldYpos - 1 == newYpos)):
                    return True
                
            elif (board[newYpos][newXpos][0] == "b"):
                  if ((newXpos == oldXpos - 1 or newXpos == oldXpos + 1) and (newYpos == oldYpos - 1)) :
                    return True
                  
            else:
              return False
            
        
        elif (piece == "bp"):
            if (board[newYpos][newXpos] == ""):  
                if ((newXpos == oldXpos and oldYpos +2 == newYpos and oldYpos == 1 and board[oldYpos+1][oldXpos]=="") or (newXpos == oldXpos and oldYpos + 1 == newYpos)):
                    return True
                
            elif (board[newYpos][newXpos][0] == "w"):
                if ((newXpos == oldXpos - 1 or newXpos == oldXpos + 1) and (newYpos == oldYpos + 1)):
                    return True
                
            else:
                return False
           
        
        elif (piece[1] == "n"):
            if (board[newYpos][newXpos] != ""):
                if (board[newYpos][newXpos][0] != piece[0]):
                    if (((oldXpos + 2 == newXpos or oldYpos + 2 == newYpos) or (oldXpos - 2 == newXpos or oldYpos - 2 == newYpos)) and ((oldXpos + 1 == newXpos or oldYpos + 1 == newYpos) or (oldXpos - 1 == newXpos or oldYpos - 1 == newYpos))) :
                        return True
            
            elif (((oldXpos + 2 == newXpos or oldYpos + 2 == newYpos) or (oldXpos - 2 == newXpos or oldYpos - 2 == newYpos)) and ((oldXpos + 1 == newXpos or oldYpos + 1 == newYpos) or (oldXpos - 1 == newXpos or oldYpos - 1 == newYpos))) :
                return True
            
            else :
                return False
            
        
        elif (piece[1] == "b"):
            if(board[newYpos][newXpos] != ""):
                if ((board[newYpos][newXpos][0] != piece[0]) and b.noObstruction(newXpos,newYpos,oldXpos,oldYpos,board) == True):
                    if ((oldYpos - newYpos == oldXpos - newXpos) or (oldYpos-newYpos==-(oldXpos-newXpos))):
                        return True
                    
            elif b.noObstruction(newXpos,newYpos,oldXpos,oldYpos,board) == True:
                if ((oldYpos - newYpos == oldXpos - newXpos) or (oldYpos-newYpos==-(oldXpos-newXpos))):
                        return True
                    
                
            else:
                return False
            
        
        elif (piece[1] == "r"):
            if(board[newYpos][newXpos] != ""):
                if ((board[newYpos][newXpos][0] != piece[0]) and r.noObstruction(newXpos, newYpos, oldXpos, oldYpos,board) == True) :
                    if ((newXpos == oldXpos and newYpos != oldYpos) or (newXpos != oldXpos and newYpos == oldYpos)):
                      return True 
            elif r.noObstruction(newXpos, newYpos, oldXpos, oldYpos,board) == True:
                if (newXpos == oldXpos and newYpos != oldYpos) or (newXpos != oldXpos and newYpos == oldYpos):
                    return True    
            else:
                return False
            
        elif (piece[1] == "k"):
            if(board[newYpos][newXpos] != ""):
                if (board[newYpos][newXpos][0] != piece[0]):
                    if ((newXpos - oldXpos <= 1 and newYpos - oldYpos <= 1) and (newXpos - oldXpos >= -1 and newYpos - oldYpos >= -1)) :
                        return True
                    
            elif  ((newXpos - oldXpos <= 1 and newYpos - oldYpos <= 1) and (newXpos - oldXpos >= -1 and newYpos - oldYpos >= -1)) :
               return True
                       
            if (piece == "bk"):
                if ((k.bqrook == False and k.bkingmove == False) and ((board[0][1] == "" and (board[0][2] == "" and board[0][3] == "")) and (newYpos == 0 and newXpos == 2))):
                        r.rcastle = True
                        return True
                   
                elif ((k.bkrook == False and k.bkingmove == False) and ((board[0][5] == "" and board[0][6] == "") and (newYpos == 0 and newXpos == 6))):
                        r.rcastle = True
                        return True
                    
                
            elif (piece == "wk"):
                if ((k.wqrook == False and k.wkingmove == False) and (board[7][1] == "" and ((board[7][2] == "" and board[7][3] == "")) and (newYpos == 7 and newXpos == 2))):
                       r.rcastle = True
                       return True
                    
                elif ((k.wkrook == False and k.wkingmove == False) and ((board[7][5] == "" and board[7][6] == "") and (newYpos == 7 and newXpos == 6))):
                       r.rcastle = True
                       return True
                    
                
            
            else:
                return False
            
        
        elif (piece[1] == "q"):
            if (board[newYpos][newXpos] != ""):
               if (board[newYpos][newXpos][0] != piece[0] and (r.noObstruction(newXpos,newYpos,oldXpos,oldYpos,board) and b.noObstruction(newXpos,newYpos,oldXpos,oldYpos,board))) :
                 if (((newXpos == oldXpos and newYpos != oldYpos) or (newXpos != oldXpos and newYpos == oldYpos)) or ((oldYpos - newYpos == oldXpos - newXpos) or (oldYpos - newYpos == -(oldXpos - newXpos)))):
                    return True
                 
            elif((r.noObstruction(newXpos,newYpos,oldXpos,oldYpos,board) and b.noObstruction(newXpos,newYpos,oldXpos,oldYpos,board))) :  
                if (((newXpos == oldXpos and newYpos != oldYpos) or (newXpos != oldXpos and newYpos == oldYpos)) or ((oldYpos - newYpos == oldXpos - newXpos) or (oldYpos - newYpos == -(oldXpos - newXpos)))):
                    return True
                
            else :
                return False
        
        else : 
            return False
            


p = pawn()
k = king()
q = queen()
n = knight()
b = bishop()
r = rook()


def checker(colour,oldxpos,oldypos,newxpos,newypos,spot1,matechecker): #checks if the current players king is in check
    check = False
    spot2 = extraboard[newypos][newxpos]
    extraboard[newypos][newxpos] = spot1
    extraboard[oldypos][oldxpos] = ""
    
    for j in range(0,8):
        for i in range(0,8):
            if (extraboard[i][j] == colour + "k"):
                if ((b.check(i, j, colour,extraboard) == True or r.check(j, i, colour,extraboard) == True) or (n.check(j, i, colour,extraboard) == True or p.check(j, i, colour,extraboard) == True)): 
                    check = True
                    extraboard[oldypos][oldxpos] = spot1
                    extraboard[newypos][newxpos] = spot2
    
    if matechecker == True:
        extraboard[oldypos][oldxpos] = spot1
        extraboard[newypos][newxpos] = spot2
    
    return check


def checkmate(colour,opcolour,oldxpos,oldypos,newxpos,newypos,spot1,board1): #checks if the current player is in checkmate
   legalmove = False
   stateofgame= ""
   #loops through all the legal moves, checking if there are no legal moves available
   for i in range(0,8):
       for j in range(0,8):
           for n in range(0,8):
               for m in range (0,8):
                     if board1[i][j] != "":
                        if board1[i][j][0] == colour:
                            if legalmoves(m,n,j,i,board1[i][j]) == True and checker(colour,j,i,m,n,board1[i][j],True) == False:
                                legalmove=True
                                                        
                            
                
   
   if legalmove == False and checker(colour,oldxpos,oldypos,newxpos,newypos,spot1,True) == True: #outputs checkmate if the current players king is in checkmate
       stateofgame="checkmate"
       print(stateofgame)
       if opcolour == black:
        print("black wins")
       else:
        print("white wins")
   
   elif legalmove == False and checker(colour,oldxpos,oldypos,newxpos,newypos,spot1,True) == False: #outputs stalemate if the current player has no legal moves but is in checkmate
       stateofgame="stalemate"
       print(stateofgame)
       


def promote(newSpotX,newSpotY,originalspot): #Allows the user to promote a pawn to a different piece of their choosing
    replacement=originalspot
    
    if originalspot[0] == "b":
        if newSpotY==7:
            while (replacement[1] != "q" and replacement[1] != "r") and  (replacement[1] != "b" and  replacement[1] != "n"): #validates input
                replacement = "b"+ input("What would you like to promote to? (q,r,b,n)?")

    elif originalspot[0] == "w":
        if newSpotY==0:
            while (replacement[1] != "q" and replacement[1] != "r") and  (replacement[1] != "b" and  replacement[1] != "n"): #validates input
                replacement= "w"+ input("What would you like to promote to? (q,r,b,n)?")

    board[newSpotY][newSpotX]=replacement



def main(): #main code, creates the board and allows the user to interact with it
    originalspot=None
    running = True
    currentPlayer=white
    oppositionPlayer=black
    w=width/8
    h=height/8   
    screen.fill((255,255,255)) 
    for xspot1 in range(8): #displays background of board
        for yspot1 in range(8):
            x=w*yspot1+w/2
            y=h*xspot1+h/2
            if (xspot1+yspot1)%2 != 0:
                pygame.draw.rect(screen,(124,252,0),(x-w/2,y-h/2,w,h))
    

    while running: 
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:

                if pygame.mouse.get_pressed()[0] == True: #if left mouse button clicked then the piece in the square of the mouse is picked up
                    
                    spotX=pygame.mouse.get_pos()[0]//50
                    spotY=pygame.mouse.get_pos()[1]//50
                    originalspot=board[spotY][spotX]

                if pygame.mouse.get_pressed()[2] == True: #if the right mouse button is clicked then it places the piece in the square of the mouse, provided it is a legal move 
                    
                    newSpotX=pygame.mouse.get_pos()[0]//50
                    newSpotY=pygame.mouse.get_pos()[1]//50
                    if originalspot!="":
                        if (currentPlayer == white and originalspot[0] == white): #checks who is current player
                            if checker(currentPlayer,spotX,spotY,newSpotX,newSpotY,originalspot,False) == False : #checks whether current player is in check
                                if (legalmoves(newSpotX,newSpotY,spotX,spotY,originalspot) == True): #checks if desired move is legal
                                    #performs desired move
                                    board[newSpotY][newSpotX] = originalspot
                                    board[spotY][spotX]= ""
                                    extraboard[newSpotY][newSpotX] = originalspot
                                    extraboard[spotY][spotX] = ""
                                    r.castle(newSpotX,newSpotY, currentPlayer)

                                    if originalspot[1] == "p": #allows the user to promote pawn if needed 
                                        promote(newSpotX,newSpotY,originalspot)

                                    checkmate(oppositionPlayer,currentPlayer,spotX,spotY,newSpotX,newSpotY,originalspot,board) #checks if the next player is in checkmate after this move

                                   
                                    if (newSpotX == spotX and newSpotY == spotY): #switches currentplayer if the move was made/legal 
                                        currentPlayer = white
                                        oppositionPlayer = black
                                    else:
                                        currentPlayer = black
                                        oppositionPlayer = white
                    
                        elif (currentPlayer == black and originalspot[0] == black):  #checks who is current player
                            if checker(currentPlayer,spotX,spotY,newSpotX,newSpotY,originalspot,False) == False: #checks whether current player is in check
                                if (legalmoves(newSpotX,newSpotY,spotX,spotY,originalspot) == True): #checks if desired move is legal
 
                                    #performs desired move
                                    board[newSpotY][newSpotX] = originalspot
                                    board[spotY][spotX]= ""
                                    extraboard[newSpotY][newSpotX] = originalspot
                                    extraboard[spotY][spotX] = ""
                                    r.castle(newSpotX,newSpotY,currentPlayer)
                                    

                                    if originalspot[1] == "p":  #allows the user to promote pawn if needed
                                        promote(newSpotX,newSpotY,originalspot)

                                    checkmate(oppositionPlayer,currentPlayer,spotX,spotY,newSpotX,newSpotY,originalspot,board)  #checks if the next player is in checkmate after this move

                                    if (newSpotX == spotX and newSpotY == spotY):#switches currentplayer if the move was made/legal 
                                        currentPlayer = black
                                        oppositionPlayer = white
                                    else:
                                        currentPlayer = white
                                        oppositionPlayer = black
                        
                                       
                    
                                
            screen.fill((255,255,255)) #displays background of board
            for xspot1 in range(8):
                 for yspot1 in range(8):
                     x=w*yspot1+w/2
                     y=h*xspot1+h/2
                     if (xspot1+yspot1)%2 != 0:
                          pygame.draw.rect(screen,(124,252,0),(x-w/2,y-h/2,w,h))


            for xspot2 in range(0,8): #displays all the pieces on the board 
                for yspot2 in range(0,8):
                    x=w*yspot2+w/2
                    y=h*xspot2+h/2
                    spot=board[yspot2][xspot2]
                    if spot != "":
                        if (spot[0] == "b"):
                            fillcolour=((0,0,0))
                        elif (spot[0]== "w"):
                           fillcolour=((220,220,220))
                        if (spot[1] == "p"):
                            p.show(y,x,fillcolour)
                        elif (spot[1] == "k"):
                            k.show(y,x,fillcolour)
                        elif (spot[1] == "q"):
                            q.show(y,x,fillcolour)
                        elif (spot[1] == "r"):
                            r.show(y,x,fillcolour)
                        elif (spot[1] == "n"):
                            n.show(y,x,fillcolour)
                        elif (spot[1] == "b"):
                            b.show(y,x,fillcolour)  
            
            k.castlecheck() #checks if the each king is still able to castle
            r.rcastle= False
            
            if event.type==pygame.QUIT:
                running = False
                sys.exit()
            pygame.display.update()
           
           

main()    
