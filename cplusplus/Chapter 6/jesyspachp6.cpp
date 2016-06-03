#include <iostream>
#include <vector>

int main() {
	int x;
	std::vector<int> v;

	std::cout << "Enter as many numbers as you want:\n";
	while (std::cin >> x)
		v.push_back(x);

	if (v.empty()) {
		std::cout << "An Empty Sequence.\n";
		return 0;
	}

	std::size_t greatest_index = 0;
	std::size_t least_index = 0;

	for (std::size_t i = 0; i < v.size(); ++i) {
		if (v[i] > v[greatest_index])
			greatest_index = i;
		if (v[i] < v[least_index])
			least_index = i;
	}

	std::cout << "Greatest Element " << v[greatest_index] << " is at index " << greatest_index << ".\n";
	std::cout << "Least element " << v[least_index] << " is at index " << least_index << ".\n";

	int total = 0;
	for (int e : v)
		total += e;

	std::cout << "Sum: " << total << "\n";
	std::cout << "Interger Average: " << total/v.size() << "\n";

	for (auto e : v)
		std::cout << "v contains: " << e << "\n";

	return 0;
}