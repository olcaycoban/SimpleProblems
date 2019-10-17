#include "pch.h"
#include <iostream>

using namespace std;

int ar[101] = {};

int main()
{
	int rotate;
	int n;
	cin >> rotate;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> ar[i];
	}

	for (int i = 0; i < n; i++) {
		cout << ar[(i + rotate) % n] << "";
	}
}
