#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    vector<int>::iterator itr;
    int n, x;
    vector<int> v;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> x;
        v.push_back(x);
    }

    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> x;
        itr = lower_bound(v.begin(), v.end(), x);
        if (x == *itr)
            cout << "Yes " << (itr - v.begin() + 1) << endl;
        else
            cout << "No " << (itr - v.begin() + 1) << endl;
    }

    return 0;
}
