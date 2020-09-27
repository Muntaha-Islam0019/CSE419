from math import floor, ceil, sqrt

while True:
    start, end = map(int, input().split())
    if not start and not end:
        break

    count = floor(sqrt(end)) - ceil(sqrt(start)) + 1
    print(count)
