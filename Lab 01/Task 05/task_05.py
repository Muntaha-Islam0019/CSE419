# initiating with -1 as it is told and 1001 inputs as S <= 1000
sum_of_factors = [-1] * 1001

for i in range(1, 1001):
    
    # summing the factors of each number
    sum_of_factor = sum(j for j in range(1, i+1) if i % j == 0)

    if sum_of_factor <= 1000:

        # here i is resembling S
        sum_of_factors[sum_of_factor] = i

cases = 0

while 1:

    S = int(input())

    if S == 0:
        break

    cases += 1

    print("Case {}: {}".format(cases, sum_of_factors[S]))
