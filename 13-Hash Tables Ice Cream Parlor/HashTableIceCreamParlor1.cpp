#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

map<int,int>::iterator it;

int main() {
	int T;
	cin>>T;
	while(T > 0) {
		int M, N;
		cin>>M>>N;
		map<int, int> m; 
		int *c = new int[N];
		for(int i = 0; i < N; i++) {
			cin>>c[i];
			if(m.count(c[i]) == 0) {
				m.insert(pair<int, int>(c[i], i));
			} else if(c[i] == M/2) {
				m[c[i]] = i;
			}
		}
		for(int i = 0; i < N; i++) {
			it = m.find(M-c[i]);
			if(it != m.end()) {
				int index = it->second;
				int index2 = i;
				if(index == index2) {
					continue;
				}
				if(index > index2) {
					cout<<index2+1<<" "<<index+1<<"\n";
				} else {
					cout<<index+1<<" "<<index2+1<<"\n";
				}
				break;
			}
		}
		T--;
	}
    return 0;
}