
from Gomoku import Gomoku
from minmaxAgent import MinmaxAgent
from minmaxAgent import AlphaBetaAgent

game = Gomoku(10)

agent = AlphaBetaAgent(2)

# play the game with the agent
while True:
    game.display_board()
    if game.current_player == 'X':
        game.make_move_input()
    else:
        move = agent.get_best_move(game)
        game.make_move(move[0], move[1])
    game_status = game.check_game_status()
    if game_status == 'X' or game_status == 'O':
        game.display_board()
        print(f"Player {game_status} wins!")
        break
    elif game_status == 'draw':
        game.display_board()
        print("The game is a draw.")
        break


# Path: Gomoku.py