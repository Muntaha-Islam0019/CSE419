#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    scanf("%d", &n);
    while (n != 0)
    {
        int arr[n];
        int i, first, end, ans = 0;
        for (i = 0; i < n; i++)
            scanf("%d", &arr[i]);
        sort(arr, arr + n);
        for (i = n - 1; i >= 2; i--)
        {
            first = 0, end = i - 1;
            while (first < end)
            {
                if (arr[first] + arr[end] < arr[i])
                {
                    ans += end - first;
                    first = first + 1;
                }
                else
                    end = end - 1;
            }
        }
        printf("%d\n", ans);
        scanf("%d", &n);
    }
    return 0;
}