#include <bits/stdc++.h>
using namespace std;

int T;
int N;

int a_func(int x, int y)
{
    if (y == 1)
        return (x % 10);

    int tmp = a_func(x, y / 2);

    tmp = (tmp * tmp) % 10;

    if (y & 1)
        tmp = (tmp * (x % 10)) % 10;

    return tmp;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> T;
    while (T--)
    {
        cin >> N;
        cout << a_func(N, N) << endl;
    }

    return 0;
}