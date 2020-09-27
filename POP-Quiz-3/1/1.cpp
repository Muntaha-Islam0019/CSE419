#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<pair<string, int>> a_vect;

    string an_arr[] = {"C", "SE", "419", "quiz1", "done"};
    int arr_size = sizeof(an_arr) / sizeof(an_arr[0]);

    for (int i = 0; i < arr_size; i++)
    {
        a_vect.push_back(make_pair(an_arr[i], i));
    }
    
    for (int i = 0; i < arr_size; i++)
    {
        cout << a_vect[i].first << " " << a_vect[i].second << endl;
    }
    

    return 0;
}