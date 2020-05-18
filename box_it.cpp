#include <iostream>
using namespace std;

class Box {
	int l, b, h;
public:
	Box() { l = b = h = 0; };
	Box(int length, int breadth, int height) {
		l = length;
		b = breadth;
		h = height;
	};
	Box(Box& box1) {
		l = box1.l;
		b = box1.b;
		h = box1.h;
	};
	int getLength() {// Return box's length
		return l;
	}; 
	int getBreadth() { // Return box's breadth
		return b;
	};
	int getHeight() {//Return box's height
		return h;
	};  
	long long CalculateVolume() {// Return the volume of the box
		return (long long)l * b * h;
	};

	bool operator<(Box& other) {
		if (l < other.l)
			return true;
		else if (b < other.b && l == other.l)
			return true;
		else if (h < other.h && l == other.l && b == other.b)
			return true;
		else
			return false;
	}

	friend ostream& operator<<(ostream& out, Box& box1) {
		out << box1.l << " " << box1.b << " " << box1.h;
		return out;
	}
};


void check2()
{
	int n; // number of trials
	cin >> n;
	Box temp;
	for (int i = 0; i < n; i++)
	{
		int type; // type of trial
		cin >> type;
		if (type == 1) // Testing default constructor
		{
			cout << temp << endl;
		}
		if (type == 2) // Testing parameterized constructor
		{
			int l, b, h;
			cin >> l >> b >> h;
			Box NewBox(l, b, h);
			temp = NewBox;
			cout << temp << endl;
		}
		if (type == 3) // Test overloaded <
		{
			int l, b, h;
			cin >> l >> b >> h;
			Box NewBox(l, b, h);
			if (NewBox < temp)
			{
				cout << "Lesser\n";
			}
			else
			{
				cout << "Greater\n";
			}
		}
		if (type == 4) // Test function
		{
			cout << temp.CalculateVolume() << endl;
		}
		if (type == 5) // Test copy constructor
		{
			Box NewBox(temp);
			cout << NewBox << endl;
		}

	}
}

int main()
{
	check2();
}