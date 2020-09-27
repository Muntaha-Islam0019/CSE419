#include <bits/stdc++.h>
using namespace std;

class TrickyQuestion
{
public:
    string main_string, final_string = "";

    TrickyQuestion(string a_string)
    {
        main_string = a_string;
    }

    void largest_substring_without_wxz()
    {
        size_t pos_w = main_string.find("w");
        while (pos_w != string::npos)
        {
            main_string.replace(pos_w, 1, " ");
            pos_w = main_string.find("w", pos_w + 1);
        }

        size_t pos_x = main_string.find("x");
        while (pos_x != string::npos)
        {
            main_string.replace(pos_x, 1, " ");
            pos_x = main_string.find("x", pos_x + 1);
        }

        size_t pos_z = main_string.find("z");
        while (pos_z != string::npos)
        {
            main_string.replace(pos_z, 1, " ");
            pos_z = main_string.find("z", pos_z + 1);
        }

        vector<string> words;
        istringstream iss(main_string);
        for (string s; iss >> s;)
            words.push_back(s);

        int highest_length = 0;
        int highest_length_index = 0;
        int index = 0;
        vector<string>::iterator ptr;
        for (ptr = words.begin(); ptr < words.end(); ptr++)
        {
            string temp = *ptr;
            int length = temp.length();
            if (highest_length < length)
            {
                highest_length = length;
                highest_length_index = index;
            }

            index++;
        }

        final_string = words[highest_length_index];
        cout << final_string;
    }
};

int main(int argc, char const *argv[])
{
    string the_string = "";
    cin >> the_string;

    TrickyQuestion ques(the_string);
    ques.largest_substring_without_wxz();
    
    return 0;
}
