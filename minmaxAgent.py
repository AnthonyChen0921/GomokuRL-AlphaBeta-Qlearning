
from Gomoku import Gomoku

class MinmaxAgent:
    def __init__(self, max_depth):
        # max_depth is the maximum depth of the minimax search tree
        self.max_depth = max_depth

    def get_best_move(self, game):
        # The minmax function is a recursive function that searches through the
        # minimax search tree to find the best move.
        def minmax(game, depth, maximizing_player):
            # If we have reached the maximum search depth, or if the game is over,
            # return the score of the current position.
            if depth == 0 or game.is_game_over():
                return game.evaluate_board()

            # If it is the maximizing player's turn, choose the move that leads to
            # the highest score.
            if maximizing_player:
                best_score = float('-inf')
                for move in game.get_valid_moves():
                    # Make the move.
                    game.make_move(*move)
                    # Recursively call minmax on the resulting game state.
                    score = minmax(game, depth - 1, False)
                    # Undo the move.
                    game.undo_move(*move)
                    # Update the best score if necessary.
                    best_score = max(best_score, score)
                return best_score
            
            # If it is the minimizing player's turn, choose the move that leads to
            # the lowest score.
            else:
                worst_score = float('inf')
                for move in game.get_valid_moves():
                    # Make the move.
                    game.make_move(*move)
                    # Recursively call minmax on the resulting game state.
                    score = minmax(game, depth - 1, True)
                    # Undo the move.
                    game.undo_move(*move)
                    # Update the worst score if necessary.
                    worst_score = min(worst_score, score)
                return worst_score

        # The get_next_move function returns the best move for the current player.
        def get_next_move(game):
            best_score = float('-inf')
            best_move = None
            for move in game.get_valid_moves():
                # Make the move.
                game.make_move(*move)
                # Recursively call minmax on the resulting game state.
                score = minmax(game, self.max_depth, False)
                # Undo the move.
                game.undo_move(*move)
                # Update the best score and move if necessary.
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_move

        # Return the best move.
        return get_next_move(game)



class AlphaBetaAgent:
    def __init__(self, max_depth):
        # max_depth is the maximum depth of the minimax search tree
        self.max_depth = max_depth

    def get_best_move(self, game):
        # The alphabeta function is a recursive function that searches through the
        # minimax search tree to find the best move.
        def alphabeta(game, depth, alpha, beta, maximizing_player):
            # If we have reached the maximum search depth, or if the game is over,
            # return the score of the current position.
            if depth == 0 or game.is_game_over():
                return game.evaluate_board()

            # If it is the maximizing player's turn, choose the move that leads to
            # the highest score.
            if maximizing_player:
                best_score = float('-inf')
                for move in game.get_valid_moves():
                    # Make the move.
                    game.make_move(*move)
                    # Recursively call alphabeta on the resulting game state.
                    score = alphabeta(game, depth - 1, alpha, beta, False)
                    # Undo the move.
                    game.undo_move(*move)
                    # Update the best score if necessary.
                    best_score = max(best_score, score)
                    # Update alpha if necessary.
                    alpha = max(alpha, best_score)
                    # If alpha is greater than or equal to beta, we can prune the
                    # rest of the search tree.
                    if alpha >= beta:
                        break
                return best_score
            
            # If it is the minimizing player's turn, choose the move that leads to
            # the lowest score.
            else:
                worst_score = float('inf')
                for move in game.get_valid_moves():
                    # Make the move.
                    game.make_move(*move)
                    # Recursively call alphabeta on the resulting game state.
                    score = alphabeta(game, depth - 1, alpha, beta, True)
                    # Undo the move.
                    game.undo_move(*move)
                    # Update the worst score if necessary.
                    worst_score = min(worst_score, score)
                    # Update beta if necessary.
                    beta = min(beta, worst_score)
                    # If alpha is greater than or equal to beta, we can prune the
                    # rest of the search tree.
                    if alpha >= beta:
                        break
                return worst_score

        # The get_next_move function
        def get_next_move(game):
            best_score = float('-inf')
            best_move = None
            for move in game.get_valid_moves():
                # Make the move.
                game.make_move(*move)
                # Recursively call alphabeta on the resulting game state.
                score = alphabeta(game, self.max_depth, float('-inf'), float('inf'), False)
                # Undo the move.
                game.undo_move(*move)
                # Update the best score and move if necessary.
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_move

        # Return the best move.
        return get_next_move(game)
        

        