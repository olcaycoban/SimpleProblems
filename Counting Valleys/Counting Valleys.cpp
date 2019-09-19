#include "pch.h"
#include <iostream>
#include <cmath>
#include <string>

using namespace std;


int main() {
	int n;
	cin >> n;
	string s;
	cin >> s;
	int x = 0, count = 0;
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == 'U') x++;
		if (s[i] == 'D') x--;

		if (x == 0 && s[i] == 'U') 
			count++;
	}
	cout << count << endl;
	return 0;
}