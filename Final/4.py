from functools import reduce

test_cases = int(input())
while test_cases > 0:

    number_of_boxes = int(input())

    number_of_balls = list(map(int, input().rstrip().split()))

    # nims game
    result = reduce((lambda x, y: x ^ y), number_of_balls)
    print('Second' if result == 0 else 'First')

    test_cases -= 1
