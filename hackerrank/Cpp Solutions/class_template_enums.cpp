#include <iostream>
using namespace std;
enum class Fruit { apple, orange, pear };
enum class Color { red, green, orange };

template <typename T> struct Traits;
template<class T>
class Traits{
public:
    static string name(int);
};

template<>
string Traits<Color>::name(int ind){
    switch(ind){
        case 0:
            return "red";
        case 1:
            return "green";
        case 2:
            return "orange";
        default:
            return "unknown";
    }
}

template<>
string Traits<Fruit>::name(int ind){
    switch(ind){
        case 0:
            return "apple";
        case 1:
            return "orange";
        case 2:
            return "pear";
        default:
            return "unknown";
    }
}
// Define specializations for the Traits class template here.

