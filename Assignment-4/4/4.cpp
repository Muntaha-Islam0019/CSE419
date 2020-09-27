#include <iostream>
using namespace std;

void funmath(string n, int c)
{
    for (int i = 0; i < n.size(); i++)
    {
        if (n[i] == 'a' || n[i] == 'e' || n[i] == 'i' || n[i] == 'o' || n[i] == 'u')
        {
            c++;
            cout << n[i];
        }
    }
    if (c == 0)
    {
        cout << "No vowels in the name!";
    }
    else
    {
        cout << c;
    }
}

int main()
{
    string n;
    cin >> n;
    funmath(n, 0);
}
