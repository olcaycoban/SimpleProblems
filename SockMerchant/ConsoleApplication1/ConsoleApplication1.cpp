#include "pch.h"
#include<iostream>

#define REP(i,n) for(int i=0;i<(n);++i)

using namespace std;

int socks[101];

int main() {
	int n;
	cin >> n;
	REP(i, n) {
		int x;
		cin >> x;
		socks[x]++;
	}

	int pair = 0;
	REP(i, 107)
		pair += socks[i] / 2;
	cout << pair << endl;

	return 0;
}