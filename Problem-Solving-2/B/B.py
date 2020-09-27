for _ in range(int(input())):

    first, second = map(int, input().split())

    answer = 0
    multiplicator = 1

    while first > 0 or second > 0:

        # 12 % 10 = 2 so im working with the number from right
        number_from_first = first % 10
        number_from_second = second % 10

        answer = answer + (multiplicator * ((number_from_first + number_from_second) % 10))

        multiplicator = multiplicator * 10

        # 12 // 10 = 1 so im leaving the last number
        first = first // 10
        second = second // 10

    print(answer)
