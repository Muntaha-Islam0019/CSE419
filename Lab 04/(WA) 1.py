def two_pointer (provided_list, provided_summation):
    
    first_pointer = 0
    second_pointer = len(provided_list) - 2

    count = 0

    while first_pointer < second_pointer:

        if provided_list[first_pointer] + provided_list[second_pointer] < provided_summation:
            count += second_pointer - first_pointer
            first_pointer += 1
        elif provided_list[first_pointer] + provided_list[second_pointer] >= provided_summation:
            second_pointer -= 1
    
    return count


while int(input()) != 0:

    given_list = list(map(int, input().rstrip().split()))
    given_list = sorted(given_list)

    print(two_pointer(given_list, given_list[len(given_list) - 1]))
