#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int cases, left_number, right_number, count = 0;

    int an_array[100005];
    string provided_string;

    cin >> provided_string >> cases;

    for (int i = 1; i < provided_string.size(); i++)
    {

        if (provided_string[i] == provided_string[i - 1])
            count++;

        an_array[i] = count;
    }

    while (cases--)
    {
        cin >> left_number >> right_number;
        cout << an_array[right_number - 1] - an_array[left_number - 1] << endl;
    }

    return 0;
}