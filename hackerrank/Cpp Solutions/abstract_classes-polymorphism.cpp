#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>
using namespace std;

struct Node {
    Node* next;
    Node* prev;
    int value;
    int key;
    Node(Node* p, Node* n, int k, int val) :prev(p), next(n), key(k), value(val) {};
    Node(int k, int val) :prev(NULL), next(NULL), key(k), value(val) {};
};

class Cache {

protected:
    map<int, Node*> mp; //map the key to the node in the linked list
    int cp;  //capacity
    Node* tail; // double linked list tail pointer
    Node* head; // double linked list head pointer
    virtual void set(int, int) = 0; //set function
    virtual int get(int) = 0; //get function

};
class LRUCache : public Cache {
public:
    ~LRUCache() {
        Node* ptr = tail;
        while (ptr->prev) {
            ptr = ptr->prev;
            delete ptr->next;
        }
    }
    LRUCache(int capacity) { cp = capacity; }
    void set(int x, int y) {
        if (!mp[x])
            mp[x] = new Node(x, y);
        else {
            mp[x]->value = y;
            return;
        }

        if (mp.size() == 1)
            tail = head = mp[x];
        else if (head != mp[x]) {
            if (mp[x]->prev)
                mp[x]->prev->next = mp[x]->next;
            if (mp[x]->next)
                mp[x]->next->prev = mp[x]->prev;
            mp[x]->next = head;
            mp[x]->prev = NULL;
            head->prev = mp[x];
            head = mp[x];
            if (mp.size() > cp) {
                tail = tail->prev;
                mp.erase(tail->next->key);
                delete tail->next;
                tail->next = NULL;
            }
        }
    }
    int get(int x) {
        std::map<int, Node*>::iterator itr;
        itr = mp.find(x);
        if (itr != mp.end()) {
            return mp[x]->value;
        }
        else return -1;
    }
};
int main() {
    int n, capacity, i;
    cin >> n >> capacity;
    LRUCache l(capacity);
    for (i = 0; i < n; i++) {
        string command;
        cin >> command;
        if (command == "get") {
            int key;
            cin >> key;
            cout << l.get(key) << endl;
        }
        else if (command == "set") {
            int key, value;
            cin >> key >> value;
            l.set(key, value);
        }
    }
    return 0;
}
