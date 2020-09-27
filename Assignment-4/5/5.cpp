#include <iostream>
using namespace std;

void funmath(string n, string a)
{
    double price;
    
    if (a == "mohakhali")
    {
        price = 100 + 40 + ((8 * 100) / 100);
    }
    else
    {
        price = 100 + 60 + ((8 * 100) / 100);
    }

    cout << price;
}

int main()
{
    string n;
    string a;
    cin >> n;
    cin >> a;
    funmath(n, a);
}
