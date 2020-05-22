#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stdio.h>
using namespace std;
class Person {
protected:
    int age;
    string name;
    //virtual int cur_id;
public:
    virtual void getdata() { cout << "failed\n"; }
    virtual void putdata() { cout << "failed\n"; }
};

class Professor : public Person {
    static int cur_id;
    int publications;
    int id;
public:
    Professor() { id = ++cur_id; }
    void getdata() {
        char temp[101];
        scanf("%s", temp);
        name = temp;
        scanf("%d", &age);
        scanf("%d", &publications);
    }
    void putdata() {
        printf("%s %d %d %d\n", name.c_str(), age, publications, id);
    }
};
int Professor::cur_id = 0;

class Student : public Person {
    static int cur_id;
    int marks[6];
    int id;
public:
    Student() { id = ++cur_id; }
    void getdata() {
        char temp[101];
        scanf("%s", temp);
        name = temp;
        scanf("%d", &age);
        for (int i = 0; i < 6; ++i)
            scanf("%d", &marks[i]);
    }
    void putdata() {
        int sum = 0;
        for (int i = 0; i < 6; ++i)
            sum += marks[i];
        printf("%s %d %d %d\n", name.c_str(), age, sum, id);
    }
};
int Student::cur_id = 0;

int main() {

    int n, val;
    cin >> n; //The number of objects that is going to be created.
    Person* per[n];

    for (int i = 0; i < n; i++) {

        cin >> val;
        if (val == 1) {
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for (int i = 0; i < n; i++)
        per[i]->putdata(); // Print the required output for each object.
    delete [] per;
    return 0;
}
