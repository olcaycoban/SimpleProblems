//https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

#include <bits/stdc++.h>

using namespace std;

int makeAnagram(string a, string b) {

    int count1[26] = {0}, count2[26] = {0}; 
  
    for (int i=0; a[i]!='\0'; i++) 
        count1[a[i]]++; 
  
    for (int i=0; b[i]!='\0'; i++) 
        count2[b[i]]++; 
  
    int result = 0; 
    for (int i=0; i<26; i++) 
        result += abs(count1[i] - count2[i]); 
    return result; 
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string a;
    getline(cin, a);

    string b;
    getline(cin, b);

    int res = makeAnagram(a, b);

    fout << res << "\n";

    fout.close();

    return 0;
}