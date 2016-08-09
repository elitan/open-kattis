#include <iostream>
#include <string>
#include <unistd.h>

int main() {
    int m =1000001,
        x,
		sum_holder,
		count_arr[1000001];
	std::string tmp;
	
	// zero the array
	for(int i = 0; i < m; i++) {
		count_arr[i] = 0;
	}

	// set each starting point for a house
    for(int i = 2; i < m+1; i++) {
        x = i;
        sum_holder = x;
		// add the previous, and add 1 to a count_arr array
        while(sum_holder <= m) {
            count_arr[sum_holder] += 1;
            x++;
            sum_holder += x;
        }
    }

    for (std::string line; std::getline(std::cin, line);) {
        x = std::stoi(line);
        if(x == 0)
            break;
        std::cout << count_arr[x] << std::endl;
    }
}
