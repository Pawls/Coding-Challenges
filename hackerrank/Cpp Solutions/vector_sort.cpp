#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int length;
    int val;
    vector<int> v;
    cin >> length;
    for(int i=0;i<length;++i){
        cin >> val;
        v.push_back(val);
    }
    sort(v.begin(),v.end());
    for(int i: v)
        cout << i << " ";
    cout << '\n';
    return 0;
}
