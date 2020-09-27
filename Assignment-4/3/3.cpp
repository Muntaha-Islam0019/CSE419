#include <bits/stdc++.h>
using namespace std;

void funmath()
{

    char s[20];
    cin >> s;
    int flag = 0;
    int length = strlen(s);

    for (int i = 0; i < length; i++)
    {
        if (s[i] != s[length - i - 1])
        {
            flag++;
            break;
        }
    }

    if (flag)
    {
        cout << " is not a palindrome";
    }
    else
    {
        cout << " is a palindrome";
    }
}

int main()
{
    funmath();
}