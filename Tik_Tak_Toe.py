#Tik tack toe
'''
requirement:
N can be any
playesr will be 2

object:
board
player 
playingpiece
enum of symbols( O,X ) 
game
'''
from enum import Enum

class Board:
    def __init__(self,size):
        self.size=size
        self.board=[]
        self.count=0
        self.intialize()

    def intialize(self):
        self.board=[[None]*self.size for _ in range(self.size)]

    def addMark(self,row,column,playingpiece):
        if self.board[row][column]==None:
            self.board[row][column]=playingpiece
            self.count+=1
            return True
        else:
            return False

    def istherespace(self):
        if self.count==self.size*self.size:
            return False
        return True

    def isUsed(self,row,col):
        if self.board[row][col]:
            return True 
        return False

class player:
    def __init__(self,name,playingpiece):
        self.name=name
        self.playingpiece=playingpiece
    def getName(self):
        return self.name 
    def getpiece(self):
        return self.playingpiece 
    def setName(self,name):
        self.name=name
    def setpiece(self,playingpiece):
        self.playingpiece=playingpiece

class Pieces(Enum):
    X = 'X'
    O = 'O'

class playingpiece:
    def __init__(self,symbol):
        self.symbol = symbol
    def getSymbol(self):
        return self.symbol
    def setSymbol(self,symbol):
        self.symbol = symbol

class game:
    def __init__(self,size, name1, name2):
        self.board = Board(size)
        self.player1 = player(name1, playingpiece(Pieces.X))
        self.player2 = player(name2,playingpiece(Pieces.O))
        self.queue=[self.player1,self.player2]
    
    def start(self):
        winner=None 
        while winner==None:
            if not self.board.istherespace():
                break
            playerTurn = self.queue.pop(0)
            print('Players Turn: '+playerTurn.name)
            row = int(input("Enter row "+playerTurn.name))
            col = int(input("Enter row "+playerTurn.name))
            if self.board.isUsed(row,col):
                print('Already used slot')
                self.queue = [playerTurn].append([self.queue])
                continue
            self.board.addMark(row,col,playerTurn.playingpiece)
            if self.checkWinner(playerTurn.playingpiece, row, col):
                winner = playerTurn
            else:
                self.queue.append(playerTurn)
        if winner==None:
            print('Tie')
        else:
            print('*****Winner*****')
            print(winner.name)
        
    def checkWinner(self,playingpiece, row, col):
        checkRow = True
        checkCol = True
        digonal1 = True
        digonal2 = True
        for i in range(self.board.size):
            if self.board.board[row][i]!=playingpiece:
                checkRow = False
            if self.board.board[i][col]!=playingpiece:
                checkCol = False
            if self.board.board[i][i]!=playingpiece:
                digonal1 = False
            if self.board.board[i][self.board.size-1-i]!=playingpiece:
                digonal2 = False 
        return checkRow or checkCol or digonal1 or digonal2

if __name__=='__main__':
    size = int(input("Enter size of board"))
    name1 = input("Enter player 1 name  ")
    name2 = input("Enter player 2 name  ")
    print("GAME STARTED")
    print("-----------------------")
    gameObj = game(size,name1,name2)
    gameObj.start()