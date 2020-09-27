#include<bits/stdc++.h>

using namespace std;

int main()
{
    string original_string, a_string;
    int test_cases, number_of_strings;

    scanf("%d", &test_cases);

    while (test_cases--) 
    {
        cin >> original_string;

        scanf("%d", &number_of_strings);

        while (number_of_strings--) 
        {
            string another_string = "";
            cin >> a_string;

            for (int i = 0; i < a_string.size(); i++)
                another_string += original_string[i];

            if (a_string == another_string)
                cout << "y" << endl;
            else
                cout << "n" << endl;
        }
    }

    return 0;
}