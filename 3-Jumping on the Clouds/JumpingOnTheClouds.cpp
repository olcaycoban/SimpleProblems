#include "pch.h"
#include <iostream>


using namespace std;


int n, c[101];

int main() {

	cin >> n;

	for (int i = 0; i < n; i++) 
		cin >> c[i];

	int result = 0;

	for (int i = 0; i < n - 1; ) {
		if (c[i + 2] != 1)
			i += 2;
		else
			i++;
		result++;
	}

	cout << result;

	return 0;
}