Github Repository: https://github.com/kararalfaris/assignment-4
Dockerhub Repository: https://hub.docker.com/r/kararalfaris/stackof4game

StackofFour Game

Description:
StackofFour is a simple console-based Connect Four game implemented in Python. It allows two players to take turns dropping colored discs from the top into a vertically suspended grid. The first player to connect four of their own discs horizontally, vertically, or diagonally wins the game.

How to Run: 

To play the StackofFour game, follow these steps:

1. Open the `game.py` file in a Python environment.

2. Run the script:
   python game.py

3. The game will prompt players to take turns entering a column number to drop their disc into. The game board will be displayed after each move.

4. The game will continue until one of the players connects four discs or the board is filled, resulting in a draw.

OR

1. Pull docker image from docker hub
2. Run Docker Engine
3. Run the followig command:
    docker run -i -t stackof4game


Rules:

- Players take turns to drop their discs into a column.
- The first player to connect four discs in a row (horizontally, vertically, or diagonally) wins.
- If the board is filled and no player has connected four discs, the game is a draw.

Example Board:

0 1 2 3 4 5 6 7
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
0 1 2 3 4 5 6 7