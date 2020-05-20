#include <iostream>
#include <deque>
#include <sstream>
#include <vector>
using namespace std;

void printKMax(vector<int>& arr, int n, int k) {
    deque<int> dq;
    for (int i = 0; i < n; i++) {
        while (!dq.empty() && dq.front() <= (i - k))
            dq.pop_front();
        if (dq.empty())
            dq.push_back(i);
        while (!dq.empty() && arr[i] >= arr[dq.back()]) {
            dq.pop_back();
        }
        dq.push_back(i);

        if (i >= k - 1)
            cout << arr[dq.front()] << " ";
    }
    cout << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t, n, k;
    int i, val;
    string str, input;
    getline(cin, input);
    t = stoi(input);
    for (int i = 0; i < t * 2; ++i) {
        getline(cin, input);
        str += input + '\n';
    }
    stringstream ss(str);
    while (ss >> n >> k) {
        vector<int> arr;
        for (i = 0; i < n; i++) {
            ss >> val;
            arr.push_back(val);
        }
        printKMax(arr, n, k);
    }
    return 0;
}