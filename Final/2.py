def trailing_zero_count(number):
    
    count = 0
    multiple_of_five = 5
    while int(number / multiple_of_five) >= 1:
        count += int(number / multiple_of_five)
        multiple_of_five *= 5

    return count

def reverse_trailing_zero_count(number):
    
    # as python has no limit of maximum value, taking c++'s maximum int value
    lowest = 0
    highest = 2147483647

    results = list()

    # searching first number    
    while lowest < highest:
        mid = int((lowest + highest) / 2)
        count_temp = trailing_zero_count(mid)
        if count_temp < number:
            lowest = mid + 1
        else:
            highest = mid
        
    while trailing_zero_count(lowest) == number:
        results.append(lowest)
        lowest += 1

    return results


print(reverse_trailing_zero_count(int(input())))
