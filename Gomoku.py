
import random

class Gomoku:
    # ---------------------- INITIALIZATION  ---------------------- #
    # initialize the board
    # current_player is set to 'X' by default
    # Use 2D list to represent the board
    # board_size is the length of the board in one direction, e.g. 3x3 board, 4x4 board, etc.
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 'X'
    
    # ---------------------- DISPLAY BOARD  ---------------------- #
    # display the board
    # Logs: fixed the double digit axis labels alignment issue
    def display_board(self):
        # print column labels
        # column_labels = '   '.join([str(i) for i in range(self.board_size)])

        for i in range(self.board_size):
            if i <= 9:
                column_labels = '   '.join([str(i) for i in range(self.board_size)])
            else:
                column_labels1 = '   '.join([str(i) for i in range(10)]) + '   '
                column_labels2 = '  '.join([str(i) for i in range(10, self.board_size)])
                column_labels = column_labels1 + column_labels2
        print('     ' + column_labels)
        print('   ' + '-' * (len(column_labels)+3))

        # print rows
        for i, row in enumerate(self.board):
            if i <= 9:
                print(f" {i} | " + ' | '.join(row) + ' |')
            else:
                print(f"{i} | " + ' | '.join(row) + ' |')
            print('   ' + '-' * (len(column_labels)+3))

    # ---------------------- GAME LOGIC  ---------------------- #
    # make a move by the current player, pass in the row and column index
    def make_move(self, row, col):
        while True:
            try:
                if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
                    print("Invalid move. Please choose a row and column within the boundaries of the board.")
                elif self.board[row][col] != ' ':
                    print("That space is already occupied. Please choose a different space.")
                else:
                    self.board[row][col] = self.current_player
                    self.current_player = 'X' if self.current_player == 'O' else 'O'
                    break
            except ValueError:
                print("Invalid input. Please enter a valid row and column.")

    # undo a move by the current player, pass in the row and column index
    def undo_move(self, row, col):
        self.board[row][col] = ' '
        self.current_player = 'X' if self.current_player == 'O' else 'O'
        

    # define another version of make_move for input
    def make_move_input(self):
        while True:
            try:
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))
                if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
                    print("Invalid move. Please choose a row and column within the boundaries of the board.")
                elif self.board[row][col] != ' ':
                    print("That space is already occupied. Please choose a different space.")
                else:
                    self.board[row][col] = self.current_player
                    self.current_player = 'X' if self.current_player == 'O' else 'O'
                    break
            except ValueError:
                print("Invalid input. Please enter a valid row and column.")

    # play the game by taking turns, 2 human players on the same computer
    def play_game(self):
        while True:
            self.display_board()
            self.make_move_input()
            game_status = self.check_game_status()
            print(self.board)
            if game_status == 'X' or game_status == 'O':
                self.display_board()
                print(f"Player {game_status} wins!")
                break
            elif game_status == 'draw':
                self.display_board()
                print("The game is a draw.")
                break
    
    # List all possible moves remaining on the board
    def get_valid_moves(self):
        moves = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == ' ':
                    moves.append((i, j))
        return moves

    # get the next move by the current player
    def random_next_move(self):
        while True:
            # choose a random row and column index
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)

            # check if the tile is available
            if self.board[row][col] == ' ':
                return row, col

    # play the game automatically by taking turns, all moves are random
    def auto_play_game(self):
        while True:
            # get the random next move
            row, col = self.random_next_move()
            self.make_move(row, col)
            self.current_player = 'X' if self.current_player == 'O' else 'O'
            game_status = self.check_game_status()
            if game_status == 'X' or game_status == 'O':
                self.display_board()
                print(f"Player {game_status} wins!")
                break
            elif game_status == 'draw':
                self.display_board()
                print("The game is a draw.")
                break


    # ---------------------- WINNING CONDITION  ---------------------- #
    def check_game_status(self):
        # check if the game has been won by the current player
        if self.check_horizontal_win('O') or self.check_vertical_win('O') or self.check_major_diagonal_win('O') or self.check_minor_diagonal_win('O'):
            return 'O'
        elif self.check_horizontal_win('X') or self.check_vertical_win('X') or self.check_major_diagonal_win('X') or self.check_minor_diagonal_win('X'):
            return 'X'

        # check if the game has ended in a draw
        if self.is_board_full():
            return "Draw"

        # if the game is still ongoing
        return "Ongoing"


    def check_minor_diagonal_win(self, player):
        # check all possible diagonals starting from the top-right corner and going to the bottom-left corner
        for i in range(self.board_size - 4):
            for j in range(4, self.board_size):
                if all([self.board[i+k][j-k] == player for k in range(5)]):
                    return True
        return False

    def check_major_diagonal_win(self, player):
        # check all possible diagonals starting from the top-left corner and going to the bottom-right corner
        for i in range(self.board_size - 4):
            for j in range(self.board_size - 4):
                if all([self.board[i+k][j+k] == player for k in range(5)]):
                    return True
        return False

    def check_vertical_win(self, player):
        # check all possible vertical lines
        for i in range(self.board_size - 4):
            for j in range(self.board_size):
                if all([self.board[i+k][j] == player for k in range(5)]):
                    return True
        return False

    def check_horizontal_win(self, player):
        # check all possible horizontal lines
        for i in range(self.board_size):
            for j in range(self.board_size - 4):
                if all([self.board[i][j+k] == player for k in range(5)]):
                    return True
        return False
    
    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True


    # ---------------------- MINIMAX ALGORITHM  ---------------------- #
    def evaluate_board(self):
        # check if the game has been won by the current player
        if self.check_horizontal_win('O') or self.check_vertical_win('O') or self.check_major_diagonal_win('O') or self.check_minor_diagonal_win('O'):
            return 1000
        elif self.check_horizontal_win('X') or self.check_vertical_win('X') or self.check_major_diagonal_win('X') or self.check_minor_diagonal_win('X'):
            return -1000

        # if current player has 4 in a row, set a score of 500
        for i in range(self.board_size - 4):
            for j in range(self.board_size):
                if all([self.board[i+k][j] == 'O' for k in range(5)]):
                    return 500

        # if current player has 4 in a row, set a score of -500
        for i in range(self.board_size - 4):
            for j in range(self.board_size):
                if all([self.board[i+k][j] == 'X' for k in range(5)]):
                    return -500

        # if current player has 3 in a row, set a score of 100
        for i in range(self.board_size - 3):
            for j in range(self.board_size):
                if all([self.board[i+k][j] == 'O' for k in range(4)]):
                    return 100

        # if current player has 3 in a row, set a score of -100
        for i in range(self.board_size - 3):
            for j in range(self.board_size):
                if all([self.board[i+k][j] == 'X' for k in range(4)]):
                    return -100

        # if current player has 2 in a row, set a score of 10
        for i in range(self.board_size - 2):
            for j in range(self.board_size):
                if all([self.board[i+k][j] == 'O' for k in range(3)]):
                    return 10

        # if current player has 2 in a row, set a score of -10
        for i in range(self.board_size - 2):
            for j in range(self.board_size):
                if all([self.board[i+k][j] == 'X' for k in range(3)]):
                    return -10


        # check if the game has ended in a draw
        if self.is_board_full():
            return 0

        # if the game is still ongoing
        return 1


    def is_game_over(self):
        return self.check_horizontal_win('O') or self.check_vertical_win('O') or self.check_major_diagonal_win('O') or self.check_minor_diagonal_win('O') or self.check_horizontal_win('X') or self.check_vertical_win('X') or self.check_major_diagonal_win('X') or self.check_minor_diagonal_win('X') or self.is_board_full()
