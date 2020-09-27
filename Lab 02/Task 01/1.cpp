#include <stdio.h>
#include <math.h>

void print_factors(long n);

int main(int argc, char **argv)
{
    long n;
    while (1)
    {
        scanf("%ld", &n);
        if (n == 0)
        {
            break;
        }
        printf("%ld = ", n);
        if (n < 0)
        {
            printf("-1 x ");
            n = -n;
        }
        print_factors(n);
        printf("\n");
    }
    return 0;
}

void print_factors(long n)
{
    int first = 1;
    while (n % 2 == 0)
    {
        if (first)
        {
            printf("2");
            first = 0;
        }
        else
        {
            printf(" x 2");
        }
        n /= 2;
    }
    long i = 3;
    long sqn = (sqrt(n)) + 1;
    while (i <= sqn)
    {
        if ((n % i) == 0)
        {
            if (first)
            {
                printf("%ld", i);
                first = 0;
            }
            else
            {
                printf(" x %ld", i);
            }
            n /= i;
        }
        else
        {
            i += 2;
        }
    }
    if (n > 1)
    {
        if (first)
        {
            printf("%ld", n);
        }
        else
        {
            printf(" x %ld", n);
        }
    }
}