#include <bits/stdc++.h>

using namespace std;

int main() {
    int n,s,w = 1,k;
    cin >> n;
    k = n-1;
    for(int i = 0; i < n; i++){
     s = k;
     for(int j = 0; j < s; j++) cout << " ";
     for(int m = 0; m < w; m++) cout << "#";
     cout << endl;
     k--;
     w++;
    }
    return 0;
}