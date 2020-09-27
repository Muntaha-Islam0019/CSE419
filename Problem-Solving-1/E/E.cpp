#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long n, a;
    cin >> n;

    if (n % 2 == 0)
        a = n / 2;
    else
        a = ((n + 1) / 2) * (-1);

    cout << a << endl;
    return 0;
}