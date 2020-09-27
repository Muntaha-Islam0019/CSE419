# saves all primes less than or equal to this number
def sieve(number):

    prime_list = [True for index in range(number + 1)]

    # print('Test 3:', prime_list)

    current_number = 2
    while current_number * 2 <= number:

        if prime_list[current_number] == True:

            for a_number in range(current_number * current_number, number + 1, current_number):
                prime_list[a_number] = False

        current_number += 1
    
    # print('Test 2:', prime_list)

    return prime_list


user_input = int(input())

if user_input > 0:
    prime_list = sieve(user_input)
elif user_input < 0:
    prime_list = sieve(-1 * user_input)

answer = list()

# print('Test 1:', prime_list)

if user_input < 0:
    answer.append(-1)

for an_index in range(1, len(prime_list)):

    while prime_list[an_index] and user_input % an_index == 0:
        answer.append(an_index)
        user_input /= an_index

answer_string = f"{user_input} = "

for a_answer in answer:
    answer_string += f"{str(a_answer)} x "

answer_string = answer_string[:len(answer_string) - 2]
print(answer_string)
