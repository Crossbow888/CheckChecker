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

pieces = generateRandomPieceSet()
board = generateboard()
print(placepieces(board, pieces))
