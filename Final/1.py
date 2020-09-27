# from math import gcd

def my_gcd(first_number, second_number):

    while(second_number):
       first_number, second_number = second_number, first_number % second_number

    return first_number


numbers = list(map(int, input().rstrip().split()))
answer = my_gcd(numbers[0], numbers[1])

index = 2
while index < len(numbers):
    answer = my_gcd(answer, numbers[index])
    index += 1

print(answer)

# print(my_gcd(0, 1))
# print(gcd(0, 1))

# print(gcd(0, 13))
# print(my_gcd(0, 13))
