// Hack around stdlib bug with C++14.
#include <initializer_list>  // force libstdc++ to include its config
#undef _GLIBCXX_HAVE_GETS    // correct broken config
// End hack.

#include <iostream>
#include <vector>
#include <string>

std::vector<int> read_int_vector() {
	std::vector<int> result;
	int x;

	std::cout << "Enter as many numbers as you'd like:\n";

	while (true) {
		while (std::cin >> x)
			result.push_back(x);
		if (std::cin.eof()) {
			break;
		}
	std::cin.clear();
	std::string s;
	std::getline(std::cin, s); 

	std::cout << "Warning, ignoring: " << s << "\n";
	}

	std::cout << "End of File encountered, stopping.\n";
	return result;
}

int average(std::vector<int> v);
int sum(std::vector<int> v);
std::vector<int> filter_greater_than(std::vector<int> v, int x);

int main() {
	auto v = read_int_vector();
	std::cout << "Average: " << average(v) << "\n";
	std::cout << "Sum: " << sum(v) << "\n";

	std::cout << "Elements greater than 5:";
	for (auto e : filter_greater_than(v, 5))
		std::cout << " " << e;
	std::cout << "\n";

	return 0;
	}

int average(std::vector<int> v) {
	if (v.empty())
		return 0;
	int size = v.size();
	return sum(v)/size;
	}

int sum(std::vector<int> v) {
	int total = 0;
	for (auto e : v)
		total += e;
	return total;
}

std::vector<int> filter_greater_than(std::vector<int> v, int x) {
	std::vector<int> result;
	for (auto e : v)
		if (e > x)
			result.push_back(e);
	return result;
}