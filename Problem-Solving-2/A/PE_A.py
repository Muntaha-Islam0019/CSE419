test_cases = int(input())

for i in range(test_cases):

    number = int(input())
    desired_string = ""
    the_dict = dict()

    for j in range(1, number + 1):
        desired_string += str(j)

    for k in range(10):
        the_dict[str(k)] = 0

    for l in desired_string:
        the_dict[l] += 1

    for m in the_dict.values():
        print(m, end = " ")

    print()
