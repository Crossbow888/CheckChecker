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
                    if piece == 'P' or piece == 'p':
                        if x == 1 or x == 8:
                            continue
                    board[(x, y)] = piece
                    break
                else:
                    continue
    return board

def isWhiteKingInCheck(board):
    colour = 'w'
    isKingInCheck = False
    for i in range(1, 9):
        for j in range(1, 9):
            if board[(i, j)] == 'K':
                WKing = (i, j)
            else: 
                continue

    isKingInCheck = isKingInCheckOnRank(board, WKing, colour) 
    isKingInCheck = isKingInCheckOnFile(board, WKing, colour)
    isKingInCheck = isKingInCheckOnDiagonal(board, WKing, colour) 
    # isKingInCheck = isKingInCheckFromKnight(board, WKing, colour) 

    return isKingInCheck

def isKingInCheckOnRank(board, kingPos, colour):
    inCheck = False
    kingPos = list(kingPos)
    if colour == 'w':
        #check to left
        while kingPos[0] - 1 > 0:
            kingPos[0] -= 1
            if board[kingPos[0], kingPos[1]] == '': 
                continue
            elif (board[kingPos[0], kingPos[1]] != 'q' or board[kingPos[0], kingPos[1]] != 'r') and board[kingPos[0], kingPos[1]] != '':
                return inCheck == False
            else:
                inCheck = True
                break
        #check to right
        while kingPos[0] + 1 <= 8:
            kingPos[0] += 1
            if board[kingPos[0], kingPos[1]] == '': 
                continue
            elif (board[kingPos[0], kingPos[1]] != 'q' or board[kingPos[0], kingPos[1]] != 'r') and board[kingPos[0], kingPos[1]] != '':
                return inCheck
            else:
                inCheck = True
                break
    return inCheck

def isKingInCheckOnFile(board, kingPos, colour): 
    inCheck = False
    kingPos = list(kingPos)
    if colour == 'w':
        #check below
        while kingPos[1] - 1 > 0 and kingPos[0] - 1 > 0:
            kingPos[0] -= 1
            if board[kingPos[0], kingPos[1]] == '': 
                continue
            elif (board[kingPos[0], kingPos[1]] != 'q' or board[kingPos[0], kingPos[1]] != 'r') and board[kingPos[0], kingPos[1]] != '':
                return inCheck
            else:
                inCheck = True
                break
        #check above
        while kingPos[0] + 1 <= 8:
            kingPos[0] += 1
            if board[kingPos[0], kingPos[1]] == '': 
                continue
            elif (board[kingPos[0], kingPos[1]] != 'q' or board[kingPos[0], kingPos[1]] != 'r') and board[kingPos[0], kingPos[1]] != '':
                return inCheck
            else:
                inCheck = True
                break
    return inCheck

def isKingInCheckOnDiagonal(board, kingPos, colour): 
    inCheck = False
    kingPos = list(kingPos)
    if colour == 'w':
        #check below to the left
        while kingPos[0] - 1 > 0 and kingPos[1] - 1 > 0:
            kingPos[0] -= 1
            kingPos[1] -= 1
            if board[kingPos[0], kingPos[1]] == '': 
                continue
            elif (board[kingPos[0], kingPos[1]] != 'q' or board[kingPos[0], kingPos[1]] != 'b' or board[kingPos[0], kingPos[1]] != 'p') and board[kingPos[0], kingPos[1]] != '':
                return inCheck
            else:
                inCheck = True
                break
        #check below to the right
        while kingPos[0] - 1 > 0 and kingPos[1] + 1 <= 8:
            kingPos[0] -= 1
            kingPos[1] += 1
            if board[kingPos[0], kingPos[1]] == '': 
                continue
            elif (board[kingPos[0], kingPos[1]] != 'q' or board[kingPos[0], kingPos[1]] != 'b' or board[kingPos[0], kingPos[1]] != 'p') and board[kingPos[0], kingPos[1]] != '':
                return inCheck
            else:
                inCheck = True
                break
        #check above to the right
        while kingPos[0] + 1 <= 8 and kingPos[1] + 1 <= 8:
            kingPos[0] += 1
            kingPos[1] += 1
            if board[kingPos[0], kingPos[1]] == '': 
                continue
            elif board[kingPos[0], kingPos[1]] != 'q' or board[kingPos[0], kingPos[1]] != 'b' or board[kingPos[0], kingPos[1]] != 'p' or board[kingPos[0], kingPos[1]] != '':
                return inCheck
            else:
                inCheck = True
                break
        #check above to the left
        while kingPos[0] + 1 <= 8 and kingPos[1] - 1 <= 8:
            kingPos[0] += 1
            kingPos[1] += 1
            if board[kingPos[0], kingPos[1]] == '': 
                continue
            elif board[kingPos[0], kingPos[1]] != 'q' or board[kingPos[0], kingPos[1]] != 'b' or board[kingPos[0], kingPos[1]] != 'p'or board[kingPos[0], kingPos[1]] != '': #FIX because pawns only have one range also fix pawns only attacking in one direction!
                return inCheck
            else:
                inCheck = True
                break

    return inCheck

# def isKingInCheckFromKnight(board, WKing, colour): 

def printBoard(board):
    for i in range(1, 9):
        for j in range(1, 9):
            if not board[(i, j)] == '': 
                print("| " + board[(i, j)], end=" |")
            else:
                print("|  ", end=" |")
        print()

pieces = generateRandomPieceSet()
board = generateboard()
placepieces(board, pieces)

printBoard(board)
# print(placepieces(board, pieces))
print(isWhiteKingInCheck(board))

