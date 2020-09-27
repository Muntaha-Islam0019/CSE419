test_cases = int(input())

for _ in range(test_cases):

    number = int(input())
    a = [0 for i in range(10)]

    for i in range(1, number + 1):
        j = i
        while j > 0:
            a[j % 10] += 1
            j //= 10

    for i in range(len(a)):
        if i > 0:
            print(" {}".format(a[i]), end = "")
        else:
            print("{}".format(a[i]), end = "")
    
    print()
