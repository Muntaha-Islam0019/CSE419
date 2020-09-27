#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<pair<string, string>> a_vect;

    a_vect.push_back(make_pair("Hello!", "Bonjour!"));
    a_vect.push_back(make_pair("How's life?", "Comment va la vie?"));
    a_vect.push_back(make_pair("Have a nice day!", "Bonne journee!"));
    
    cout << "English - French" << endl << endl;
    for (int i = 0; i < 3; i++)
    {
        cout << a_vect[i].first << " - " << a_vect[i].second << endl;
    }
    

    return 0;
}