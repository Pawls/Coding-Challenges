#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

const long long mod = pow(2, 31);

int main() {
    int n,count = 0;
    long long s, p, q;
    cin >> n >> s >> p >> q;
    unsigned long long val = s % mod;
    unsigned long long val_prev = val;
    int i;
    for (i = 1; i < n; ++i) {
        val = (val * p + q) % mod;
        if (val == val_prev || val == s) {
            count = i;
            break;
        }
        val_prev = val;
    }
    if (i == n)
        count = n;

    cout << count << endl;
    system("Pause");
    return 0;
}
