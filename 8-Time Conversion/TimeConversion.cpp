#include <bits/stdc++.h>

using namespace std;

string timeConversion(string s) 
{
    string str = "";
    int num = stoi(s.substr(0,2));  
    if(s[8] == 'P' && num != 12)
    {
        num += 12;
    }
    if(s[8] == 'A' && num == 12)
    {
        num = 0;
    } 
    if(num < 10)
    {
        str += '0';
    }
     
    
   
    str += to_string(num);  
    str += s.substr(2,6);  
    return str;
}
int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
