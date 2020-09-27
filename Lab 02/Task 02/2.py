n, a, b = map(int, input().rstrip().split())

# as you're one among the n
x = n - a - 1

if x > b:
    print(b + 1)
else:
    print(x + 1)
