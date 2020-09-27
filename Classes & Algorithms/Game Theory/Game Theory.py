# This is an exple of using game theory. Different cases may requir different implementation; but, the approach would be same. Here, some balls are in a box. Players can take 2, 3 or 5 balls at a time. Player who take the last ball wins.

def can_win(number_of_balls):

    # cases where he can never win
    # as, in 0 balls he cant pick one, and in 1 balls he cant pick as he can at least pick 1 ball
    if number_of_balls == 0 or number_of_balls == 1:
        return False

    # cases where his opponent can't win, or in other words, he can
    # as, if the opponent is left with 0 balls, he wins    
    if can_win(number_of_balls - 2) == 0 or can_win(number_of_balls - 3) == 0 or can_win(number_of_balls - 5) == 0:
        return True

    # otherwise
    return False


# CAUTION: it's just the basic game theory. Nim's game is different. In nims game, there are several piles and the players can take as much stones as he wants; at least 1. Here, nim-sum is the cumulative XOR value of the number of coins of each pile. If the initial nim-sum is non-zero, player A wins. Otherwise, B wins.