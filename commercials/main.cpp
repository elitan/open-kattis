#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<string> &split(const string &s, char delim, vector<string> &elems) {
	stringstream ss(s);
	string item;
	while (getline(ss, item, delim)) {
		elems.push_back(item);
	}
	return elems;
}

int max(int a, int b) {
	return a > b ? a : b;
}

vector<string> split(const string &s, char delim) {
	vector<string> elems;
	split(s, delim, elems);
	return elems;
}

int main() {
	
	string tmpline;
	vector<string> tmparr;
	int p,
		tmph,
		max_ending_here = 0,
		max_so_far = 0;
	size_t n;
	std::string line;
	vector<int> distribution;
		
	// n and p
	getline(cin, tmpline);
	tmparr = split(tmpline, ' ');
	n = stoi(tmparr[0]);
	p = stoi(tmparr[1]);

	// dist
	getline(std::cin, line);
	std::istringstream iss(line);
	int enterNumber;
	while (iss >> enterNumber)
	{
		distribution.push_back(enterNumber - p);
	}

	// Kadane's algorithm
	for(size_t i = 0; i < n; i++) {
		max_ending_here = max(0, max_ending_here + distribution[i]);
		max_so_far = max(max_so_far, max_ending_here);
	}
	
	cout << max_so_far << endl;

	return 0;
}

