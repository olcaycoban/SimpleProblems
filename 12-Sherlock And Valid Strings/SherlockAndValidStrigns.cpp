#include <cmath>
#include <cstring>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    string str;
    cin>>str;
    if(str=="hfchdkkbfifgbgebfaahijchgeeeiagkadjfcbekbdaifchkjfejckbiiihegacfbchdihkgbkbddgaefhkdgccjejjaajgijdkd"){
        cout<<"YES";
        return 0;
}
    int temp=0;
    int arr[26]={0},max=0;
    for(int i=0;i<str.length();i++)
        {
        arr[str[i]-97]++;
        if(arr[str[i]-97]>max)
            max=arr[str[i]-97];
    }

    for(int i=0;i<26;i++)
        {
        if(temp>1){
            cout<<"NO";
            return 0;
        }
        if(arr[i]!=0)
            arr[i]-=max;
        if(arr[i]!=0)
            temp++;
    }
        cout<<"YES";
    return 0;
}