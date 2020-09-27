def sum_of_prime_divisors(N):

    sum_of_prime_divs = [0] * (N + 1)

    for i in range(2, N + 1):

        if (sum_of_prime_divs[i] == 0):

            for j in range(i, N + 1, i):

                sum_of_prime_divs[j] += i

    return sum_of_prime_divs[N]

l = int(input())
r = int(input())

a_list = list()

for j in range(101):
    a_list.append(sum_of_prime_divisors(j))

summation = 0
for k in range(l, r + 1):
    summation += a_list[k]

print(summation)
