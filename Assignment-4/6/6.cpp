#include <bits/stdc++.h>
using namespace std;

double funmath(double numerator, double denominator)
{
    if (denominator == 0)
    {
        return 0;
    }
    else
    {
        double w = (numerator / denominator);
        int x = int(w);
        double ans = w - x;
        return ans;
    }
}

int main()
{
    double n, m;
    cin >> n;
    cin >> m;
    cout << funmath(n, m);
}
