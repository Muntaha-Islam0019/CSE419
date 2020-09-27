#include <bits/stdc++.h>
using namespace std;

int summation(int x, int y)
{
    return x + y;
}

int subtraction(int x, int y)
{
    return x - y;
}

int multiplication(int x, int y)
{
    return x * y;
}

double division(int x, int y)
{
    return x / y;
}

int exclusive_or(int x, int y)
{
    return x ^ y;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int first_number, second_number;
    string operator_name;

    cin >> first_number;
    cin >> operator_name;
    cin >> second_number;

    if (operator_name == "+")
    {
        cout << summation(first_number, second_number) << endl;
    }
    else if (operator_name == "-")
    {
        cout << subtraction(first_number, second_number) << endl;
    }
    else if (operator_name == "*")
    {
        cout << multiplication(first_number, second_number) << endl;
    }
    else if (operator_name == "/")
    {
        cout << division(first_number, second_number) << endl;
    }
    else if (operator_name == "^")
    {
        cout << exclusive_or(first_number, second_number) << endl;
    }
    else
    {
        cout << "Please enter proper values.";
    }
    
    
    return 0;
}