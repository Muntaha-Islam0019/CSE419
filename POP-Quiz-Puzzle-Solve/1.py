def trailing_zero_count(number):
    
    count = 0
    multiple_of_five = 5
    while int(number / multiple_of_five) >= 1:
        count += int(number / multiple_of_five)
        multiple_of_five *= 5

    return count


user_number = int(input())
print(f"Trailing zeroes in the factorial of {user_number}:", trailing_zero_count(user_number))
