#include "pch.h"
#include <iostream>
#include<algorithm> 


using namespace std;


int main()
{
	int ar[6][6] = {};
	int temp;
	int m;

	for (int i = 0; i < 6; i++) {
		for (int j = 0; j < 6; j++) {
			cin >> ar[i][j];
		}
	}
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			temp = ar[i][j] + ar[i][j + 1] + ar[i][j + 2] +
				             ar[i + 1][j + 1] +
				ar[i + 2][j] + ar[i + 2][j + 1] + ar[i + 2][j + 2];
			m = max(m, temp);
		}
	}

	cout << m;
}