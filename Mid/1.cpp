#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    priority_queue <int> q;

    for (int i = 0; i < 10; i++)
    {
        int number;
        cin >> number;
        q.push(number);
    }

    int arr[10];

    int index = 0;
    while (!q.empty())
    {
        int another_number;
        another_number = q.top();
        arr[index] = another_number;
        q.pop();

        index++;
    }

    for (int i = 9; i >= 0; i--)
    {
        cout << arr[i] << " ";
    }
    
    return 0;
}