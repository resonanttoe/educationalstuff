#include <iostream>
#include <vector>

int main() {
	int x;
	std::vector<int> v;

	std::cout << "Enter as many numbers as you'd like:\n";
	while (std::cin >> x) {
		v.push_back(x);
		}
	std::size_t i = 0;
	std::size_t greatest_index = 0;
	std::size_t least_index = 0;

	while (i < v.size()) {
		if (v[i] > v[greatest_index])
			greatest_index = i;
		if (v[i] > v[least_index])
			least_index = i;
		i += 1;
		}
		if (v.empty()) {
			std::cout << "Empty sequence";
		} else {
				std::cout << "Total Element number " << v.size()  << ".\n";
				std::cout << "Greatest Element " << v[greatest_index] << " is at index " << greatest_index << ".\n";
				std::cout << "Least Element " << v[least_index] << " is at index " << least_index << ".\n";
		}
		return 0;
	}