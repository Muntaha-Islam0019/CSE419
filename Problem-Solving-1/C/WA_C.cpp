#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int test_cases;
    cin >> test_cases;

    while (test_cases != 0)
    {
        int number;
        cin >> number;
        int sum_of_divisors = 1;

        int i = 2;
        while (i < sqrt(number))
        {
            if (number % i == 0)
            {
                sum_of_divisors += i + (int)(number / i);
            }

            i++;
        }
        
        cout << sum_of_divisors << endl;

        test_cases--;
    }
    

    return 0;
}