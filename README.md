
This program draws a grid to the display and runs a game of tic tac toe, with a single player playing against the computer. 

In order to replicate this program, do the following: 
    -Install Visual Studio Code
    -Install Python and Github extensions
    -Sign-in and connect to an existing Github account and repository
    -Write drawboard function that draws a 3x3 grid and assigns a number value to each grid-plot similar to a keyboard numberpad (1-9 starting from bottom left plot, left to right bottom to top)
    -PlayerLetter gets the user input of what mark the user wants to use either X or O
    -For the whoGoesFirst function, the random library must be called in order to determine who goes first randomly
    -playAgain gets user input for starting a new match, if the user declines the program ends. makeMark takes in the selected plot number and draws the mark in that plot based on who's turn it is
    -isWinner checks for all possible winning scenarios, for a 3x3 grid there must be 3 in a row of the same mark, diagonals included
    -getBoardCopy creates a copy of the board as it currently exists in the program, including any marks made. isSquareFree checks that no mark has been made in a designated plot
    -getPlayerMove player must select a number 1-9 that has not already been filled by either player
    -chooseRandomMoveFromList pairs with the getComputerMove function. Random move checks that a space is free and chooses a random free space, following rules set in the computer move function. getComputerMove sets which marker belongs to the computer, and starts by checking if a winning move is available. If not, it checks if the player has a winning move available, and blocks that move. From there, the computer will then favor selecting a random corner, the center plot, or a side plot in that order of priority. 
    -isBoardFull returns true if no empty spaces remain. 

    -At this point, we print a message indicating the start of the program, then initiate a while true loop. The start of the loop erases the board and calls the playerLetter function.
    A random selection is made for who goes first and the game begins.
    -if cases are then made for whether the player has won, lost or there is a draw. At the end of each round the player is asked if they want to play again, and if so the while loop repeats. 




Snapshot proof of code working: https://imgur.com/gallery/vycSdYh

Helping sources: 
https://www.programming-techniques.com/2019/10/tic-tac-toe-game-project-using-python.html
https://w3schools.com/python