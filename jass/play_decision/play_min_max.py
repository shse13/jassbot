
"""Principle from Perplexity, test. Information sets to understand first.
def minimax(state, depth, maximizingPlayer):
    if depth == 0 or is_terminal(state):
        return evaluate(state)

    if maximizingPlayer:
        maxEval = float('-inf')
        for child in generate_moves(state):
            eval = minimax(child, depth - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = float('inf')
        for child in generate_moves(state):
            eval = minimax(child, depth - 1, True)
            minEval = min(minEval, eval)
        return minEval
"""