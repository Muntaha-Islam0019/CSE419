number = int(input())

for i in range(number):

    salaries = list(map(int, input().split()))
    salaries.sort()

    print(f"Case {i + 1}: {salaries[1]}")
