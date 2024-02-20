import random

def generateRandomPieceSet():
    whitepieces = ['R', 'N', 'B', 'Q', 'B', 'N', 'R', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
    blackpieces = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'r', 'n', 'b', 'q', 'b', 'n', 'r']

    wP = ["K"]
    bP = ["k"]

    numBP = random.randint(1, 15)
    numWP = random.randint(1, 15)

    for i in range(numBP):
        bP.append(blackpieces.pop(random.randint(0, len(blackpieces) - 1)))

    for i in range(numWP):
        wP.append(whitepieces.pop(random.randint(0, len(whitepieces) - 1)))

    return wP, bP

def generateboard():

    board = {}
    for i in range(1, 9):
        for j in range(1, 9):
            board[(i, j)] = ''
    return board

def getrandomcoordinates():
    x = random.randint(1, 8)
    y = random.randint(1, 8)
    return x, y

def placepieces(board, pieces):

    for colour in pieces:
       for piece in colour:
            while True:
                x, y = getrandomcoordinates()
                if board[(x, y)] == '':
                    board[(x, y)] = piece
                    break
                else:
                    continue
    return board

def isWhiteKingInCheck(board):
    colour = 'w'
    isWhiteKinginDanger = False
    for i in range(1, 9):
        for j in range(1, 9):
            if board[(i, j)] == 'K':
                WKing = (i, j)
            else: 
                continue

    isKingInCheck = isKingInCheckOnRank(board, WKing, colour) # add recursion later
    isKingInCheck = isKingInCheckOnFile(board, WKing, colour)
    isKingInCheck = isKingInCheckOnDiagonal(board, WKing, colour) # to be implemented

    return isKingInCheck

def isKingInCheckOnRank(board, kingPos, colour):
    inCheck = False
    if colour == 'w':
        #check to left
        while kingPos[0] - 1 > 0:
            kingPos[0] -= 1
            if board[kingPos] == '': 
                continue
            elif board[kingPos] != 'q' or board[kingPos] != 'r':
                return inCheck
            else:
                inCheck = True
                break
        #check to right
        while kingPos[0] + 1 <= 8:
            kingPos[0] += 1
            if board[kingPos] == '': 
                continue
            elif board[kingPos] != 'q' or board[kingPos] != 'r':
                return inCheck
            else:
                inCheck = True
                break
    return inCheck

def isKingInCheckOnFile(board, kingPos, colour): 
    inCheck = False
    if colour == 'w':
        #check below
        while kingPos[1] - 1 > 0:
            kingPos[0] -= 1
            if board[kingPos] == '': 
                continue
            elif board[kingPos] != 'q' or board[kingPos] != 'r':
                return inCheck
            else:
                inCheck = True
                break
        #check above
        while kingPos[0] + 1 <= 8:
            kingPos[0] += 1
            if board[kingPos] == '': 
                continue
            elif board[kingPos] != 'q' or board[kingPos] != 'r':
                return inCheck
            else:
                inCheck = True
                break
    return inCheck

pieces = generateRandomPieceSet()
board = generateboard()
print(placepieces(board, pieces))
