from functools import reduce

games = int(input())

for game in range(games):

    number_of_piles = int(input())

    pile = list(map(int, input().rstrip().split()))

    result = reduce((lambda x, y: x ^ y), pile)
    # result = len(pile) % 2 [wont work on test case 2]

    print('Second' if result == 0 else 'First')
