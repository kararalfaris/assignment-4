class StackofFour:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(5):
            row = []
            for j in range(8):
                row.append('.')
            self.board.append(row)

    def fix_spot(self, col, player):
        i = 4
        while i >= 0:
            if self.board[i][col] == '.':
                self.board[i][col] = player
                break
            i = i - 1
        return (i, col)

    def is_player_win(self, player, coordinates):

        rows = coordinates[0]
        cols = coordinates[1]

        # checking columns
        count = 0
        i = rows
        while i < 5 and count <= 4:
            if self.board[i][cols] != player:
                break
            count = count + 1
            i = i + 1
        if count == 4:
            return True

        # checking rows
        count = 0
        j = cols
        while j < 8 and count <= 4:
            if self.board[rows][j] != player:
                break
            count = count + 1
            j = j + 1
        if count == 4:
            return True

        count = 0
        j = cols
        while j >= 0 and count <= 4:
            if self.board[rows][j] != player:
                break
            count = count + 1
            j = j - 1
        if count == 4:
            return True

        # right diagonal check
        i = rows
        j = cols
        count = 0
        while i < 5 and j < 8:
            if self.board[i][j] != player:
                break
            i = i + 1
            j = j + 1
        i = i - 1
        j = j - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] != player:
                break
            count = count + 1
            i = i - 1
            j = j - 1
        if count == 4:
            return True
        # end check

        # left diagonal check
        i = rows
        j = cols
        count = 0

        while i < 5 and j >= 0:
            if self.board[i][j] != player:
                break
            i = i + 1
            j = j - 1

        i = i - 1
        j = j + 1

        while i >= 0 and j < 8:
            if self.board[i][j] != player:
                break
            i = i - 1
            j = j + 1
            count = count + 1
        if count == 4:
            return True
        # end check

    def is_board_filled(self):
        for row in range(5):
            for col in range(8):
                if self.board[row][col] == '.':
                    return False
        return True

    def swap_player_turn(self, player):
        if player == 'X':
            return 'O'
        else:
            return 'X'

    def show_board(self):
        for colNum in range(8):
            print(colNum, end=" ")
        print()
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()
        for colNum in range(8):
            print(colNum, end=" ")
        print()

    def not_valid(self, col):
        if col > 7 or col < 0:
            print('Column out of Range.')
            return True
        elif self.board[0][col] == 'X' or self.board[0][col] == 'O':
            print('This Column is Already Filled')
            return True
        return False

    def start(self):
        self.create_board()

        player = 'X'
        while True:

            self.show_board()

            print("Player ", player, " trun")
            # taking user input
            col = int(input("Enter a column: "))
            while (self.not_valid(col)):
                col = int(input("Invalid Input.Enter a column Again: "))
            print()

            # fixing the spot
            coordinates = self.fix_spot(col, player)

            # checking whether current player has won or not
            if self.is_player_win(player, coordinates):
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()
        print("Game Finished")


# starting the game
game = StackofFour()
game.start()