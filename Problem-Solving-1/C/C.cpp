#include <cstdio>

using namespace std;

int main()
{
    int test_cases, number, i;
    int summation;

    scanf("%d", &test_cases);

    for (int test_case = 1; test_case <= test_cases; test_case++)
    {
        scanf("%d", &number);

        summation = 0;

        for (i = 1; i * i < number; i++)
            if (number % i == 0)
                summation += i + number / i;

        if (i * i == number)
            summation += i;
        summation -= number;

        printf("%d\n", summation);
    }

    return 0;
}