#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int test_cases;
    cin >> test_cases;

    while (test_cases--) {

        int surface_area;
        cin >> surface_area;

        cout << sqrt(surface_area / 6) << endl;
    }

    return 0;
}