#include "pch.h"
#include <iostream>

using namespace std;

int main()
{
	int ar[101] = {};
	int br = 0;
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> ar[i];
	}
	for (int i = 0; i < n-1; i++) {
		for (int j = i+1; j < n; j++) {
			if (ar[i] > ar[j]) {
				br++;
			}
		}
	}
	cout << br;
}