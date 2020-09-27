# This is an exple of using two pointer. Different cases may requir different implementation; but, the approach would be same. Here, list is sorted in ascending order. Target is to find out if there remains any pair of elements which has sum of summation.


def two_pointer (provided_list, provided_summation):
    
    first_pointer = 0
    second_pointer = len(provided_list) - 1

    while first_pointer < second_pointer:

        if provided_list[first_pointer] + provided_list[second_pointer] == provided_summation:
            return True
        elif provided_list[first_pointer] + provided_list[second_pointer] < provided_summation:
            first_pointer += 1
        else:
            second_pointer -= 1
    
    return False

