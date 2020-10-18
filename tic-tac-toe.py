import random  #allows for random selection/generation

def drawBoard(board): #this function draws the board and assigns a number to each square starting at 1
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter(): #this function allows player to choose their marker, the players marker is returned first, then the computers
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst(): #decides who goes first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain(): #player indicates if they want to play another round
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMark(board, letter, move): #receives parameters board, letter and move to know what letter to draw and what square it goes in
    board[move] = letter

def isWinner(bo, le): 
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across top win
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across middle win
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across bottom win 
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down left win
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down middle win
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down right win
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal win
    (bo[9] == le and bo[5] == le and bo[1] == le))   # diagonal win

def getBoardCopy(board): #duplicate the board
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSquareFree(board, move): #check if square is open
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSquareFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSquareFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X': #this if/else
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    for i in range(1, 10): #this loop checks if a winning move is available
        copy = getBoardCopy(board)
        if isSquareFree(copy, i):
            makeMark(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    for i in range(1, 10): #does the player have a winning move available? if so, block them
        copy = getBoardCopy(board)
        if isSquareFree(copy, i):
            makeMark(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9]) #if a corner is free, take it
    if move != None:
        return move
    if isSquareFree(board, 5): #take the center if open
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8]) #select a side 

def isBoardFull(board):
    for i in range(1, 10):
        if isSquareFree(board, i):
            return False
    return True

print('Welcome to Tic...Tac...TOOOOEEEEEE!!!!')

while True:
    theBoard = [' '] * 10 #erase the board
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player': #cases for the player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMark(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('20% muscle increase! You have won!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie, why did you not win?')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter) #now it's the computer's turn
            makeMark(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer beat you.. You small brainer.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie, why did you not win?')
                    break
                else:
                    turn = 'player'
    
    if not playAgain():
        break
                