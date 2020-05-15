#include <vector>
#include <iostream>
#include <cmath>
using namespace std;

template<bool...digits>
int reversed_binary_value(){
    vector<bool> args = {digits...};
    int result = 0;
    for(int i = 0; i<args.size(); ++i){
        result += int(args[i])*pow(2,i);
    }
    return result;
}

int main(){
    cout << reversed_binary_value<0>() << endl; //
    cout << reversed_binary_value<>() << endl; //
    cout << reversed_binary_value<1,1>() << endl; //3
    cout << reversed_binary_value<0,0,0,1>() << endl; //8
    return 0;
}
