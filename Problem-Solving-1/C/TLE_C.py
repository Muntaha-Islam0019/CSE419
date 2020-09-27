from math import sqrt

test_cases = int(input())
for i in range(test_cases):

    number = int(input())
    sum_of_divisors = 1

    j = 2
    while j < sqrt(number):
        
        if number % j == 0:
            sum_of_divisors += j + int(number / j)
        
        j += 1
    
    print(sum_of_divisors)
