#include "pch.h"
#include <iostream>
#define REP for (int i = 0; i < n; i++)

using namespace std;

int main() {
	int ar[101] = {};
	int n; int temp = 0; int z = 0;
	cin >> n;
	int mon;
	cin >> mon;
	int count = 0;
	REP cin >> ar[i];
	for (int i = 0; i < n - 1; i++) {
		for (int j = i + 1; j < n; j++) {
			if (ar[i] > ar[j]) {
				temp = ar[j];
				ar[j] = ar[i];
				ar[i] = temp;
			}
		}
	}

	while (mon -= ar[z]>0)
	{
		count++;
		z++;
	}	
	cout << count;
	return 0;
}